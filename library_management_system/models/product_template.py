from odoo import models, api, fields
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    book_name = fields.Char()
    book_type = fields.Selection(string='Book Type',
                                 selection=[('comic', 'Comic'), ('study', 'Study'), ('story', 'Story')])
    author_name = fields.Char()
    qty = fields.Integer()

    def IssueBook(self):
        if self.qty == 0:
            self.qty = 0
        else:
            self.qty = self.qty - 1

    @api.constrains('qty')
    def _check_value(self):
        if self.qty < 0:
            raise ValidationError("Quantity can't be less then ZERO : %s" % self.qty)
