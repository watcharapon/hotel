from netforce.model import Model, fields

class HotelLine(Model):
    _name = "hotel.line"
    _string = "Hotel"
    _name_field = "bed"
    _fields ={
        "hotel_id" : fields.Many2One("hotel","Hotel ID", required=True, search=True),
        "room_number" : fields.Many2One("roomnumber","Room No."),
        "bed": fields.Selection([["double", "Double"], ["single", "Single"]], "Bed", required=True, search=True),
        "bedroom": fields.Selection([["singlebeddedRoom", "Single bedded room"], ["twinbeddedroom", "Twin Bedded Room"], ["doublebeddedroom", "Double Bedded Room"]], "Bedroom", required=True, search=True),
        "breakfast": fields.Selection([["havebreakfast", "Have brekfast"], ["nobrekfast", "No brekfast"]], "Breakfast", required=True),
        "price" : fields.Decimal("Prive", required=True, search=True),
        #"location" : fields.Text("Location", search=True),
        #"status_room": fields.Selection([["emptyroom", "Empty room"], ["romnotbusy", "Room not busy"]], "status room", required=True, search=True),
        }

    _order = "room_number"

HotelLine.register()
