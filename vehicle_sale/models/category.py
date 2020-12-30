from odoo import fields, models

class category(models.Model):
    _name = 'category'

    name = fields.Char(string="Category", required=True)