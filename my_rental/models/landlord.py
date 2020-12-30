from odoo import models, fields, api

class Landlord(models.Model):
    _inherit="res.partner"
    house_ids=fields.One2many('house.data','landlord_id',string="House_ids")
    broker_ids=fields.Many2many('broker.data','broker_landlord_rel','landlord_id','broker_id', string="broker_ids")
    complaint_ids = fields.One2many('complaint.data','landlord_id',string="Complaint_ids") 