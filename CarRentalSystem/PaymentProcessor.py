
#payment processor decides which strategy needs to be followed here 
class PaymentProcessor:
    def processPayment(self,amount,paymentStrategy):
        paymentStrategy.processPayment(amount)
        return True 
    
    #so here it displays whether the payment is processed correctly or not
    
    
