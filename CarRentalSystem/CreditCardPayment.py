
from CarRentalSystem.PaymentStrategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def __init__(self,cardnumber,name,expirydate):
        self.cardnumber=cardnumber
        self.name=name 
        self.expirydate=expirydate
    
    #now create a helper function to perform the mask
    def mask_card_number(self,cardnumber):
        if len(cardnumber) <= 4:
            return "*" * len(cardnumber)
        return "*" * (len(cardnumber) - 4) + cardnumber[-4:]
    
    def processPayment(self,amount):
        print(f"Processing credit card payment of ${amount}")
        print(f"Card Number: {self.mask_card_number(self.cardnumber)}")
        print(f"Name on Card: {self.name}")
        print(f"Expiry Date: {self.expirydate}")
    
    #so here we have written all the implementation of the credit card payment strategy

        