from ParkingLot.ParkingSpot import ParkingSpot

class OtherVehicleParkingSpot(ParkingSpot):
    def __init__(self,spotNumber:int,spotType:str):
        super().__init__(spotNumber,spotType)
    
    def can_park_vehicle(self,vehicle):
        return vehicle.getVehicleType().lower()=="other"