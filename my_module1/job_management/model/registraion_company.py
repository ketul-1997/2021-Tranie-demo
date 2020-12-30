from odoo import api, fields, models

class Company(models.Model):
    _name = 'company.registraion'
    
    name = fields.Char("Company Name", required=True)
    image = fields.Binary()
    c_mobile = fields.Char("Contact no", required=True)
    pin_code = fields.Char("Pincode")
    address = fields.Char("Enter Your Company Addres") 
    email = fields.Char("Enter Company Email")
