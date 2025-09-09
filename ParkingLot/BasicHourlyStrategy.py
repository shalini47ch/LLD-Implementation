from ParkingLot.ParkingFeeStrategy import ParkingFeeStrategy
from ParkingLot.enums.DurationTypes import DurationTypes

class BasicHourlyStrategy(ParkingFeeStrategy):
    #we can have cars,bike,auto and others
    def calculate_fee(self, vehicleType: str, duration: int, durationType: DurationTypes) -> float:
        vehicleType=vehicleType.lower()
        if vehicleType=="car":
            return duration*10.0 if durationType==durationType.HOURS else duration*10.0*24
        elif vehicleType=="bike":
            return duration*5.0 if durationType==durationType.HOURS else duration*5.0*24
        #now the next case is for auto
        elif vehicleType=="auto":
            return duration*8.0 if durationType==durationType.HOURS else duration*8.0*24
        else:
            return duration*15.0 if durationType==durationType.HOURS else duration*15.0*24
        
       