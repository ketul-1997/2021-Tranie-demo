from odoo import models, fields

class vehicles(models.Model):
    _name="vehicles"

    # _rec_name = 'model'

    category = fields.Many2one('category', string="Category", required=True)
    company = fields.Many2one('company', string="Company", required=True)
    name = fields.Char(string="Name", required=True)
    model = fields.Char(string="Model", required=True)
    

