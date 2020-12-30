from odoo import api, fields, models



class Rent_agrement(models.TransientModel):
    _name = 'coustom.report.wizard'
    

    company_name = fields.Many2one("company.registraion")
    
    # print(agreement_name.month_rent)
    # print(company_name)
    
    def render_html(self):
        l = []
        orders = self.env['employee.information'].search([('company_name', '=', self.company_name.name)])
        print(orders)
        return self.env.ref('job_management.report_user').report_action(orders)
        # return self.env.ref('job_management.model_employee_information')
        
        
        # docs = self.env['rent_agrement'].browse(self.env.context.get('active_id'))
        # print(docs.month_rent,'.....')
        # sales_records = []
        # orders = self.env['rent_agrement'].search([('user_id', '=', .id)])


        # return self.env.ref(my_model.building_report).report_action(docids)