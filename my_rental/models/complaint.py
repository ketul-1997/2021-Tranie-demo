from odoo import models, fields, api

class Complaint(models.Model):
    _name = 'complaint.data'
    name = fields.Char(string='Complaint Number', required=True ,copy=False, default='New')
    ctype= fields.Char('Complaint Type')
    desc= fields.Text('Description')
    date = fields.Date('Complaint Date')
    resolved = fields.Selection(
       [('solved','Solved'),('pending','Pending'), ('inprocess','In-Process'),('unsolvable','Unsolvable')],
       'Resolved')
    landlord_id = fields.Many2one('res.partner', string= 'Landlord')
    tenant_id = fields.Many2one('tenant.data', string= 'Tenant')
    user_id = fields.Many2one(
        'res.users', string='User', default=lambda self: self.env.uid, readonly=True)

    @api.model
    def create(self,vals):
        if vals.get('name') == 'New':
            vals['name']= self.env['ir.sequence'].next_by_code('complaint.data') or 'New'
        result = super(Complaint,self).create(vals)
        return result