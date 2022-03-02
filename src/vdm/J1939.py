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

"""J1939 Model"""

# pylint: disable=C0103, disable=R0902

from sdv.model import (
    DataPointFloat,
    DataPointSInt32,
    DataPointUInt32,
    ListSpec,
    Model,
    ModelSpec,
    RangeSpec,
)


class PGN6144(Model):
    """PGN6144 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.EngineSpeed = DataPointFloat("EngineSpeed", self)


class PGN61443Instances:
    """PGN61443 Instances"""

    SA0 = "SA0"


class PGN61443(Model):
    """PGN61443 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.VehicleAccelerationRateLimitStatus = DataPointUInt32(
            "VehicleAccelerationRateLimitStatus", self
        )
        self.DPFThermalManagementActive = DataPointUInt32(
            "DPFThermalManagementActive", self
        )
        self.AcceleratorPedalPosition1 = DataPointUInt32(
            "AcceleratorPedalPosition1", self
        )
        self.EnginePercentLoadAtCurrentSpeed = DataPointUInt32(
            "EnginePercentLoadAtCurrentSpeed", self
        )
        self.RemoteAcceleratorPedalPosition = DataPointFloat(
            "RemoteAcceleratorPedalPosition", self
        )


class PGN61441Instances:
    """PGN61441 Instances"""

    SA0 = "SA11"


class PGN61441(Model):
    """PGN61441 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.RemoteAcceleratorEnableSwitch = DataPointUInt32(
            "RemoteAcceleratorEnableSwitch", self
        )


class PGN61440Instances:
    """PGN61440 Instances"""

    SA15 = "SA15"


class PGN61440(Model):
    """PGN61440 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.ActualRetarderPercentTorque = DataPointSInt32(
            "ActualRetarderPercentTorque", self
        )
        self.DriversDemandRetarder = DataPointSInt32("DriversDemandRetarder", self)


class PGN57344Instances:
    """PGN57344 Instances"""

    SA49 = "SA49"
    SA39 = "SA39"


class PGN57344(Model):
    """PGN57344 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.AftertreatmentRegenerationInhibitSwitch = DataPointUInt32(
            "AftertreatmentRegenerationInhibitSwitch", self
        )


class PGN65276(Model):
    """PGN65276 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.FuelLevel1 = DataPointFloat("FuelLevel1", self)


class PGN65217Instances:
    """PGN65217 Instances"""

    SA49 = "SA49"
    SA39 = "SA39"
    SA0 = "SA0"


class PGN65217(Model):
    """PGN65217 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.VehicleDistanceTotalHR = DataPointFloat("VehicleDistanceTotalHR", self)


class PGN65248Instances:
    """PGN65248 Instances"""

    SA49 = "SA49"
    SA39 = "SA39"
    SA0 = "SA0"


class PGN65248(Model):
    """PGN65248 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.VehicleDistanceTotal = DataPointFloat("VehicleDistanceTotal", self)


class PGN65226(Model):
    """PGN65226 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.LampStatus = DataPointUInt32("LampStatus", self)
        self.SPN = DataPointUInt32("SPN", self)
        self.FMI = DataPointUInt32("FMI", self)
        self.SPNConversion = DataPointUInt32("SPNConversion", self)
        self.OccurenceCount = DataPointUInt32("OccurenceCount", self)


class J1939(Model):
    """J1939 model"""

    def __init__(self, parent: Model):
        super().__init__(parent)

        self.PGN65226 = ModelSpec[PGN65226]([RangeSpec("SA", 0, 254)], PGN65226(self))
        self.PGN65248 = ModelSpec[PGN65248]([ListSpec(PGN65248)], PGN65226(self))
        self.PGN65217 = ModelSpec[PGN65217]([ListSpec(PGN65217)], PGN65217(self))
        self.PGN65276 = ModelSpec[PGN65276]([RangeSpec("SA", 0, 254)], PGN65276(self))
        self.PGN57344 = ModelSpec[PGN57344]([ListSpec(PGN57344)], PGN57344(self))
        self.PGN61440 = ModelSpec[PGN61440]([ListSpec(PGN61440)], PGN61440(self))
        self.PGN61441 = ModelSpec[PGN61441]([ListSpec(PGN61441)], PGN61441(self))
        self.PGN61443 = ModelSpec[PGN61443]([ListSpec(PGN61443)], PGN61443(self))
        self.PGN6144 = ModelSpec[PGN6144]([RangeSpec("SA", 0, 254)], PGN6144(self))
