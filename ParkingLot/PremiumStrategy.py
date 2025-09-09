from ParkingLot.ParkingFeeStrategy import ParkingFeeStrategy
from ParkingLot.enums.DurationTypes import DurationTypes

class PremiumStrategy(ParkingFeeStrategy):
     def calculate_fee(self, vehicleType: str, duration: int, durationType: DurationTypes) -> float:
        vehicleType=vehicleType.lower()
        if vehicleType=="car":
            return duration*20.0 if durationType==durationType.HOURS else duration*20.0*24
        elif vehicleType=="bike":
            return duration*8.0 if durationType==durationType.HOURS else duration*8.0*24
        #now the next is for auto
        elif vehicleType=="auto":
            return duration*12.0 if durationType==durationType.names.HOURS else duration*12.0*24
        else:
            return duration*25.0 if durationType==durationType.HOURS else duration*25.0*24
    
    #here this is the logic for premium fee strategy while the parking of vehicles