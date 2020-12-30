from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    medicine_line = fields.One2many('pharmacy.medicine', 'user_id', string="Medicines")
