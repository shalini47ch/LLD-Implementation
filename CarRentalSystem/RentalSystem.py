from datetime import datetime
from typing import List, Dict, Optional
from CarRentalSystem.VehicleFactory import VehicleFactory
from CarRentalSystem.ReservationManager import ReservationManager
from CarRentalSystem.PaymentProcessor import PaymentProcessor
from CarRentalSystem.RentalStore import RentalStore
from CarRentalSystem.User import User
from CarRentalSystem.Reservation import Reservation
from CarRentalSystem.PaymentStrategy import PaymentStrategy
# from CarRentalSystem.Economy import Economy

class RentalSystem:
    #here the singleton design pattern is also applied
    _instance = None

    def __init__(self):
        self.stores= []
        self.vehicle_factory=VehicleFactory()
        self.reservation_manager=ReservationManager()
        self.payment_processor=PaymentProcessor()
        self.users={}
        self.next_user_id=1

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = RentalSystem()
        return cls._instance

    def add_store(self, store: RentalStore):
        self.stores.append(store)

    def get_store(self, store_id: int) -> Optional[RentalStore]:
        for store in self.stores:
            if store.getId() == store_id:
                return store
        return None

    def get_stores(self) -> List[RentalStore]:
        return self.stores

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    def create_reservation(self, user_id: int, vehicle_registration: str,
                           pickup_store_id: int, return_store_id: int,
                           start_date: datetime, end_date: datetime) -> Optional[Reservation]:
        user = self.get_user(user_id)
        pickup_store = self.get_store(pickup_store_id)
        return_store = self.get_store(return_store_id)
        vehicle = pickup_store.get_vehicle(vehicle_registration) if pickup_store else None

        if user and pickup_store and return_store and vehicle:
            return self.reservation_manager.create_reservation(
                user, vehicle, pickup_store, return_store, start_date, end_date
            )
        return None

    def process_payment(self, reservation_id: int, payment_strategy: PaymentStrategy) -> bool:
        reservation = self.reservation_manager.get_reservation(reservation_id)
        if reservation:
            result = self.payment_processor.processPayment(reservation.get_total_amount(), payment_strategy)
            if result:
                self.reservation_manager.confirm_reservation(reservation_id)
                return True
        return False

    def start_rental(self, reservation_id: int):
        self.reservation_manager.start_rental(reservation_id)

    def complete_rental(self, reservation_id: int):
        self.reservation_manager.complete_rental(reservation_id)

    def cancel_reservation(self, reservation_id: int):
        self.reservation_manager.cancel_reservation(reservation_id)

    def register_user(self, user: User):
        user_id = user.get_user_id()
        if user_id in self.users:
            print(f"User with id: {user_id} already exists in the system")
            return
        self.users[user_id] = user
