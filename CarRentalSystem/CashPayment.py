
from CarRentalSystem.PaymentStrategy import PaymentStrategy
#here we will implement the strategy pattern for cash payment
class CashPayment(PaymentStrategy):
    def processPayment(self,amount):
        print(f"Processing cash payment of ${amount}")
    

    