#now the parking lot will have parking spots and will also have the functionality of parkvehicle or vacatethespot

class ParkingLot:
    def __init__(self,parkingspots):
        self.parkingspots=parkingspots
    
    def findavailableSpots(self,vehicletype):
        #iterate through the parking spots
        for spot in self.parkingspots:
            if not spot.isOccupied() and spot.getSpotType()==vehicletype:
                return spot
        return None #meaning we were not able to find available slot
    
    def parkVehicle(self,vehicle):
        spot=self.findavailableSpots(vehicle.getVehicleType())
        if spot:
            spot.parkVehicle(vehicle)
            print(f"Vehicle parked successfully in spot:{spot.getSpotNumber()}")
            return spot
        print(f"No parking spots available to park the vehicle")
        return None 
    
    #now the next helper function is to vacate
    def vacateSpot(self,spot,vehicle):
        if spot and spot.isOccupied() and spot.getVehicle()==vehicle:
            spot.vacate()
            print(f"vehicle {vehicle.getVehicleType()} vacated the spot {spot.getSpotNumber()}")
        else:
            print(f"The spot is already vacate")
        
    def getSpotByNumber(self,spotnumber):
        for spot in self.parkingspots:
            if spot.getSpotNumber()==spotnumber:
                return spot
        return None 
    


        
        