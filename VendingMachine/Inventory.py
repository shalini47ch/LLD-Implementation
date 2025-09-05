import threading as Threading

class Inventory:
    def __init__(self):
        self.item_shelfs=[]
        self.lock=Threading.Lock()
    
    def get_item_shelfs(self):
        return self.item_shelfs
    
    def set_item_shelfs(self,item_shelfs):
        self.item_shelfs=item_shelfs
        
    #now create a method to add itemshelf to itemshelves
    def add_item_shelf(self,item_shelf):
        with self.lock:
            self.item_shelfs.append(item_shelf)
    #create two more helper functions to getitem and updatesoldout item
    
    def get_item(self,code):
        for item_shelf in self.item_shelfs:
            if item_shelf.get_code()==code:
                return item_shelf
        return None

    def update_sold_out_item(self, code):
        with self.lock:
            item=self.get_item(code)
            if item:
                item.set_sold_out()
    