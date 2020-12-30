from odoo import http
from odoo.http import request


class WebsiteStudent(http.Controller):
    @http.route('/books', auth='user', type="http", website=True)
    def website_course(self):
        records = request.env['product.template'].sudo().search([])
        return request.render('library_management_system.website_book_issue', {'records': records})


    @http.route('/books/issue/submit', auth='public', type="http", website=True)
    def request_book(self, **post):
        print(post.get('book_name'))

        request.env['product.template'].sudo().create({'name': post.get('book_name')})
        return request.redirect('/books')
