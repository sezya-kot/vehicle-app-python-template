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

# skip B101

from unittest import mock

import pytest
from sdv.vehicle_app import VehicleApp

from vdm.proto.seats_pb2 import BASE, SeatLocation
from vdm.SeatService import SeatService


@pytest.mark.asyncio
async def test_for_seats_movecomponent():
    # Disable no-value-for-parameter, seems to be false positive with mock lib
    # pylint: disable=no-value-for-parameter
    with mock.patch.object(
        SeatService,
        "MoveComponent",
        new_callable=mock.AsyncMock,
        return_value=get_sample_request_data(),
    ):
        location = SeatLocation(row=1, index=1)
        get_position = get_sample_request_data()
        response = await SeatService.MoveComponent(
            location, BASE, get_position["position"]  # type: ignore
        )
        assert response == get_sample_request_data()


@pytest.mark.asyncio
async def test_for_seats_movecomponent_set_high_position():
    # Disable no-value-for-parameter, seems to be false positive with mock lib
    # pylint: disable=no-value-for-parameter
    with mock.patch.object(
        SeatService,
        "MoveComponent",
        new_callable=mock.AsyncMock,
        return_value=get_error_invalid_arg_response(),
    ):
        location = SeatLocation(row=1, index=1)
        set_position = set_seat_position_high()
        response = await SeatService.MoveComponent(
            location, BASE, set_position["position"]  # type: ignore
        )
        assert response == get_error_invalid_arg_response()


@pytest.mark.asyncio
async def test_for_seats_movecomponent_error_path():
    # Disable no-value-for-parameter, seems to be false positive with mock lib
    # pylint: disable=no-value-for-parameter
    with mock.patch.object(
        SeatService,
        "MoveComponent",
        new_callable=mock.AsyncMock,
        return_value=get_error_response(),
    ):
        location = SeatLocation(row=1, index=1)
        get_position = get_sample_request_data()
        response = await SeatService.MoveComponent(
            location, BASE, get_position["position"]  # type: ignore
        )
        assert response == get_error_response()


@pytest.mark.asyncio
async def test_for_publish_to_topic():
    # Disable no-value-for-parameter, seems to be false positive with mock lib
    # pylint: disable=no-value-for-parameter

    with mock.patch.object(
        VehicleApp, "publish_mqtt_event", new_callable=mock.AsyncMock, return_value=-1
    ):
        response = await VehicleApp.publish_mqtt_event(
            str("sampleTopic"), get_sample_request_data()  # type: ignore
        )
        assert response == -1


def get_sample_request_data():
    return {"position": 330, "requestId": "123456789"}


def set_seat_position_high():
    return {"position": 1001, "requestId": "123456789"}


def get_error_invalid_arg_response():
    data = set_seat_position_high()
    error_msg = f"""Provided position {data["position"]}  \
        should not be Greater than 1000 (Max)"""
    resp_data = {
        "requestId": data["requestId"],
        "result": {"status": 1, "message": error_msg},
    }
    return resp_data


def get_sample_response():
    get_position = get_sample_request_data()
    resp_data = {
        "requestId": {"requestId": get_position["position"], "result": {"status": 0}}
    }
    return resp_data


def get_error_response():
    data = get_sample_request_data()
    error_msg = "Received unknown RPC error"
    resp_data = {
        "requestId": data["requestId"],
        "result": {"status": 1, "message": error_msg},
    }
    return resp_data
