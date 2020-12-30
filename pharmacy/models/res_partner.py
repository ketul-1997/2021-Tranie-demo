from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    inventory_stock_purchase_id = fields.Many2one('pharmacy.inventory.stock.purchase.line', string="Stocks")
