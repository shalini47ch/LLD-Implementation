#here we will write the logic for debitcard payment 

from VendingMachine.PaymentStrategy import PaymentStrategy
import time

class DebitCardPayment(PaymentStrategy):
    def paymentwithintention(self, amount):
        print(f"Payment of {amount} made using Debit Card")
        #this is the processing time 
        time.sleep(1)
        print("Payment successful by Debit Card")
