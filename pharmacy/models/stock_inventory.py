from odoo import fields, models, api


class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    medicine_line = fields.One2many('pharmacy.medicine', 'stock_id', string="Medicine")
    user_id = fields.Many2one('res.users', string="User")
    inventory_stock_purchase_id = fields.One2many('pharmacy.inventory.stock.purchase.line', 'stock_id',
                                                  string="Customer Details")
