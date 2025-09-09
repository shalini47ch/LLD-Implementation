#here we will create a vehicle factory class which will create different types of vehicles based on the input
from ParkingLot.CarVehicle import CarVehicle
from ParkingLot.Bike import BikeVehicle
from ParkingLot.Auto import Auto
from ParkingLot.ParkingFeeStrategy import ParkingFeeStrategy
from ParkingLot.OtherVehicle import OtherVehicle

class VehicleFactory:
    @staticmethod
    def create_vehicle(licensePlate:str,vehicleType:str,feeStrategy:ParkingFeeStrategy):
        if vehicleType=="car":
            return CarVehicle(licensePlate,vehicleType,feeStrategy)
        
        elif vehicleType=="bike":
            return BikeVehicle(licensePlate,vehicleType,feeStrategy)
        
        elif vehicleType=="auto":
            return Auto(licensePlate,vehicleType,feeStrategy)
        
        else:
            return OtherVehicle(licensePlate,vehicleType,feeStrategy)
        
        