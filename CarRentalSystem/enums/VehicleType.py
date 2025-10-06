#it will have different types of vehicles like economy, luxury, SUV,sedan
from enum import Enum

class VehicleType(Enum):
    ECONOMY="Economy",
    LUXURY="Luxury",
    SUV="SUV",
    SEDAN="Sedan",
    #add these to support more different types of vehicles 
    BIKE="Bike",
    AUTO="Auto"