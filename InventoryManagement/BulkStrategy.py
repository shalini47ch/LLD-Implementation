
from InventoryManagement.ReplenishmentStrategy import ReplenishmentStrategy
from InventoryManagement.Product import Product

class BulkStrategy(ReplenishmentStrategy):
    def __init__(self,bulk_quantity:int):
        self._bulk_quantity=bulk_quantity
    
    def replenish(self,product:Product):
        if(product.getQuantity()<product.getThreshold()):
            print(f"Replenishing {product.getName()} with quantity {self._bulk_quantity} using BulkStrategy")
            #updating the quantity of the product
            product.setQuantity(product.getQuantity()+self._bulk_quantity)
        else:
            print("No need to replenish the stock")
        
    