from enum import Enum

class VehicleStatus(Enum):
    AVAILABLE="Available",
    RESERVED="Reserved",
    RENTED="Rented",
    MAINTENANCE="Maintenance",
    OUTOFSERVICE="OutOfService"