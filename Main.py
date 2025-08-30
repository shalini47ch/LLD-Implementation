from InventoryManagement.InventoryManager import InventoryManager
from InventoryManagement.Warehouse import Warehouse
from InventoryManagement.ProductFactory import ProductFactory
from InventoryManagement.enums.ProductCategories import ProductCategories
from InventoryManagement.JustInTimeStrategy import JustInTimeStrategy
from InventoryManagement.BulkStrategy import BulkStrategy
if __name__ == "__main__":
    inventory_manager = InventoryManager.getInstance()
    #lets first create warehouses and add warehouses
    warehouse1 = Warehouse("W1", "Main Warehouse", "123 Main St")
    warehouse2 = Warehouse("W2", "Secondary Warehouse", "456 Side St")
    
    #similarly use product Factory to create productd
    productfactory=ProductFactory()
    laptop=productfactory.create_product(category=ProductCategories.ELECTRONICS,stockId="E1001",name="Laptop",price=1000.0,quantity=50,threshold=10)
    tshirt=productfactory.create_product(category=ProductCategories.CLOTHING,stockId="C1001",name="T-Shirt",price=20.0,quantity=100,threshold=20)
  
    inventory_manager.add_warehouse(warehouse1)
    inventory_manager.add_warehouse(warehouse2)
    #now the next step is to add products to the warehouse
    warehouse1.add_product(laptop,30)
    warehouse2.add_product(tshirt,80)
    #now we need to set the replenishment strategies
    inventory_manager.set_replenishment_strategies([JustInTimeStrategy()])
    inventory_manager.check_and_replenish("E1001")
    inventory_manager.perform_inventory_check()
    
 
    