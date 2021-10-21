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


from __future__ import print_function

from cloudevents.sdk.event import v1
from dapr.ext.grpc import App
import logging
from seat_adjuster import SeatAdjuster
import json

app = App()


@app.subscribe(pubsub_name='mqtt-pubsub', topic='SEATPOSITION')
def onSeatPositionUpdate(event: v1.Event) -> None:
    data = json.loads(event.Data())
    print(f'Subscriber received: id={data["id"]}, SeatPosition="{data["SeatPosition"]}", content_type="{event.content_type}"', flush=True)  # noqa: E501


if __name__ == '__main__':
    logging.basicConfig()
    seatAdjuster = SeatAdjuster()
    seatAdjuster.start()
    app.run(50008)
