from odoo import fields, models, api


class ProductStock(models.Model):
    _inherit = 'product.template'

    medicine_type = fields.Selection([('liquid','Liquid'),('tablet','Tablet'),('drops','Drops'),('inhaler','Inhaler'),('injection','Injection')],'Product Type')
    medicine_category = fields.Many2one('medication', string='Product Category')
