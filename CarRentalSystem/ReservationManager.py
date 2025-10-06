from CarRentalSystem.Reservation import Reservation

class ReservationManager:
    def __init__(self):
        self.hmap={} #here it will have all the reservations
        self.nextreservationid=1
        
    def create_reservation(self,user,vehicle,pickupstore,returnstore,startdate,enddate):
        reservation=Reservation(self.nextreservationid,user,vehicle,pickupstore,returnstore,startdate,enddate)
        #update the given hmap
        self.hmap[reservation.get_id()]=reservation
        #now update the next reservationid
        self.nextreservationid+=1
        
        if hasattr(user,"add_reservation"):
            user.add_reservation(reservation)
        return reservation
    
    #lets firstcreate a helper function to confirm the reservation
    def confirm_reservation(self,reservationid):
        reservation=self.hmap.get(reservationid)
        #if reservation exists then confirm reservation
        if reservation:
            reservation.confirm_reservation()
            
    def start_rental(self,reservationid):
        reservation=self.hmap.get(reservationid)
        if reservation:
            reservation.start_rental()
    
    def complete_rental(self,reservationid):
        reservation=self.hmap.get(reservationid)
        if reservation:
            reservation.complete_rental()
    
    def cancel_reservation(self,reservationid):
        reservation=self.hmap.get(reservationid)
        if reservation:
            reservation.cancel_reservation()
    
    def get_reservation(self,reservationid):
        return self.hmap.get(reservationid)

    
    

    