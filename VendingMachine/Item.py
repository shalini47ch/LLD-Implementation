from VendingMachine.enums.ItemType import ItemType

class Item:
    def __init__(self, item_type: ItemType, price: int):
        self.item_type = item_type
        self.price = price
    
    def get_item_type(self) -> ItemType:
        return self.item_type
    
    def get_price(self) -> int:
        return self.price
    
    def set_price(self, price: int):
        self.price = price
    
    
    
    def __repr__(self):
        return f"Item(type={self.item_type}, price={self.price})"

