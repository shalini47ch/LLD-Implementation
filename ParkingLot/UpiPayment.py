#here also we will inherit it from the PaymentStrategy abstract class 

from ParkingLot.PaymentStrategy import PaymentStrategy

class UpiPayment(PaymentStrategy):
    #here we will pay by using the upi method 
    def processPayment(self, amount: float):
        print(f"Processing UPI payment of $" +{amount})
