from odoo import models, fields, api

class Rental(models.Model):
    _name = 'rental.data'
    name = fields.Many2one('tenant.data', string="Tenant Name",required=True)
    address = fields.Char(string="House", related='name.house_name.name')
    price = fields.Integer('Rent Amount')
    start_date = fields.Date('Current Date')
    end_date = fields.Date('Expiration Date')
    tenure = fields.Integer('No. of Months', store=True)
    total = fields.Integer('Total Amount', store=True)
    landlord_id = fields.Many2one('res.partner', string="Landlord")
    user_id = fields.Many2one(
        'res.users', string='User', default=lambda self: self.env.uid, readonly=True)
    sequence= fields.Char(string='Agreement Number', required=True ,copy=False, default='New')

    @api.model
    def create(self,vals):
        if vals.get('sequence') == 'New':
            vals['sequence']= self.env['ir.sequence'].next_by_code('rental.data') or 'New'
        result = super(Rental,self).create(vals)
        return result


    @api.onchange('start_date', 'end_date', 'price')
    def onchange_dates(self):
        start = self.start_date
        end = self.end_date
        if start and end:
            month = (end.year-start.year)*12 + (end.month-start.month)
            total = month*self.price
            self.tenure = month
            self.total = total

    @api.onchange('price')
    def price_validation(self):
        if self.price > 20000:
            raise ValidationError('Rent amount cannot be greater then 20000')

    @api.constrains('end_date')
    def check_dates(self):
        for record in self:
            if record.end_date and record.end_date < record.start_date:
                raise models.ValidationError(
                    'Expiration Date must be in Future')