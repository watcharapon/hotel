from pprint import pprint
from netforce.model import Model, fields, get_model
import time

class Hotelticket(Model):
    _name = "hotel.ticket"
    _string = "Hotel Ticket"
    _fields ={
        "check_in" : fields.Date("Check in"),
        "check_out" : fields.Date("Date To"),
        "hotel_id" : fields.Many2One("hotel","Hotel ID", required=True, search=True),
        "room_id" : fields.Many2One("roomnumber","Room No."),
        "price" : fields.Decimal("Pribe", required=True, search=True),
        "bed": fields.Selection([["double", "Double"], ["single", "Single"]], "Bed", required=True, search=True),
        "hotel_ids": fields.Char("Hotel IDS"),
        "state": fields.Selection([["draft","Draft"],
                                   ["confirm","Confirmed"]], "Status", required=True),
        "contact_id": fields.Many2One("contact","Contact",required=True),
        'lines': fields.One2Many("hotel.ticket.line","ticket_id","Lines"),
        }

    _defaults = {
        "state":"draft",
        "check_in": lambda *a: time.strftime("%Y-%m-%d"),
    }

    def get_report_data(self,ids,context={}):
        res=super().get_report_data(ids,context)
        print("xxxxxxxxxxxxxxxxxxxxxx")
        return res

    def get_report_data_custom(self,ids,context={}):
        pages=[]
        for index, obj in enumerate(self.browse(ids)):
            page_vals={
                'number': 'simple_number%s'%(index),
                'lines': [], #each
            }
            for i in range(10):
                page_vals['lines'].append({
                    'qty': i,
                })
            pages.append(page_vals)

        print("="*30)
        pprint(pages)
        print("="*30)
        data={
            'pages': pages,
        }
        return data

    def update_date(self,context={}):
        data = context['data']
        hotel_ids = get_model("hotel").search([]) or None
        if data.get('check_in') and data.get('check_out'):
            for ticket in self.search_browse([["check_in","<=",data['check_in']],["state","!=","draft"]]):
                if ticket.check_out <= data["check_in"]: continue
                if ticket.hotel_id.id in hotel_ids:
                    hotel_ids.remove(ticket.hotel_id.id)
            for ticket in self.search_browse([["check_in",">",data['check_in']],["state","!=","draft"]]):
                if data["check_out"] <= ticket.check_in: continue
                if ticket.hotel_id.id in hotel_ids:
                    hotel_ids.remove(ticket.hotel_id.id)
        data["hotel_ids"] = hotel_ids
        return data

    def confirm(self,ids,context={}):
        self.write(ids,{"state":"confirm"})
        obj = self.browse(ids)[0]
        return {
            "next" : {
                "name": "hotel_ticket",
                "mode": "form",
                "active_id": obj.id,
            },
            "flash": "Confirm",
        }

    def onchange_hotel(self,context={}):
        data = context['data']
        if data.get("hotel_id"):
            hotel = get_model("hotel").browse(data["hotel_id"])
            if data.get("room_id"):
                for line in hotel.lines:
                    if not line.room_number: continue
                    if line.room_number.id == data["room_id"] and line.bed == data["bed"]:
                        data["price"] = line.price or 0
        return data

    def copy(self, ids, context):
        obj = self.browse(ids)[0]
        vals = {
            "contact_id": obj.contact_id.id,
            "check_in": obj.check_in,
            "check_out": obj.check_out,
            "hotel_id": obj.hotel_id.id,
            "bed": obj.bed,
            "price": obj.price,
            "room_id": obj.room_id.id,
        }
        new_id = self.create(vals)
        new_obj = self.browse(new_id)
        return {
            "next": {
                "name": "hotel_ticket",
                "mode": "form",
                "active_id": new_id,
            },
            "flash": "copy success",
        }
Hotelticket.register()
