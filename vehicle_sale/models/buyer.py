from odoo import models, fields

class buyer(models.Model):
    _name = 'buyer'

    name = fields.Char(string='Name', required=True)
    contact_no = fields.Char(string='Contact No', required=True)
    vehicle = fields.Many2one('vehicles',string='Vehicle', required=True)
    date = fields.Date(string='Request Date', default=fields.Date.today)
    