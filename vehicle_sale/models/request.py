from odoo import fields, models, api

class RequestHandel(models.Model):
    _name = 'requesthandel'

    def status_change_to_requested(self):
        self.status = 'Requested'
    
    def status_change_to_accepted(self):
        self.status = 'Accepted'
    
    def status_change_to_deleted(self):
        self.status = 'Deleted'
    

    seller = fields.Many2one('seller', string="Seller")
    buyer = fields.Many2one('buyer', string="Buyer")
    bid_price = fields.Integer(string="Bid Price")
    status = fields.Char(string="Status", default="Posted", readonly=True)