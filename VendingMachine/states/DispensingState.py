
from VendingMachine.states.VendingMachineState import VendingMachineState
class DispensingState(VendingMachineState):
    def __init__(self):
        print("Currently Vending Machine is in Dispensing State")
    
    def click_on_insert_coin(self, machine):
        raise Exception("You cannot insert coin at this state")
     #here create a method of product selection button
    def click_on_product_selection_button(self,machine,code):
        raise Exception("You cannot select product at Dispense State")
    #
    def insert_coin(self,machine,coin):
        raise Exception("You cannot insert coin at this state")
    
    def choose_product(self, machine, code):
        raise Exception("You cannot choose product at this state")
    
    def get_change(self, returned_amount):
        raise Exception("You cannot get change at this state")
    
    def dispense_product(self, machine, code):
        item=machine.get_inventory().get_item_shelf(code)
        machine.get_inventory().update_item_shelf(code)
        print(f"Dispensed item {item.get_name()}")
        machine.set_vending_machine_state(machine.getidle())
        print("Vending Machine State changed to Idle State")
        
    def refund_full_money(self):
        raise Exception("Cannot refund money while dispensing.")

    def update_inventory(self):
        print("Inventory updated after dispensing product.")