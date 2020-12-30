from odoo import fields, models, api

class Appointment(models.Model):
    _name = 'appointment'

    name = fields.Char(string = "Application Number", readonly= True, required = True, copy = False, default = 'New')
    date = fields.Datetime(string='Book Appointment')
    patient_id = fields.Many2one('res.partner','Patient')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('appoint') or 'New'
        result = super(Appointment, self).create(vals)
        return result

