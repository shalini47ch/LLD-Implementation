from enum import Enum

class ReservationStatus(Enum):
    PENDING="Pending"
    CONFIRMED="Confirmed"
    CANCELLED="Cancelled"
    COMPLETED="Completed"
    INPROGRESS="InProgress"