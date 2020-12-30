from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,date

class Doctor(models.Model):
    _name = 'doctor'


    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Gender')
    department = fields.Many2one('doctordepartment',string='Department')
    yearexp = fields.Integer(string='Years Of Experience')
    patient_id = fields.Many2many('res.partner',string='Patients')


    @api.onchange('dob')
    def compute_age(self):
        if self.dob:
            date1 = str(self.dob)
            d1 = datetime.strptime(date1, "%Y-%m-%d").date()

            d2 = date.today()

            self.age = relativedelta(d2, d1).years

