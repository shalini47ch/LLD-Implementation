from VendingMachine.PaymentStrategy import PaymentStrategy
import time 

class CreditCardPayment(PaymentStrategy):
    def paymentwithintention(self, amount):
        print(f"Payment of {amount} made using Credit Card")
        time.sleep(1)
        print("Payment successful by Credit Card")

