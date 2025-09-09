class Payment:
    def __init__(self,amount,paymentStrategy):
        self.amount=amount
        self.paymentStrategy=paymentStrategy

    def processPayment(self):
        if self.amount>0:
            self.paymentStrategy.processPayment(self.amount)
        else:
            print("Invalid amount")
        
