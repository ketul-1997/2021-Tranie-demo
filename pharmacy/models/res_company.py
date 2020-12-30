from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    stock_id = fields.Many2one('stock.inventory', string="Stock")
