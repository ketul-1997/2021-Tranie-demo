from odoo import models, fields, api

class Tenant(models.Model):
   _name = "tenant.data"

   name = fields.Char('Name')
   house_name = fields.Many2one('house.data',string="House Name")
   mobile = fields.Char('Mobile')
   email = fields.Char('Email')
   buy_rent = fields.Selection(
      [('buy','Buy'),('rent','Rent'), ('enquiring','Just Enquiring')],
      'Buy / Rent')
   price = fields.Integer('Tenant Price')
   state = fields.Selection([('draft', 'Draft'), ('done', 'Deal Accepted'),('cancel', 'Deal Rejected'),], required=True, default='draft')


   def button_accept_deal(self):
      for record in self:
         record.write({'state':'done'})
      template = self.env.ref('my_rental.send_confirm_mail_template')
      template.send_mail(self.id)
      print('Accept deal......',self)
   

   def button_reject_deal(self):
      for record in self:
         record.write({'state':'cancel'})
      template = self.env.ref('my_rental.send_reject_mail_template')
      template.send_mail(self.id)
      print('Reject deal...........', self)

   def button_draft_deal(self):
      for record in self:
         record.write({'state':'draft'})
      print('Reject deal...........', self)