
from abc import ABC, abstractmethod
from ParkingLot.Vehicle import Vehicle

class ParkingSpot(ABC):
    def __init__(self,spotNumber:int,spotType:str):
        self._spotNumber=spotNumber
        self._spotType=spotType
        self._vehicle=None
        self._isOccupied=False
    
    @abstractmethod
    def can_park_vehicle(self,vehicle:Vehicle):
        pass
    
    def getSpotNumber(self)->int:
        return self._spotNumber
    
    def getSpotType(self)->str:
        return self._spotType
    
    def isOccupied(self)->bool:
        return self._isOccupied
    
    def getVehicle(self):
        return self._vehicle
    
    #we can park the vehicle on that spot and also vacate it
    
    def parkVehicle(self,vehicle:Vehicle):
        if self._isOccupied:
            #meaning it is already occupied so return spot is already occupied
            raise Exception("Parking Spot is already occupied")
        if not self.can_park_vehicle(vehicle):
            raise Exception("This vehicle is not suitable for {vehicle.getVehicleType()} spot".format(vehicle=vehicle))
        
        self._vehicle=vehicle
        self._isOccupied=True
    
    def vacate(self):
        if not self.isOccupied:
            raise Exception("The parking spot is already vacant")
        self._vehicle=None
        self._isOccupied=False
    
    
    
    

        
        
        
        
        
        