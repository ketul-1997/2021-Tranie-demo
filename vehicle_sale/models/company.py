from odoo import fields, models

class company(models.Model):
    _name = "company"

    # category = fields.Many2one('category', string='Category', required=True)
    name= fields.Char(string="Company", required=True)
    category = fields.Many2one('category', string='Category', required=True)