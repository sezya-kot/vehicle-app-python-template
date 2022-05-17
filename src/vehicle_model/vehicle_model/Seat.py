# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

# pylint: disable=C0103

from sdv.model import DataPointBoolean, Model


class Seat(Model):
    """
    A class used to represent Seat model

    ...

    Attributes
    ----------
    Position : DataPointBoolean
        an object instantiation of DataPointBoolean class
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.Position = DataPointBoolean("Position", self)
