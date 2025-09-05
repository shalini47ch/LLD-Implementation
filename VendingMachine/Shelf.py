from VendingMachine.Item import Item

class ItemShelf:
    def __init__(self,code:str,product:Item=None,is_available=True):
        self.code=code
        self.product=product
        self.is_available=is_available
    
    def get_code(self)->str:
        return self.code
    
    def get_product(self)->Item:
        return self.product
    
    def set_product(self,product:Item):
        self.product=product
        self.is_available=True
    
    #create a method to check for the availability of the product
    def check_availability(self)->bool:
        return self.is_available
    
    def remove_product(self):
        remove_product=self.product
        self.product=None
        self.is_available=False
        return remove_product
