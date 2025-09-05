#create an abstract class to describe the different states of the vending machine 

from abc import ABC, abstractmethod

class VendingMachineState(ABC):
    @abstractmethod
    def click_on_insert_coin(self,machine):
        pass
    
    @abstractmethod
    #here create a method of product selection button
    def click_on_product_selection_button(self,machine,code):
        pass
    #now the next is to insert the coin
    @abstractmethod
    def insert_coin(self,machine,coin):
        pass
    
    @abstractmethod 
    def choose_product(self,machine,code):
        pass 
    
   #we will create 4 more helper methods getchange(),dispenseproduct,refundfullmoney,updateinventory
    def get_change(self,returned_amount):
       pass
    #there arw two more methods one is to dispense the product and another is to refund the full money
    @abstractmethod
    def dispense_product(self,machine,code):
        pass

    @abstractmethod
    def refund_full_money(self,machine):
        pass
    #at last create a helper funtion to update the inventory
    @abstractmethod
    def update_inventory(self,machine,item,code):
        pass