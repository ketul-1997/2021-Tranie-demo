from odoo import fields, models, api

class DoctorDepartment(models.Model):
    _name = 'doctordepartment'

    name = fields.Char('Department')
