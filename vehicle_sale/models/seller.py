from odoo import fields, models, api

class SellerPost(models.Model):
    _name = "seller"


    def status_change_to_requested(self):
        print('Status Changed to Requested\n'*5)
        self.status = 'Requested'

    def status_change_to_delivered(self):
        self.status = 'Delivered'

    def status_change_to_canceled(self):
        self.status = 'Canceled'
    
    # @api.onchange('category', 'vehicles')
    # def choose_vehicle(self):
    #     self.vehicle = self.env['vehicles'].sudo().search([('category.name','ilike',self.category.name)])
    #     print('Vehicles:', self.vehicle)

        # return vehicle


    name = fields.Char(string="Name", required=True)
    contact_no = fields.Char(string="Contact No", required=True)
    category = fields.Many2one('category',string="Category")
    vehicle = fields.Many2one("vehicles", string="Vehicle", required=True)
    # model = fields.Many2one("vehicles.model", string="Model", required=True)
    model_year = fields.Char(string="Model Year", required=True)
    # fuel = fields.Char(string="Fuel")
    fuel = fields.Many2one("fueltype", string="Fuel")
    rc_no = fields.Char(string="Rc No")
    price = fields.Integer(string="Price", required=True)
    kilometers = fields.Integer(string="Kilometers", required=True)
    status = fields.Char(string="Status", required=True, default='Posted', readonly=True)
    image = fields.Binary(string="Image")