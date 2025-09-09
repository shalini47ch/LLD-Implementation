
from ParkingLot.Vehicle import Vehicle
from ParkingLot.ParkingFeeStrategy import ParkingFeeStrategy

class Auto(Vehicle):
    def __init__(self,licensePlate:str,vehicleType:str,feeStrategy:ParkingFeeStrategy):
        super().__init__(licensePlate,vehicleType,feeStrategy)

#creating an auto vehicle class which will inherit from the vehicle class
