from InventoryManagement.enums.ProductCategories import ProductCategories
from InventoryManagement.Product import Product

class GroceryProduct(Product):
        def __init__(self,stockId:str,name:str,price:float,quantity:int,threshold:int,category:ProductCategories):
            super().__init__(stockId,name,price,quantity,threshold,ProductCategories.GROCERY)
            self._expiryDate=None 
            self._refrigerated=False 
        
        #now here putting the respective getters and setters for the new attributes 
        def getExpiryDate(self):
            return self._expiryDate
        
        def setExpiryDate(self,expiryDate):
            self._expiryDate=expiryDate
        
        def isRefrigerated(self):
            return self._refrigerated
        
        def setRefrigerated(self,refrigerated:bool):
            self._refrigerated=refrigerated

