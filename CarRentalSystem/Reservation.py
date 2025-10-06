from CarRentalSystem.enums.ReservationStatus import ReservationStatus 
from CarRentalSystem.enums.VehicleStatus import VehicleStatus
from CarRentalSystem.Vehicle import Vehicle


class Reservation:
    def __init__(self,reservationId,user,vehicle:Vehicle,pickupstore,returnstore,startdate,enddate):
        self.id=reservationId
        self.user=user
        self.vehicle=vehicle
        self.pickupstore=pickupstore
        self.returnstore=returnstore
        self.startdate=startdate
        self.enddate=enddate 
        self.status=ReservationStatus.PENDING
        
        #calculate the totaldays and totalamount
        diff=(self.enddate-self.startdate).days+1
        self.totalamount=vehicle.calculateRentalPrice(diff)
    
    #now create a helper function to confirm reservwtion
    def confirm_reservation(self):
        if(self.status==ReservationStatus.PENDING):
            self.status=ReservationStatus.CONFIRMED
            self.vehicle.set_status(VehicleStatus.RESERVED)
    
    #now the next is to startRental then complete rental
    def start_rental(self):
        if(self.status==ReservationStatus.CONFIRMED):
            self.status=ReservationStatus.INPROGRESS
            self.vehicle.set_status(VehicleStatus.RENTED)

    def complete_rental(self):
        if(self.status==ReservationStatus.INPROGRESS):
            self.status=ReservationStatus.COMPLETED
            self.vehicle.set_status(VehicleStatus.AVAILABLE)
    
    #create one more helper to support cancel reservation
    def cancel_reservation(self):
        if self.status in [ReservationStatus.PENDING,ReservationStatus.COMPLETED]:
            self.status=ReservationStatus.CANCELLED
            self.vehicle.set_status(VehicleStatus.AVAILABLE)

    def get_id(self):
        return self.id

    def get_total_amount(self):
        return self.totalamount
    
    
    
        
    
        
        
    
        