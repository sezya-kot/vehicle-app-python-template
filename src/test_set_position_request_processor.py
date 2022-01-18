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

from sdv.client import VehicleClient

from set_position_request_processor import SetPositionRequestProcessor


def test_request_processor():
    processor = get_set_position_request_processor_instance()
    response = processor._SetPositionRequestProcessor__get_processed_response(
        get_sample_request_data(), get_vehicle_client_instance()
    )
    message = response["result"]["message"]
    has_exception = message.__contains__("Exception details:")
    assert has_exception


def test_for_exception_with_bfb_app_publish_data_to_topic():
    processor = get_set_position_request_processor_instance()
    response_status = processor._SetPositionRequestProcessor__publish_data_to_topic(
        get_sample_request_data(), "bfb-app", get_vehicle_client_instance()
    )
    assert response_status == -1


def test_for_exception_with_gui_app_publish_data_to_topic():
    processor = get_set_position_request_processor_instance()
    response_status = processor._SetPositionRequestProcessor__publish_data_to_topic(
        get_sample_request_data(), "gui-app", get_vehicle_client_instance()
    )
    assert response_status == -1


def get_sample_request_data():
    return {"position": 330, "requestId": "123456789"}


def get_set_position_request_processor_instance():
    return SetPositionRequestProcessor()


def get_vehicle_client_instance():
    return VehicleClient(50051)
