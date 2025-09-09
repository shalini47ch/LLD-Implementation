from abc import ABC,abstractmethod 
from ParkingLot.enums.DurationTypes import DurationTypes

class ParkingFeeStrategy(ABC):
    @abstractmethod 
    def calculate_fee(self,vehicleType:str,duration:int,durationType:DurationTypes):
        pass

