from odoo import models, fields, api

class House(models.Model):
   _name = 'house.data'
   name = fields.Char('Name', required=True)
   society = fields.Char('Society')
   area = fields.Char('Area')
   landmark = fields.Char('Landmark')
   city = fields.Char('City')
   start_price = fields.Integer('Price Starts from')
   end_price = fields.Integer('Last Price')
   availability = fields.Selection(
      [('onsale','For Sale'),('onrent','For Rent'), ('sold','SOLD')],
      'Availability')
   landlord_id= fields.Many2one('res.partner', string="Landlord")
   sequence = fields.Char(string='Registered Number', required=True ,copy=False, default='New')
    
   @api.model
   def create(self,vals):
      if vals.get('sequence') == 'New':
         vals['sequence']= self.env['ir.sequence'].next_by_code('house.data') or 'New'
      result = super(House,self).create(vals)
      return result