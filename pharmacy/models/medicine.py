from odoo import fields, models, api


class Medicine(models.Model):
    _name = 'pharmacy.medicine'

    name = fields.Char(string="Name")
    price = fields.Integer(string="Price")
    manufacture_date = fields.Date(string="Manufactured Date")
    stock = fields.Integer(string="Stock")
    stock_id = fields.Many2one('stock.inventory', string="Stock ID")
    user_id = fields.Many2one('res.users', string="User ID")
    customer_name = fields.Char(string="Customer Name")
