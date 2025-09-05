from VendingMachine.states.VendingMachineState import VendingMachineState
from VendingMachine.Shelf import ItemShelf

class HasMoney(VendingMachineState):
    def __init__(self):
        print("Currently Vending Machine is in HasMoney State")
    
    def click_on_insert_coin(self, machine):
        #that button is already pressed before
        return

    def click_on_product_selection_button(self, machine, code):
        machine.set_vending_machine_state(machine.getselected())
        print("Vending Machine State changed to ProductSelection State")
        
       
    def insert_coin(self, machine, coin):
        machine.get_coinslists().append(coin)
        print(f"Inserted coin of value {coin.get_value()}")
        
    
    def choose_product(self, machine, code):
        raise Exception("You need to click on product selection button")
       
    
    def get_change(self, returned_amount):
        return returned_amount
        
        
    
    def dispense_product(self, machine, code):
        raise Exception("You need to click on product selection button")
        
    
    def refund_full_money(self, machine):
        machine.set_vending_machine_state(machine.getidle())
        return machine.get_coinslists()
      
    
    def update_inventory(self, machine, item, code):
        machine.get_inventory().add_item_shelf(ItemShelf(code, item))
       
    

    