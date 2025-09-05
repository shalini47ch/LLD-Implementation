from VendingMachine.PaymentStrategy import PaymentStrategy
import time 

class Cash(PaymentStrategy):
    def paymentwithintention(self, amount):
        print(f"Payment of {amount} made using Cash")
        time.sleep(1) #here the processing time is 1 second
        print("Payment successful by Cash")