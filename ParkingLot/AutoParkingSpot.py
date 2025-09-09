from ParkingLot.ParkingSpot import ParkingSpot

class AutoParkingSpot(ParkingSpot):
    def __init__(self,spotNumber:int,spotType:str):
        super().__init__(spotNumber,spotType)
    
    def can_park_vehicle(self,vehicle):
        return vehicle.getVehicleType().lower()=="auto"