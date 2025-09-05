       
from VendingMachine.states.Idle import Idle
from VendingMachine.states.HasMoney import HasMoney
from VendingMachine.states.Selected import Selected
from VendingMachine.states.DispensingState import DispensingState
from VendingMachine.Inventory import Inventory
from VendingMachine.CreditCardPayment import CreditCardPayment
from VendingMachine.Shelf import ItemShelf
from VendingMachine.Item import Item
from VendingMachine.enums.ItemType import ItemType

class VendingMachine:
    def __init__(self):
        self.vending_machine_state = HasMoney() # start in Idle
        self.inventory = Inventory()
        self.coinslists = []
        self.payment_strategy = CreditCardPayment()

        self.idle = Idle()
        self.hasmoney = HasMoney()
        self.selected = Selected()
        self.dispensing = DispensingState()
        
        self.inventory.add_item_shelf(ItemShelf(ItemType.COKE.value, Item("Coke", 25)))
        self.inventory.add_item_shelf(ItemShelf(ItemType.PEPSI.value, Item("Pepsi", 35)))
        self.inventory.add_item_shelf(ItemShelf(ItemType.SODA.value, Item("Soda", 20)))
        self.inventory.add_item_shelf(ItemShelf(ItemType.JUICE.value, Item("Juice", 40)))
        self.inventory.add_item_shelf(ItemShelf(ItemType.LAYS.value, Item("Lays", 15)))
        self.inventory.add_item_shelf(ItemShelf(ItemType.KURKURE.value, Item("Kurkure", 20)))
   

  
    def get_vending_machine_state(self):
        return self.vending_machine_state

    def set_vending_machine_state(self, state):
        self.vending_machine_state = state

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

    def get_coinslists(self):
        return self.coinslists

    def set_coinslists(self, coinslists):
        self.coinslists = coinslists

    def get_payment_strategy(self):
        return self.payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def getidle(self):
        return self.idle

    def gethasmoney(self):
        return self.hasmoney

    def getselected(self):
        return self.selected

    def getdispensing(self):
        return self.dispensing
    def refund_full_money(self):
        total = sum(self.coinslists)
        self.coinslists = []  # reset coins
        print(f"Refunded full money: {total}")
        return total

    # ----------------------
    # Delegate methods to current state
    # ----------------------
    def click_on_insert_coin(self):
        self.vending_machine_state.click_on_insert_coin(self)

    def click_on_product_selection_button(self, code):
        self.vending_machine_state.click_on_product_selection_button(self, code)

    def insert_coin(self, coin):
        self.vending_machine_state.insert_coin(self, coin)

    def choose_product(self, code):
        self.vending_machine_state.choose_product(self, code)

    def get_change(self, amount):
        self.vending_machine_state.get_change(amount)

    def dispense_product(self, code):
        return self.vending_machine_state.dispense_product(self, code)

