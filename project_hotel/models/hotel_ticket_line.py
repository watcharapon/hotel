from netforce.model import Model, fields


class HotelTicketLine(Model):
    _name="hotel.ticket.line"
    _fields={
        'ticket_id': fields.Many2One("hotel.ticket","Hotel Ticket",required=True,on_delete="cascade"),
        'product_id': fields.Many2One("product","Product"),
        'qty': fields.Decimal("Qty"),
        'unit_price': fields.Decimal("Unit Price"),
        'amount': fields.Decimal("Amount"),
    }

HotelTicketLine.register()
