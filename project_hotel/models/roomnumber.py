from netforce.model import Model, fields

class Roomnumber(Model):
    _name = "roomnumber"
    _string = "Room number"
    _name_field = "number"
    _fields = {
        "room_number" : fields.Integer("Room number", required=True, search=True),
        "number" : fields.Char("Number", required=True),
        }

Roomnumber.register()

