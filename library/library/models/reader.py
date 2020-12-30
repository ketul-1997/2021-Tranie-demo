from odoo import api,fields, models

class Reader(models.Model):
    _name = 'reader'
    name = fields.Char("Name")
    bookreader_id = fields.Char(string="Reader ID", readonly=True, required=True, copy=False, default='New') 
    phone_no = fields.Char("Phone No")
    address = fields.Char("Address")
    requestbook = fields.One2many('bookrequest','requestby' , string="BookRequest")

    @api.model
    def create(self, vals):
        if vals.get('bookreader_id', 'New') == 'New':
            vals['bookreader_id'] = self.env['ir.sequence'].next_by_code('reader') or 'New'
        result = super(Reader, self).create(vals)
        return result