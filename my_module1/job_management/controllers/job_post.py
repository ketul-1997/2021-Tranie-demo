from odoo import http
from odoo.http import request
import base64

class Job_management(http.Controller):


    @http.route('/jobpost', auth='user', type='http' ,website=True)
    def job_post(self, **post):
        print('hello')
        job_post_info = request.env['job.post'].sudo().search([])
        for rec in job_post_info:
            print(rec.start_date)
            
        return http.request.render('job_management.jobpost_website', {'job_post_info': job_post_info })



    @http.route('/jobpost/<model("job.post"):document>', auth='user', type='http' ,website=True)
    def info(self, document):
        print(document,"doc........")
        job_post_info = request.env['job.post'].sudo().search([('id','=',document.id)])
        print(job_post_info.c_name.name)
        return http.request.render('job_management.jobpost_website_inherit', {'job_post_info': job_post_info })
    


    
    @http.route('/jobpost/employee/<model("job.post"):employee>', auth='user', type='http' ,website=True)
    def employee(self, employee):
        print(employee,'....................')
        employee_info = request.env['job.post'].sudo().search([('id','=',employee.id)])
        # employee_info = request.env['employee.information'].sudo().search()
        print(employee_info.job_info)
        return http.request.render('job_management.employee_apply_form',{'employee_info': employee_info })
    
    
    
    @http.route('/employee/form/submit', type='http', auth="user", website=True)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):
        print(post,'poist')
        if post.get('attachment'):
            print('enterr............................')
            name = post.get('attachment')
            
        # attechment_list.append(attachment.id)
        #     # file = post.get('attachment').read()
        #     # attachment = file.read()
        #     print(name,'hello...............................')
        #     # print(base64.decode(file, file))
        #     Attachments = request.env['ir.attachment']
        #     attachment_id = Attachments.sudo().create({
        #             'name':name,
        #             'datas_fname': name,
        #             'res_name': name,
        #             'type': 'binary',   
        #             'res_model': 'employee.information',
        #             'datas': base64.encodestring(file),
        #         })
        #     print(attachment_id)
        #     value = {
        #             'attachment' : attachment_id
        #         }
            # print(value,'............') 
            partner = request.env['employee.information'].sudo().create({
                    'name': post.get('name'),
                    'mobile_no': post.get('mobile_no'),
                    'email':post.get('email'),
                    'date_of_birth':post.get('date_of_birth'),
                    # 'resume': value,
                    'company_name':post.get('company_name'),
                    'job_info':post.get('job_info'),
                })
            attached_files = request.httprequest.files.getlist('attachment')
            for attachment in attached_files:
                attached_file = attachment.read()
                attachment = request.env['ir.attachment'].sudo().create({
                    'name': attachment.filename,
                    'res_model': 'employee.information',
                    'res_id': partner,
                    'type': 'binary',
                    # 'name': attachment.filename,
                    'datas': base64.encodestring(attached_file),
                })
        return request.redirect('/')
        