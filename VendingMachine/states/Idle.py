from VendingMachine.states.VendingMachineState import VendingMachineState
from VendingMachine.Shelf import ItemShelf

class Idle(VendingMachineState):
    def __init__(self):
        print("Currently Vending Machine is in Idle State")
    
    def click_on_insert_coin(self, machine):
        machine.set_vending_machine_state(machine.gethasmoney())
        print("Vending Machine State changed to HasMoney State")
    
    def click_on_product_selection_button(self, machine, code):
        #idle state cannot select the product
        raise Exception("You need to click on insert coin button")
    
    def insert_coin(self, machine, coin):
        raise Exception("You cannot insert coin in Idle State")
    
    def choose_product(self, machine, code):
        raise Exception("You cannot choose a product in Idle State")
    
    def get_change(self, returned_amount):
        raise Exception("You cannot get change in Idle State")
    
    def dispense_product(self, machine, code):
        raise Exception("You cannot dispense product in Idle State")
    
    def refund_full_money(self, machine):
        raise Exception("You cannot refund money in Idle State")
    
    def update_inventory(self, machine, item, code):
        machine.get_inventory().add_item_shelf(ItemShelf(code, item))
    

    