from odoo import models, fields, api

class Broker(models.Model):
    _name = 'broker.data'
    name= fields.Char('Name', required=True)
    birth_date= fields.Date('Birth Date')
    address= fields.Char('Address')
    mobile_no= fields.Char('Mobile No.')
    landlord_ids= fields.Many2many('res.partner','broker_landlord_rel','broker_id','landlord_id',string='Landlord Ids')
    tenant_ids= fields.Many2many('tenant.data','broker_tenant_rel','broker_id','tenant_id',string='Tenant Ids')
    
    