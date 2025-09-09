from ParkingLot.CarParkingSpot import CarParkingSpot
from ParkingLot.BikeParkingSpot import BikeParkingSpot
from ParkingLot.AutoParkingSpot import AutoParkingSpot
from ParkingLot.OtherVehicleParkingSpot import OtherVehicleParkingSpot
from ParkingLot.ParkingLot import ParkingLot
from ParkingLot.BasicHourlyStrategy import BasicHourlyStrategy
from ParkingLot.PremiumStrategy import PremiumStrategy
from ParkingLot.VehicleFactory import VehicleFactory
from ParkingLot.enums.DurationTypes import DurationTypes
from ParkingLot.CreditCard import CreditCard 
from ParkingLot.Cash import Cash


#this is the main function where we will perform all  the operatiosn 
#here we need to create a helper function to get the paymentstrategy
def getPaymentStrategy(paymentmethod,fee):
    if(paymentmethod==1):
        return CreditCard()
    elif(paymentmethod==2):
        return Cash()
    else:
        print("Invalid choice,Default to Creditcard")
        return CreditCard()
    

    
if __name__=="__main__":
    #lets first define the list of parkingSpots
    parkingspots=[
        CarParkingSpot(1,"car"),
        CarParkingSpot(2,"car"),
        BikeParkingSpot(3,"bike"),
        AutoParkingSpot(4,"auto"),
        OtherVehicleParkingSpot(5,"others")
            
    ]
    #lets first initialize theparking lot
    parkinglot=ParkingLot(parkingspots)
    #now do for the fee strategies
    hourlyStrategy=BasicHourlyStrategy()
    premiumStrategy=PremiumStrategy()
    
    #create vehicles using FactoryPattern
    car1=VehicleFactory.create_vehicle("CAR123","car",hourlyStrategy)
    car2=VehicleFactory.create_vehicle("CAR456","car",premiumStrategy)
    bike1=VehicleFactory.create_vehicle("BIKE789","bike",hourlyStrategy)
    
    #park vehicles
    carspot=parkinglot.parkVehicle(car1)
    bikespot=parkinglot.parkVehicle(bike1)
    
    #now the next is to choose the payment methods creditcard,cash
    print("Select the payment method for your vehicle")
    print("1. Credit Card")
    print("2. Cash")
    paymentmethod = int(input("Enter choice: ")) #here asking for input of payment
    print(f"[DEBUG] You selected payment method {paymentmethod}")
    
    if carspot:
        carfee=car1.calculate_fee(2,DurationTypes.HOURS)
        carstrategy=getPaymentStrategy(paymentmethod,carfee)
        carstrategy.processPayment(carfee)
        #atlast vacate the parkingspot
        parkinglot.vacateSpot(carspot,car1)
        print(f"Vehicle {car1._licensePlate} has left spot {carspot._spotNumber}. Spot is now free.")
    if bikespot:
        bikefee=bike1.calculate_fee(2,DurationTypes.HOURS)
        bikestrategy=getPaymentStrategy(paymentmethod,bikefee)
        bikestrategy.processPayment(bikefee)
        parkinglot.vacateSpot(bikespot,bike1)
        print(f"Vehicle {bike1._licensePlate} has left spot {bikespot._spotNumber}. Spot is now free.")
        
    print("\n---- Parking Lot Simulation Ended ----")
        
    
    