from odoo import fields, models, api


class InventoryStockPurchaseLine(models.Model):
    _name = 'pharmacy.inventory.stock.purchase.line'

    customer_id = fields.Many2one('res.partner', string="Customer")
    medicine_id = fields.Many2one('pharmacy.medicine', string="Medicine")
    stock_purchase = fields.Integer(string="Stock Purchased")
    stock_id = fields.Many2one('stock.inventory', string="Stock ID")
