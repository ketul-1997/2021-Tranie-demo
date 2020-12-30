from odoo import http, _
from odoo.http import request
from odoo.exceptions import ValidationError


class WebsitePharmacyMedicine(http.Controller):
    @http.route('/pharmacy/medicine/form', auth='public', type='http', website=True)
    def website_pharmacy_medicine(self):
        domain = [('stock', '>', 0)]
        medicines = request.env['pharmacy.medicine'].sudo().search(domain)
        return request.render('pharmacy.website_pharmacy_medicine_template_form', {
            'medicines': medicines
        })

    @http.route('/pharmacy/medicine/form/submit', auth='public', type='http', website=True)
    def website_pharmacy_medicine_submit(self, **post):
        print("----------post in submit\n\n", post)
        name = post.get('name')
        domain = [('name', '=', name)]
        medicines = request.env['pharmacy.medicine'].sudo().search(domain)
        return request.render('pharmacy.website_pharmacy_medicine_template_form_submit', {
            'medicines': medicines
        })

    @http.route('/pharmacy/medicine/form/qty/<model("pharmacy.medicine"):medicines>', auth='user', type='http',
                website=True)
    def website_pharmacy_medicine_qty(self, medicines, **post):
        print("----------post\n\n", post)
        print("----------medicines in qty\n\n", medicines)
        cust_name = post.get('cust_name')
        qty = int(post.get('qty'))
        user = request.env.user.id
        print("--------current user\n\n", user)

        if medicines.stock:
            if qty <= medicines.stock:
                c = request.env['res.partner'].create({'name': cust_name})
                request.env['pharmacy.inventory.stock.purchase.line'].create(
                    {'customer_id': c.id, 'medicine_id': medicines.id, 'stock_purchase': qty,
                     'stock_id': medicines.stock_id.id})
                medicines.stock = medicines.stock - qty
            else:
                raise ValidationError(_("We have only %d stock left of %s and you are buying %d") % (
                    medicines.stock, medicines.name, qty))
        else:
            raise ValidationError("Medicines are out of stock")

        return request.render('pharmacy.website_pharmacy_medicine_template_thanks')
