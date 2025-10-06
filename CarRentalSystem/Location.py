class Location:
    def __init__(self, address, city, state, zip_code):
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
    
    #now adding the specific getter and setters 
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state 
    
    def get_zip_code(self):
        return self.zip_code