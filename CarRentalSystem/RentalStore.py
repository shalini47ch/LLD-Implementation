#rental store 

class RentalStore:
    def __init__(self,id,name,location):
        #rental store will have vehicles with registration number followed by vehicle 
        self._id=id
        self._name=name 
        self._location=location
        self._vehicles={} #here the key will be the registration number and the value will be the vehicle
    
    #lets first define the getters and setters 
    def getId(self):
        return self._id
    
    def setId(self,value):
        self._id=value
    
    def getName(self):
        return self._name 
    
    def getLocation(self):
        return self._location
    
    def setName(self,value):
        self._name=value 
    
    def setLocation(self,location):
        self._location=location 
    
    #now create addVehicle 
    #this is same like adding to hmap followed 
    def addVehicle(self,vehicle):
        self._vehicles[vehicle.get_registration_number()]=vehicle 
    
    def removeVehicle(self,registrationNumber):
        if registrationNumber in self._vehicles:
            del self._vehicles[registrationNumber]
            
    def get_vehicle(self, registration_number):
        return self._vehicles.get(registration_number, None)
    
    
    
    
    

        
        