
from abc import ABC, abstractmethod
from InventoryManagement.Product import Product
#here we will create an abstract class for replenishment strategy and then two other strategies will be implmented using that

class ReplenishmentStrategy(ABC):
    @abstractmethod
    def replenish(self,product:Product):
        pass
  