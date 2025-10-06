from CarRentalSystem.PaymentStrategy import PaymentStrategy

#here we will write the implementation of the UPI Payment
class UpiPayment(PaymentStrategy):
    def __init__(self,upiid):
        self.upiid=upiid
    
    #now create a helper function to write about the process payment method 
    def processPayment(self, amount):
        print("Payment done by upiId of ${self.upiid} and has an amount of ${amount}")
    
    

    
