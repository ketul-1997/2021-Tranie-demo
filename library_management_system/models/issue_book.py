from odoo import models, fields, api


class IssueBook(models.Model):
    _name = 'lms.book.issue'
    _rec_name = 'book_id'

    book_id = fields.Many2one("product.template", string="Issue Book")
    qty_id = fields.Many2one("product.template", string="Quantity")

    def IssueBook(self):
        # print(self.name,'-----------------in name\n\n\n\n')
        if self.qty_id == 0:
            self.qty_id = 0
        else:
            self.qty_id = self.qty_id - 1
