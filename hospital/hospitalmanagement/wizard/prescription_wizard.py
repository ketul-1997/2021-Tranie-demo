from odoo import fields, models, api


class DoctorWizard(models.TransientModel):
    _name = 'doctor.wizard'

    patient_id = fields.Many2one('res.partner','Patient Name')
    medicine_id = fields.Many2many('product.template',string = 'Prescription List')

    def prescribe_medicine(self):
        patient = self.env['res.partner'].search([('id','ilike',self.patient_id.id)])
        patient.write({
            'medicine_id':self.medicine_id
        })

