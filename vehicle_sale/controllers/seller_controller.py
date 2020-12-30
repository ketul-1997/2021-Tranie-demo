from odoo import http
from odoo.http import request
import base64

class VehicleSellerWebsite(http.Controller):
    _inherit ='ir.attachment'

    @http.route(['/vehicle/seller'], type='http', auth="public", website=True)
    def seller_route(self,**post):
        seller_info = request.env['seller'].sudo().search([])
        return http.request.render('vehicle_sale.website_vehicle_seller',{'seller_info':seller_info})

    @http.route('/vehicle/seller/<model("seller"):document>', auth='user', type='http', website=True)
    def seller_info(self, document):
        seller_info = request.env['seller'].sudo().search([('id','ilike',document.id)])
        return http.request.render('vehicle_sale.website_vehicle_seller_inherit',{'seller_info':seller_info})


    @http.route(['/vehicle/seller/form'], type='http', auth="public", website=True)
    def seller_form(self,**post):
        seller_info = request.env['seller'].sudo().search([])
        vehicle_info = request.env['vehicles'].sudo().search([])
        category_info = request.env['category'].sudo().search([])
        fuel_info = request.env['fueltype'].sudo().search([])
        return http.request.render('vehicle_sale.vehicle_selling_form',{'seller_info':seller_info,'vehicle_info':vehicle_info,'fuel_info':fuel_info,'category_info':category_info})

    @http.route(['/vehicle/seller/form/submit'], type='http', auth="public", website=True)
    def seller_form_submit(self,**post):
        print('****************\n'*5,
        'Name\t\t:\t',post.get('name'), type(post.get('name')),
        '\nVehicle\t:\t',post.get('vehicle'),type(post.get('vehicle')),
        '\nKilometers\t:\t',post.get('kilometers'),type(post.get('kilometers')),
        '\nImage\t:\t', post.get('image'),type(post.get('image')),
        '\n****************\n'*5)

        # try:
        #     if post.get('image'):
        #         Attachments = request.env['ir.attachment']
        #         name = post.get('image')
        #         file = post.get('image')

        #         print('****************\n'*5)
        #         print('File Name\t:\t', name)
        #         print('File\t\t:\t', file)
        #         print('****************\n'*5)

        #         attachment_id = Attachments.sudo().create({
        #             'name':name,
        #             'datas_fname': name,
        #             'res_name': name,
        #             'type': 'binary', 
        #             'res_model': 'seller.image',
        #             'res_id': 'seller.id',
        #             'datas': base64.encodestring(file)
        #         })

        #         print('Attachmet Id\t:\t', attachment_id)
        #         # value = {​​​​​​​​'attachment' : attachment_id}

        # except Exception as e:
        #     print(e)


        request.env['seller'].create({
            'name': post.get('name'),
            'contact_no': post.get('contact_no'),
            'category' : post.get('category'),
            'vehicle': post.get('vehicle'),
            'model_year' : post.get('model_year'),
            'fuel' : post.get('fuel'),
            'rc_no' : post.get('rc_no'),
            'price' : post.get('price'),
            'kilometers' : post.get('kilometers'),
            'image' : post.get('base64.encodestring(image)')
        })
        return request.redirect('/vehicle/seller')
