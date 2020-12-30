from odoo import models, fields, api


class BookRecord(models.Model):
    _name = 'lms.books'
    _rec_name = 'qty'

    name = fields.Char()
    book_type = fields.Selection(string='Book Type',
                                 selection=[('comic', 'Comic'), ('study', 'Study'), ('story', 'Story')])
    qty = fields.Integer()

    def IssueBook(self):
        # print(self.name,'-----------------in name\n\n\n\n')
        if self.qty == 0:
            self.qty = 0
        else:
            self.qty = self.qty - 1
