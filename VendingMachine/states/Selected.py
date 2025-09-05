from VendingMachine.states.VendingMachineState import VendingMachineState
from VendingMachine.Shelf import ItemShelf

class Selected(VendingMachineState):
    def __init__(self):
        print("Currently Vending Machine is in the selected state")
        
    def click_on_insert_coin(self, machine):
        raise Exception("You cannot insert coin in selected state")
    
    def click_on_product_selection_button(self, machine, code):
        #already in selected state
        return
    def insert_coin(self, machine, coin):
        raise Exception("You cannot insert coin in selected state")
    
    def choose_product(self, machine, code):
        shelf = machine.get_inventory().get_item(code)
        if shelf is None or not shelf.check_availability():
            raise Exception("Product not available")
        item = shelf.get_product()
        paidbyuser = sum([coin.get_value() for coin in machine.get_coinslists()])

        if item.get_price() > paidbyuser:
            print("Insufficient balance, please insert more coins")
            machine.refund_full_money() 
            machine.set_vending_machine_state(machine.getidle())
            return

        elif item.get_price() < paidbyuser:
            self.get_change(paidbyuser - item.get_price())

        machine.set_vending_machine_state(machine.getdispensing())
        print("Vending Machine State changed to Dispensing State")

    
    def get_change(self, returned_amount):
        print(f"Returned amount is {returned_amount}")
        return returned_amount
    def dispense_product(self, machine, code):
        return Exception ("You cannot dispense product in selected state")  
    
    def refund_full_money(self, machine):
        print("Returning the full money back to the coin dispenser tray")
        machine.set_vending_machine_state(machine.getidle())
        return machine.get_coinslists()   
    #create one more helper function to update the inventory
    def update_inventory(self, machine, item, code):
        machine.get_inventory().add_item_shelf(ItemShelf(code, item))
        
   