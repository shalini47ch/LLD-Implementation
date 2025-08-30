from InventoryManagement.enums.ProductCategories import ProductCategories
from InventoryManagement.Product import Product

class ElectronicsProduct(Product):
    def __init__(self,stockId:str,name:str,price:float,quantity:int,threshold:int,category:ProductCategories):
        super().__init__(stockId,name,price,quantity,threshold,ProductCategories.ELECTRONICS)
        self._warrantyPeriod=None 
        self._brand=None
    
    def get_brand(self):
        return self._brand
    
    def set_brand(self,brand:str):
        self._brand=brand
    
    #similarly write the getters and setters for warrantyPeriod
    def get_warrantyPeriod(self): 
        return self._warrantyPeriod
    
    def set_warrantyPeriod(self,warrantyPeriod:int):
        self._warrantyPeriod=warrantyPeriod