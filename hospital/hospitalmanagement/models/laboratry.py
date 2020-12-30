from odoo import fields, models, api

class Laboratry(models.Model):
    _name = 'laboratry'

    name = fields.Char('Name')
    type = fields.Selection([('blood test','Blood Test'),('urine test','Urine Test'),('blood pressure','Blood Pressure'),
                             ('x-ray','X-Ray')],'type')
    doctor_id = fields.Many2one('doctor',string='Incharge')
    patient_id =  fields.Many2many('res.partner',string ='Patients')




# class BloodTest(models.Model):
#     _name = 'bloodtest'
#
#     name = fields.Char(string = "Blood Test", readonly= True, required = True, copy = False, default = 'New')
#     patient_id = fields.Many2one('res.partner','Patient')
#
#
# class