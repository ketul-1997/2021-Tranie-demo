from odoo import fields, models, api

class PatientIn(models.Model):
    _name = 'patient.in'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Patient')
    admission = fields.Date('Admission')
    room_id = fields.Many2one('room',string='Alloted Room')

    @api.onchange('room_id')
    def room_allocation(self):
        if self.room_id:
            id = self.room_id.id
            room = self.env['room'].search([('id','ilike',id)])
            patient = self.partner_id
            room.write({
                'patient_id':patient
            })




