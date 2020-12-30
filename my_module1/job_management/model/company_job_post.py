from odoo import api, fields, models
from datetime import timedelta
from datetime import date

class Company_job_post(models.Model):
    _name = 'job.post'
    _rec_name = 'c_name'
    c_name = fields.Many2one("company.registraion",string='Company Name', required=True)
    c_mobile = fields.Char("Contact no", required=True)
    pin_code = fields.Char("Pincode")
    email = fields.Char("Enter Company Email")
    address = fields.Char("Enter Your Company Addres")
    job_info = fields.Char("job name")
    start_date = fields.Date('Start Date')
    end_date = fields.Date("End Date")
    no_of_postion = fields.Integer("Number of hires for this role")
    job_type = fields.Selection(
             [('full-time', 'Full-time'),
             ('part-time', 'Part-time'),],
             'Job-type' )
    job_description = fields.Text("Enter your small information about your job")
    salary = fields.Float("salary per month")




    @api.onchange("start_date","end_date")
    def onchange_dates(self):
        for r in self:
            if r.start_date and r.end_date:
                if r.end_date < r.start_date:
                    raise models.ValidationError('Release date must be in the past') 