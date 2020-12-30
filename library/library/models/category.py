from odoo import api,fields, models

class Category(models.Model):
    _name = "category"
    name = fields.Char("Name")
    
