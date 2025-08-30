from InventoryManagement.enums.ProductCategories import ProductCategories
from InventoryManagement.Product import Product

class ClothingProduct(Product):
    #all the parameters are private and to access them their 
    def __init__(self,stockId:str,name:str,price:float,quantity:int,threshold:int,category:ProductCategories):
            super().__init__(stockId,name,price,quantity,threshold,ProductCategories.CLOTHING)
            self._size=None 
            self._color=None 
        
    def getSize(self):
        return self._size
    
    def setSize(self,size:str):
        self._size=size
        
    def getColor(self):
        return self._color
    
    def setColor(self,color:str):
        self._color=color
