from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,date

class Patient(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(string ='Age')
    dob = fields.Date(string= 'Date of Birth')
    gender = fields.Selection([('male','Male'),('female','Female')],'Gender')
    height = fields.Float(string = 'Height')
    weight = fields.Float(string = 'Weight')
    address = fields.Text(string= 'Address')
    disease = fields.Char(string= 'Problem Definition')
    doctor_id = fields.Many2many('doctor', string='Doctor')
    laboratry_id = fields.Many2many('laboratry',string= 'Test Required')
    medicine_id = fields.Many2many('product.template', string='Prescription')

    @api.onchange('dob')
    def compute_age(self):
        if self.dob:
            date1 = str(self.dob)
            d1 = datetime.strptime(date1, "%Y-%m-%d").date()

            d2 = date.today()

            self.age = relativedelta(d2, d1).years