from abc import ABC, abstractmethod
from ParkingLot.enums.DurationTypes import DurationTypes
from ParkingLot.ParkingFeeStrategy import ParkingFeeStrategy

class Vehicle(ABC):
    def __init__(self,licensePlate:str,vehicleType:str,feeStrategy:ParkingFeeStrategy):
        self._licensePlate=licensePlate
        self._vehicleType=vehicleType
        self._feeStrategy=feeStrategy
        
    #now since the parameters are private we need to create getters and setters to access them
    def getLicensePlate(self)->str:
        return self._licensePlate
    
    def getVehicleType(self)->str:
        return self._vehicleType
    
    #now the next is to calcualtethe parking feee for that vehicle 
    def calculate_fee(self,duration:int,durationType:DurationTypes):
        fee=self._feeStrategy.calculate_fee(self._vehicleType,duration,durationType)
        print(f"[DEBUG] Fee calculated for {self._licensePlate}: {fee}") 
        return fee
        
    
    
        


   
