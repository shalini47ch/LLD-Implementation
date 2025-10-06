
from CarRentalSystem.Vehicle import Vehicle
from CarRentalSystem.enums.VehicleType import VehicleType
from CarRentalSystem.enums.VehicleStatus import VehicleStatus

class Auto(Vehicle):
    def __init__(self,registrationNumber:str,model:str,year:int,type:VehicleType,status:VehicleStatus,baseRentalPrice:float):
        super().__init__(registrationNumber,model,year,type,status,baseRentalPrice)
        self.ratemultiplier=1.2 

    def calculateRentalPrice(self, days):
        return self.get_base_rental_price()*days*self.ratemultiplier
    
  