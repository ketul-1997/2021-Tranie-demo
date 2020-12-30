from odoo import api,fields, models

class Mybook(models.Model):
    _name = "mybook"
    _inherit = 'mail.thread'
    name = fields.Char("Name")
    image = fields.Binary()
    category = fields.Many2one('category' , string="Category")
    isbn = fields.Integer("ISBN")
    publisher = fields.Char("Publisher")
    edition = fields.Char("Edition")
    author = fields.Char("Author")
    price = fields.Float("Price")


    def addtostock(self):
        partner = self.env['stock'].create({
                            'name': self.name,      
                        })
        print(partner)
        return


  

    @api.constrains('isbn')
    def _check_isbn(self):
        for d in self:
            if len(str(d.isbn))!= 7:
                raise models.ValidationError("Enter Currect ISBN Number")
