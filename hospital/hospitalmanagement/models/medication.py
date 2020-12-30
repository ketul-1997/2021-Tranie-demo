from odoo import fields, models, api

class Medication(models.Model):
    _name = 'medication'

    name = fields.Char(string='Medicine Category')
