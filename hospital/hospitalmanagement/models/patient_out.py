from odoo import fields, models, api

class PatientOut(models.Model):
    _name = 'patient.out'

    discharge = fields.Date('Discharge')
    patient_in_id = fields.Many2one('patient.in',string='Admitted')