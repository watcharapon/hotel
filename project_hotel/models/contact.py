from netforce.model import Model, fields

class Contact(Model):
    _inherit = "contact"
    _fields = {
        "code" : fields.Char("Id card", required=True),
        "itile": fields.Selection([["mr", "Mr."], ["miss", "Miss."], ["mrs", "Mrs."], ["ms", "Ms."], ["dr", "Dr."]], "itile", required=True),
    }

    def name_get(self, ids, context={}):
        vals = []
        for obj in self.browse(ids):
            if obj.itile:
                name = "[%s] %s" % (obj.itile, obj.name)
            else:
                name = obj.name
            vals.append((obj.id, name))
        return vals

Contact.register()
