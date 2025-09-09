from ParkingLot.PaymentStrategy import PaymentStrategy

class Cash(PaymentStrategy):
    #here we will pay by using the cash method 
    def processPayment(self, amount: float):
        print(f"Processing Cash payment of ${amount}")