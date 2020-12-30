from odoo import models, fields, api

class Complaint_Wizard(models.TransientModel):
    _name='complaint.wizard'

    resolved = fields.Selection(
       [('solved','Solved'),('pending','Pending'), ('inprocess','In-Process'),('unsolvable','Unsolvable')], 'Resolved')

    def complaint_record_update(self):
        active_ids = self.env['complaint.data'].browse(self._context.get('active_ids'))
        print(active_ids)
        for active_id in active_ids:
            active_id.resolved= self.resolved