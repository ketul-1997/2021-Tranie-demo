from odoo import http
from odoo.http import request

class RentalController(http.Controller):
    
    @http.route('/rental', type="http", auth="public", website=True)
    def rental(self, **post):
        rental = request.env['house.data'].sudo().search(['|',('availability','=','onsale'),('availability','=','onrent')])
        print('................',rental)
        return request.render('my_rental.house_data_template',{'rentals':rental})

    @http.route('/rental/<model("house.data"):build>', type="http", auth="public", website=True)
    def house_details(self, build, **post):
        print("Record Object.........................", build)
        house_details = request.env['house.data'].search([('id', 'ilike', build.id)])
        return request.render('my_rental.house_name_template', {'house': house_details})

    @http.route('/rental/house/<model("res.partner"):build>', type="http", auth="public", website=True)
    def landlord_details(self, build, **post):
        print("Landlord Object............", build)
        landlord_details =  request.env['res.partner'].search([('id','=',build.id)])
        return request.render('my_rental.landlord_name_template',{'landlord': landlord_details})

    @http.route('/rental/house/form', type="http", auth="public", website=True)
    def tenant_data_form(self, **post):
        house = request.env['house.data'].sudo().search(['|',('availability','=','onsale'),('availability','=','onrent')])
        return request.render('my_rental.house_tenant_form', {'houses':house})

    @http.route(['/rental/house/form/submit'], type='http', auth="public", website=True)
    def building_form_submit(self, **post):
        tenant_new_record = request.env['tenant.data'].create({
            'name': post.get('name'),
            'house_name': post.get('house_name'),
            'mobile': post.get('mobile'),
            'email': post.get('email'),
            'buy_rent': post.get('buy_rent'),
            'price': post.get('price'),
        })
        return request.render("my_rental.house_tenant_form_success", {})
