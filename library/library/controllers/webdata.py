from odoo import http
from odoo.http import request

class Webdata(http.Controller):
    @http.route('/library', type='http', auth='user', website=True)
    def reader_registraion(self , **kwargs):
        return request.render('library.request_form_success11')

    @http.route('/register', type='http', auth='user', website=True)
    def webdata(self , **kwargs):
        details1 = request.env['mybook'].sudo().search([])
        read = request.env['reader'].sudo().search([])
        return request.render('library.register_page_template',{'details':details1 , 'read':read})

    

    @http.route('/status', type='http', auth='user', website=True)
    def statusdata(self , **kwargs):
        details8 = request.env['reader'].sudo().search([])
        return request.render("library.status_show",{'details':details8})
     
    @http.route(['/check/mystatus/submit'], type='http', auth='public', website=True)
    def status(self , **post):
        myname = int( post.get('myname'))
        print(".....................>>>>>>>>>>>>>>>>>>>>")
        print(myname)
        print(type(myname))
        details4 = request.env['bookrequest'].sudo().search([('requestby','=',myname)])
        for i in details4:
            k = i.requestby.name
            if i.requestby.name == myname:
                print(i.state)
        return request.render('library.detail_page_template1',{'details4':details4})

    @http.route(['/reader/form'], type='http', auth="user", website=True)
    def register_form_submit(self,**post):
        var1 = post.get('name')
    
        var2 = post.get('phone_no')

        var3 = post.get('address')

        print(var1)
        print(var2)
        print(var3)

        partner = request.env['reader'].sudo().create({
                            'name': var1,
                            'phone_no' : var2,
                            'address' : var3
                        })

        print(partner)
        
        return request.render("library.request_form_success")

    @http.route(['/customer'], type='http', auth="user", website=True)
    def register_form_submit(self,**post):

        var1 = int(post.get('bookname'))
        print(type(var1))
        print(".................>>>>>>>>>>>>>>>>>>>>>")
        var2 = int(post.get('myname'))
        print(type(var2))
        print(var1)
        print(var2)
        details2 = request.env['mybook'].sudo().search([])
        details3 = request.env['reader'].sudo().search([])
        for var3 in details3:
            # print(var3.name)
            if var2 == var3.id:
                r_name = var3.name  
        print(r_name)  
        print(type(r_name))
        # print(details3)
        for var in details2:
            if var.id == var1:
                partner1 = request.env['bookrequest'].sudo().create({
                            'name': var.name,
                            'author':var.author,
                            'edition':var.edition,
                            'publisher':var.publisher,
                            'requestby': var2
                        })
        return request.render("library.request_form_success")