
#here we will create an abstract class for a vehicle and then this will be used to create different vehicles like economy,premium and suv
from abc import ABC, abstractmethod
from CarRentalSystem.enums.VehicleType import VehicleType
from CarRentalSystem.enums.VehicleStatus import VehicleStatus

class Vehicle(ABC):
    def __init__(self,registrationNumber:str,model:str,year:int,type:VehicleType,status:VehicleStatus,baseRentalPrice:float):
        #now we will declare the constructors accordingly
        self._registrationNumber=registrationNumber
        self._model=model
        self._year=year
        self._type=type
        self._status=status
        self._baseRentalPrice=baseRentalPrice
    
    @abstractmethod
    def calculateRentalPrice(self,days:int)->float:
        pass
    
    #now adding the specific getters and setters 
    def get_registration_number(self):
        return self._registrationNumber
    
    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_type(self):
        return self._type

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_base_rental_price(self):
        return self._baseRentalPrice

        