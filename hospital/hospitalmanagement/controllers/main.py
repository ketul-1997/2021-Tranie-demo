from odoo import http
from odoo.http import request

class Main(http.Controller):

    @http.route('/appointment', type='http', auth='user', website=True)
    def appointment(self,**post):

        return request.render('hospitalmanagement.template_appointment')

    @http.route('/appointment/form/submit', type='http', auth='user', website=True)
    def appointment_booking(self,**post):
        patient = request.env['res.partner'].create({
            'name':post.get('patient'),
            'age':post.get('age'),
            'dob':post.get('dob'),
            'gender':post.get('gender'),
            'height':post.get('height'),
            'weight':post.get('weight'),
            'address':post.get('address'),
            'mobile':post.get('mobile'),
            'disease':post.get('problem')
        })

        request.env['appointment'].create({
            'date': post.get('date'),
            'patient_id': patient.id
        })

        return request.render('hospitalmanagement.booking_successful')

    @http.route('/patient', type='http', auth='user', website=True)
    def patient(self, **post):
        patient = request.env['res.partner'].sudo().search([])
        return request.render('hospitalmanagement.template_patient',{
            'patient':patient
        })

    @http.route('/patient/details', type='http', auth='user', website=True)
    def patient_get_details(self, **post):
        id = post.get('patient')
        patient = request.env['res.partner'].sudo().search([('id','ilike',id)])

        return request.render('hospitalmanagement.patient_details',{
            'patients':patient
        })

    @http.route('/patient/edit/<model("res.partner"):patient>', type='http', auth='user', website=True)
    def patient_details_edit(self,patient):
        patients = request.env['res.partner'].sudo().search([('id','ilike',patient.id)])

        return request.render('hospitalmanagement.edit_patient',{
            'patient':patients
        })

    @http.route('/patient/edit/submit', type='http', auth='user', website=True)
    def patient_edit_submit(self,**post):
        name = post.get('name')
        patient = request.env['res.partner'].sudo().search([('name', 'ilike', name)])
        patient.write({
            'height':post.get('height'),
            'weight':post.get('weight'),
            'mobile':post.get('mobile'),
            'address':post.get('address')
        })

        return request.redirect('/patient')

    @http.route('/room/selection', type='http', auth='user', website=True)
    def patient_room_get_details(self, **post):
        patient = request.env['res.partner'].sudo().search([])
        room = request.env['room'].sudo().search([])
        return request.render('hospitalmanagement.admit_room_template', {
            'patient': patient,
            'room':room
        })

    @http.route('/room/appointed', type='http', auth='user', website=True)
    def room_assigned(self, **post):
        request.env['patient.in'].create({
            'partner_id':post.get('patient'),
            'admission':post.get('date'),
            'room_id':post.get('room')
        })

