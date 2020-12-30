from odoo import api,fields, models

class Stock(models.Model):
    _name = "stock"
    name = fields.Char("Name")
    quantity = fields.Integer("Quantity")
    state = fields.Selection([
            ('concept', 'Concept'),
            ('started', 'Started'),
            ('progress', 'In progress'),
            ('finished', 'Done'),
            ],default='concept')