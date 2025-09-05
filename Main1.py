from VendingMachine.VendingMachine import VendingMachine
from VendingMachine.enums.Coins import Coins
from VendingMachine.enums.ItemType import ItemType

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.click_on_insert_coin()
    vending_machine.click_on_product_selection_button(ItemType.PEPSI.value)
    # vending_machine.insert_coin(Coins.FIVE)
    vending_machine.choose_product(ItemType.PEPSI.value)
    item = vending_machine.dispense_product(ItemType.PEPSI.value)
    print(f"Dispensed Item is {item}")
    vending_machine.set_coinslists([])

    
    