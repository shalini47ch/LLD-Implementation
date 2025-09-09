
from ParkingLot.Vehicle import Vehicle
from ParkingLot.ParkingFeeStrategy import ParkingFeeStrategy

class OtherVehicle(Vehicle):
    def __init__(self,licensePlate:str,vehicleType:str,feeStrategy:ParkingFeeStrategy):
        super().__init__(licensePlate,vehicleType,feeStrategy)