from ParkingLot.PaymentStrategy import PaymentStrategy

class DebitCard(PaymentStrategy):
    def processPayment(self, amount: float):
        print(f"Processing debit card payment of ${amount}")
    