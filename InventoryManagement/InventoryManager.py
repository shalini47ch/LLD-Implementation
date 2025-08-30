from threading import Lock
from InventoryManagement.Product import Product
from InventoryManagement.ProductFactory import ProductFactory

class InventoryManager:
    _instance=None 
    _lock=Lock()
    
    def __init__(self):
        #check if the instance already exists
        if InventoryManager._instance is not None:
            raise Exception("This class is a singleton!")
        #now we will declare the other collections 
        self._warehouses=[]
        self._product_factory=ProductFactory()
        self.replenishment_strategies=None 
    
    @classmethod
    def getInstance(cls):
        #since the instance is None we create a new instance
        with cls._lock:
            if cls._instance is None:
                cls._instance=InventoryManager()
        return cls._instance
    
    #create a function to set the replenishment strategies
    def set_replenishment_strategies(self,strategies):
        self.replenishment_strategies=strategies
    #create a function to add an element to a warehouse
    def add_warehouse(self,warehouse):
        self._warehouses.append(warehouse)
    #create a function to remove elements from a warehouse 
    def remove_warehouse(self,warehouse):
        if warehouse in self._warehouses:
            self._warehouses.remove(warehouse)
    #create a function to get a product by a specific stockId 
    def get_product_by_stockId(self,stockId:str):
        for warehouse in self._warehouses:
            product=warehouse.get_product(stockId)
            if product is not None:
                return product
        return None
    #check for the product quantity and perform the replenishment if needed
    def check_and_replenish(self,stockId:str):
        product=self.get_product_by_stockId(stockId)
        if product is not None:
            if product.getQuantity()<=product.getThreshold():
                if self.replenishment_strategies is not None:
                    for strategy in self.replenishment_strategies:
                        strategy.replenish(product)
                else:
                    print("No replenishment strategies set")
        else:
            print("Product not found")
    #perform inventory check
    def perform_inventory_check(self):
        for warehouse in self._warehouses:
            products=warehouse.list_all_products()
            for product in products:
                print(f"Product: {product.getName()}, StockId: {product.getStockId()}, Quantity: {product.getQuantity()}, Threshold: {product.getThreshold()}")

        