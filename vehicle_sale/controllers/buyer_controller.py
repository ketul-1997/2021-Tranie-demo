from odoo import http
from odoo.http import request
import datetime

class VehicleBuyerWebsite(http.Controller):
    _inherit = 'seller'

    def status_change_to_requested(self,document):
        print('*************\n'*5, self.env['seller'].status,'\n','*************\n'*5)
        self.env['seller'].status = 'Requested'
        

    # @http.route(['/vehicle/buyer'], type="http", auth="public", warning=True)
    def show_warning(self):
        return {
            'warning': {
                    'title':'WARNING',
                    'message': 'Request Sent Successfully'}
               }
    
    @http.route(['/vehicle/buyer'], type='http', auth="public", website=True)
    def buyer_router(self, **post):
        buyer_info = request.env['buyer'].sudo().search([])
        vehicle_info = request.env['vehicles'].sudo().search([])
        seller_info = request.env['seller'].sudo().search([])
        return http.request.render('vehicle_sale.website_vehicle_buyer_form', {'buyer_info': buyer_info,'vehicle_info':vehicle_info, 'seller_info':seller_info})

    @http.route(['/vehicle/buyer/form/submit'], type='http', auth="user", website=True)
    def search_seller(self, **post):
        date = datetime.datetime.today()


        request.env['buyer'].create({
            'name' : post.get('name'),
            'contact_no' : post.get('contact_no'),
            'vehicle' : post.get('vehicle'),
            'date' : date
        })

        vehicle = post.get('vehicle')

        seller_info = request.env['seller'].sudo().search([('vehicle.id','ilike',vehicle),('status','ilike','Posted')])
        return http.request.render('vehicle_sale.website_vehicle_searched',{'seller_info':seller_info})

    @http.route('/vehicle/buyer/form/submit/<model("seller"):document>', auth='user', type='http', website=True)
    def buyer_info(self, document):
        seller_info = request.env['seller'].sudo().search([('id','ilike',document.id)])
        return http.request.render('vehicle_sale.website_searched_vehicle_inherit',{'seller_info':seller_info})
