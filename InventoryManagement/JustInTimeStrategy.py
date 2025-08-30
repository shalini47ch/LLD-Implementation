
from InventoryManagement.ReplenishmentStrategy import ReplenishmentStrategy
from InventoryManagement.Product import Product

#this is one of the strategy for replenishment
class JustInTimeStrategy(ReplenishmentStrategy):
    def replenish(self,product:Product):
        if(product.getQuantity()<product.getThreshold()):
            #this is the difference that can be added to equalize it to the threshold
            orderquantity=product.getThreshold()-product.getQuantity()
            print(f"Replenishing{product.getName()} with quantity {orderquantity} using JustInTimeStrategy")
            #updating the quantity of the product
            product.setQuantity(product.getQuantity()+orderquantity)
        else:
            print("No need to replenish the stock")

