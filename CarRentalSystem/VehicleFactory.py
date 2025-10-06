
from CarRentalSystem.enums.VehicleType import VehicleType
from CarRentalSystem.Economy import Economy
from CarRentalSystem.Luxury import Luxury
from CarRentalSystem.SUV import SUV
from CarRentalSystem.Sedan import Sedan
from CarRentalSystem.enums import VehicleStatus 
from CarRentalSystem.enums import ReservationStatus
from CarRentalSystem.Bike import Bike 
from CarRentalSystem.Auto import Auto

class VehicleFactory:
    
    @staticmethod
    def create_vehicle(vehicle_type, registration_number, model, year,type, status, base_rental_price):
        if(vehicle_type==VehicleType.ECONOMY):
            return Economy(registration_number,model,year,type,status,base_rental_price)
        elif(vehicle_type==VehicleType.LUXURY):
            return Luxury(registration_number,model,year,type,status,base_rental_price)
        elif(vehicle_type==VehicleType.SUV):
            return SUV(registration_number,model,year,type,status,base_rental_price)
        elif(vehicle_type==VehicleType.SEDAN):
            return Sedan(registration_number,model,year,type,status,base_rental_price)
        #we will also add for Bike and Auto
        elif(vehicle_type==VehicleType.BIKE):
            return Bike(registration_number,model,year,type,status,base_rental_price)
        elif(vehicle_type==VehicleType.AUTO):
            return Auto(registration_number,model,year,type,status,base_rental_price)
        else:
            raise ValueError(f"Unsupported vehicle type:{vehicle_type}")
        
    
            
        
    