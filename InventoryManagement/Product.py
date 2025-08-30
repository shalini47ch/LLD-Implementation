from abc import ABC, abstractmethod
from InventoryManagement.enums.ProductCategories import ProductCategories

class Product(ABC):
    def __init__(self,stockId:str,name:str,price:float,quantity:int,threshold:int,category:ProductCategories):
        #here all the parameters are private
        self._stockId=stockId
        self._name=name 
        self._price=price
        self._quantity=quantity
        self._threshold=threshold
        self._category=category
    
    def getStockId(self)->str:
        return self._stockId
    
    def getName(self)->str:
        return self._name
    
    def getPrice(self)->float:
        return self._price
    
    def getQuantity(self)->int:
        return self._quantity
    
    def getThreshold(self)->int:
        return self._threshold
    
    def getCategory(self)->ProductCategories:
        return self._category
    
    def setPrice(self,price:float):
        self._price=price
        
    def setQuantity(self,quantity:int):
        self._quantity=quantity
        
    def setThreshold(self,threshold:int):
        self._threshold=threshold
        
    def setCategory(self,category:ProductCategories):
        self._category=category
    
         