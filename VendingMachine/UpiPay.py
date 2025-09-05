
#make sure to add the processing time as well for the UPI payment
from VendingMachine.PaymentStrategy import PaymentStrategy
import time

class UpiPay(PaymentStrategy):
    def paymentwithintention(self, amount):
        print(f"Payment of {amount} made using UPI")
        time.sleep(1) #here the processing time is 1 second
        print("Payment successful by UPI")