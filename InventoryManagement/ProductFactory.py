#here we will use the factory design pattern to create products based on category
from InventoryManagement.enums.ProductCategories import ProductCategories
from InventoryManagement.GroceryProduct import GroceryProduct   
from InventoryManagement.ElectronicsProduct import ElectronicsProduct
from InventoryManagement.ClothingProduct import ClothingProduct

class ProductFactory:
    def create_product(self,category:ProductCategories,stockId:str,name:str,price:float,quantity:int,threshold:int):
        if category==ProductCategories.GROCERY:
            return GroceryProduct(stockId,name,price,quantity,threshold,category=ProductCategories.GROCERY)
        elif category==ProductCategories.ELECTRONICS:
            return ElectronicsProduct(stockId,name,price,quantity,threshold,category=ProductCategories.ELECTRONICS)
        elif category==ProductCategories.CLOTHING:
            return ClothingProduct(stockId,name,price,quantity,threshold,category=ProductCategories.CLOTHING)
        else:
            raise ValueError("Invalid product category")
        
        #here the factory pattern is implemented 
    