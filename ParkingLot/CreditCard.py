from ParkingLot.PaymentStrategy import PaymentStrategy

class CreditCard(PaymentStrategy):
    def processPayment(self, amount: float):
        print(f"Processing credit card payment of $ {amount}")
    


