from netforce.model import Model, fields
#from datetime import *
#import time

class Hotel(Model):
    _name = "hotel"
    _string = "Hotel"
    _name_field = "hotel"
    _fields ={
        "hotel" : fields.Char("Hotel", required=True, search=True),
        "lines" : fields.One2Many("hotel.line","hotel_id","Lines"),
        #"no_guest" : fields.Integer("No. of Guest", required=True, search=True),
        #"room_number" : fields.Integer("Room number", required=True, search=True),
        #"price" : fields.Decimal("Pribe", required=True, search=True),
        #"check_in" : fields.DateTime("Checkin-in", required=False),
        #"check_out" : fields.DateTime("Checkin-out"),
        #"bedroom": fields.Selection([["singlebeddedRoom", "Single bedded room"], ["twinbeddedroom", "Twin Bedded Room"], ["doublebeddedroom", "Double Bedded Room"]], "Bedroom", required=True, search=True),
        #"breakfast": fields.Selection([["havebreakfast", "Have brekfast"], ["nobrekfast", "No brekfast"]], "Breakfast", required=True),
        #"location" : fields.Text("Location", search=True),
        #"status_room": fields.Selection([["emptyroom", "Empty room"], ["romnotbusy", "Room not busy"]], "status room", required=True, search=True),
        }

Hotel.register()

