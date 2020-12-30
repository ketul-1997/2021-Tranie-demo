from odoo import models, fields

class FuelTypes(models.Model):
    _name = 'fueltype'

    name = fields.Char(string='Fuel', required=True)