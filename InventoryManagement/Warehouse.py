
class Warehouse:
    def __init__(self,id:str,name:str,location:str):
        self.id=id
        self.name=name
        self.location=location
        self.products={} #here the key will be stockId:Product
    
    #first lets create a helper function to set the location of that particular product
    def set_location(self,location):
        self.location=location 
    
    def add_product(self,product,quantity:int):
        if product.getStockId() in self.products:
            existing_product=self.products[product.getStockId()]
            existing_quantity=existing_product.getQuantity()
            existing_product.setQuantity(existing_quantity+quantity)
        else:
            product.setQuantity(quantity)
            self.products[product.getStockId()]=product
    
    #similarly we can create a function to remove the product from the warehouse
    def remove_product(self,stockId:str,quantity:int):
        if stockId in self.products:
            existing_product=self.products[stockId]
            existing_quantity=existing_product.getQuantity()
            if existing_quantity>=quantity:
                existing_product.setQuantity(existing_quantity-quantity)
                if existing_product.getQuantity()==0:
                    del self.products[stockId]
            else:
                print("Insufficient quantity to remove")
        else:
            print("Product not found in the warehouse")
    #now the next function to get the prioduct by the stockId
    def get_product(self,stockId:str):
        if stockId in self.products:
            return self.products[stockId]
        else:
            print("Product not found in the warehouse")
            return None
    #function to get all the available quantiyy for the specific stockId
    def get_product_quantity(self,stockId:str):
        if stockId in self.products:
            product=self.products[stockId]
            return product.getQuantity()
        else:
            print("Product not found in the warehouse")
            return 0
    #at last we need to return the list of all the products in the warehouse
    def list_all_products(self):
        return list(self.products.values())

        