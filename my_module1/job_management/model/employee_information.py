from odoo import api, fields, models

class Company_job_post(models.Model):
    _name = 'employee.information'
    _inherit = ['mail.thread','mail.mail','mail.activity.mixin']
    

    
    
    @api.model
    def default_rent_stage(self):
        Stage = self.env['job.stage']
        return Stage.search([], limit=1)
        
    
    name =  fields.Char("Enter Your Name")
    mobile_no =  fields.Char("Enter Your mobile number")
    email = fields.Char("Your Email Address")
    date_of_birth = fields.Date("Date of Birth")
    resume =  fields.Binary("Upload Resume" , attachment=True)
    company_name = fields.Char("Company Name")
    job_info = fields.Char("Job Role")
    stage_id = fields.Many2one('job.stage',default=default_rent_stage)
    

        
    
       
    def book_return_reminder(self):

        # Find the e-mail template
        template = self.env.ref('job_management.book_return_reminder')
        print(template,'heloo i am tamplate')
        print(template.id,'hello i am tamplateid')
        print(template.email_from)

        template.send_mail(self.id)
        