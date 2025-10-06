#lets first import the ReservationSystem here
from CarRentalSystem.RentalSystem import RentalSystem
from CarRentalSystem.RentalStore import RentalStore
from CarRentalSystem.Location import Location
from CarRentalSystem.VehicleFactory import VehicleFactory
#now importing the vehicletypes and the vehiclestatus 
from CarRentalSystem.enums.VehicleType import VehicleType
from CarRentalSystem.enums.VehicleStatus import VehicleStatus
from CarRentalSystem.User import User
from datetime import date 
from CarRentalSystem.CreditCardPayment import CreditCardPayment
from CarRentalSystem.CashPayment import CashPayment
from CarRentalSystem.UpiPayment import UpiPayment


def main():
    #lets first create a single instance of rental system  so basically singleton pattern is used
    rental_system=RentalSystem.get_instance()
    
    #now the next step is to create stores
    store1=RentalStore(1,"Downtown Store",Location("123 Main St","CityA","StateA","12345"))
    store2=RentalStore(2,"Airport Store",Location("456 Airport Rd","CityB","StateB","67890"))
    store3=RentalStore(3,"Suburban Store",Location("789 Suburb Ln","CityC","StateC","11223"))
    
    #now add these stores to the rental system
    rental_system.add_store(store1)
    rental_system.add_store(store2) 
    rental_system.add_store(store3)
    
    #now we will create the vehicles using the factory pattern
    economy_vehicle=VehicleFactory.create_vehicle(VehicleType.ECONOMY,"ABC123","Toyota Yaris",2020,"Petrol",VehicleStatus.AVAILABLE,30)
    premium_vehicle=VehicleFactory.create_vehicle(VehicleType.SEDAN,"DEF456","BMW 5 Series",2021,"Diesel",VehicleStatus.AVAILABLE,50)
    luxury_vehicle=VehicleFactory.create_vehicle(VehicleType.LUXURY,"GHI789","Mercedes S-Class",2022,"Electric",VehicleStatus.AVAILABLE,100)
    
    #once these vehicles are added we will add them to the stores
    store1.addVehicle(economy_vehicle)
    store2.addVehicle(premium_vehicle)
    store3.addVehicle(luxury_vehicle)
    
    #lets create the users and then register them to the rental system
    user1=User(1,"Alice","alice@gmail.com","9876567891")
    user2=User(2,"Bob","bob@gmail.com","1234567890")

    rental_system.register_user(user1)
    rental_system.register_user(user2)

    # Create reservations
    reservation1 = rental_system.create_reservation(
        user1.get_user_id(),
        economy_vehicle.get_registration_number(),
        store1.getId(),
        store1.getId(),
        date(2025, 5, 1),
        date(2025, 6, 15)
    )

    # Process payment using different strategies (Strategy Pattern)
    print(f"\nProcessing payment for reservation #{reservation1.get_id()}")
    print(f"Total amount: ${reservation1.get_total_amount()}")
    print("Select payment method:")
    print("1. Credit Card")
    print("2. Cash")
    print("3. UPI")

    choice = 1  # Default to credit card for this example
    if choice == 1:
        payment_strategy = CreditCardPayment("5434567898765432", "Hanna", "123")
    elif choice == 2:
        payment_strategy = CashPayment()
    elif choice == 3:
        payment_strategy = UpiPayment("user@upi")
    else:
        print("Invalid choice! Defaulting to credit card payment.")
        payment_strategy = CreditCardPayment()

    payment_success = rental_system.process_payment(reservation1.get_id(), payment_strategy)
    if payment_success:
        print("Payment successful!")

        # Start the rental
        rental_system.start_rental(reservation1.get_id())

        # Simulate rental period
        print("\nSimulating rental period...")

        # Complete the rental
        rental_system.complete_rental(reservation1.get_id())
        print("Rental completed.")
    else:
        print("Payment failed!")

if __name__ == "__main__":
    main()