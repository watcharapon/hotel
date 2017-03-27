from netforce.model import Model, fields, get_model
import time

class Hotelticket(Model):
    _name = "hotel.ticket"
    _string = "Hotel Ticket"
    _fields ={
        "date_from" : fields.Date("Date From"),
        "date_to" : fields.Date("Date To"),
        "hotel_id" : fields.Many2One("hotel","Hotel ID", required=True, search=True),
        "room_number" : fields.Many2One("roomnumber","Room No."),
        "price" : fields.Decimal("Pribe", required=True, search=True),
        "bed": fields.Selection([["double", "Double"], ["single", "Single"]], "Bed", required=True, search=True),
        "date_from" : fields.Date("Date From"),
        "hotel_ids": fields.Char("Hotel IDS"),
        "state": fields.Selection([["draft","Draft"],
                                   ["confirm","Confirmed"]], "Status", required=True),
        "contact_id": fields.Many2One("contact","Contact",required=True),
        }

    _defaults = {
        "state":"draft",
        "date_from": lambda *a: time.strftime("%Y-%m-%d"),
    }

    def update_date(self,context={}):
        data = context['data']
        hotel_ids = get_model("hotel").search([]) or None
        if data.get('date_from') and data.get('date_to'):
            for ticket in self.search_browse([["date_from","<=",data['date_from']],["state","!=","draft"]]):
                if ticket.date_to <= data["date_from"]: continue
                if ticket.hotel_id.id in hotel_ids:
                    hotel_ids.remove(ticket.hotel_id.id)
            for ticket in self.search_browse([["date_from",">",data['date_from']],["state","!=","draft"]]):
                if data["date_to"] <= ticket.date_from: continue
                if ticket.hotel_id.id in hotel_ids:
                    hotel_ids.remove(ticket.hotel_id.id)
        data["hotel_ids"] = hotel_ids
        return data

    def confirm(self,ids,context={}):
        self.write(ids,{"state":"confirm"})
        return {
            "next" : {
                "tpye": "reload",
            },
        }

    def onchange_hotel(self,context={}):
        data = context['data']
        if data.get("hotel_id"):
            hotel = get_model("hotel").browse(data["hotel_id"])
            if data.get("room_number"):
                for line in hotel.lines:
                    if not line.room_number: continue
                    if line.room_number.id == data["room_number"] and line.bed == data["bed"]:
                        data["price"] = line.price or 0
        return data

Hotelticket.register()
