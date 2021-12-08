# /********************************************************************************
# * Copyright (c) 2021 Contributors to the Eclipse Foundation
# *
# * See the NOTICE file(s) distributed with this work for additional
# * information regarding copyright ownership.
# *
# * This program and the accompanying materials are made available under the
# * terms of the Eclipse Public License 2.0 which is available at
# * http://www.eclipse.org/legal/epl-2.0
# *
# * SPDX-License-Identifier: EPL-2.0
# ********************************************************************************/


import grpc

from cloudevents.sdk.event import v1  # type: ignore
from typing import Callable, Dict, List, Optional, Tuple

from google.protobuf import empty_pb2
from google.protobuf.message import Message as GrpcMessage

from dapr.proto import appcallback_service_v1, appcallback_v1
from dapr.clients.base import DEFAULT_JSON_CONTENT_TYPE

TopicSubscribeCallable = Callable[[any, v1.Event], None]

DELIMITER = ":"


class Rule:
    def __init__(self, match: str, priority: int) -> None:
        self.match = match
        self.priority = priority


class _RegisteredSubscription:
    def __init__(self, subscription: appcallback_v1.TopicSubscription,
                 rules: List[Tuple[int, appcallback_v1.TopicRule]]):
        self.subscription = subscription
        self.rules = rules


class _CallbackServicer(appcallback_service_v1.AppCallbackServicer):
    def __init__(self):
        self._topic_map: Dict[str, TopicSubscribeCallable] = {}

        self._registered_topics_map: Dict[str, _RegisteredSubscription] = {}
        self._registered_topics: List[appcallback_v1.TopicSubscription] = []

    def register_topic(
            self,
            pubsub_name: str,
            topic: str,
            cb: TopicSubscribeCallable,
            metadata: Optional[Dict[str, str]],
            rule: Optional[Rule] = None) -> None:
        """Registers topic subscription for pubsub."""
        topic_key = pubsub_name + DELIMITER + topic
        pubsub_topic = topic_key + DELIMITER
        if rule is not None:
            path = getattr(cb, '__name__', rule.match)
            pubsub_topic = pubsub_topic + path
        if pubsub_topic in self._topic_map:
            raise ValueError(
                f'{topic} is already registered with {pubsub_name}')
        self._topic_map[pubsub_topic] = cb

        registered_topic = self._registered_topics_map.get(topic_key)
        sub: appcallback_v1.TopicSubscription = appcallback_v1.TopicSubscription()
        rules: List[Tuple[int, appcallback_v1.TopicRule]] = []
        if not registered_topic:
            sub = appcallback_v1.TopicSubscription(
                pubsub_name=pubsub_name,
                topic=topic,
                metadata=metadata,
                routes=appcallback_v1.TopicRoutes()
            )
            registered_topic = _RegisteredSubscription(sub, rules)
            self._registered_topics_map[topic_key] = registered_topic
            self._registered_topics.append(sub)

        sub = registered_topic.subscription
        rules = registered_topic.rules

        if rule:
            path = getattr(cb, '__name__', rule.match)
            rules.append((rule.priority, appcallback_v1.TopicRule(
                match=rule.match, path=path)))
            rules.sort(key=lambda x: x[0])
            rs = [rule for id, rule in rules]
            del sub.routes.rules[:]
            sub.routes.rules.extend(rs)

    def ListTopicSubscriptions(self, request, context):
        return appcallback_v1.ListTopicSubscriptionsResponse(
            subscriptions=self._registered_topics)

    def OnTopicEvent(self, request, context):
        pubsub_topic = request.pubsub_name + DELIMITER + \
            request.topic + DELIMITER + request.path
        if pubsub_topic not in self._topic_map:
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)  # type: ignore
            raise NotImplementedError(
                f'topic {request.topic} is not implemented!')

        tuple = self._topic_map[pubsub_topic](request.data)

        return empty_pb2.Empty()
