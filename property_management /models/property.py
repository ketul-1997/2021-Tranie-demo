from flectra import fields, models, api


class PropertyDetails(models.Model):
    _name = 'property.details'
    _inherits = {'product.template': 'product_id'}

    product_id = fields.Many2one('product.template', string="Product")

    number = fields.Char('Sequence Number', readonly=True, default='New')
    address = fields.Char(string="Address", required=True)
    latitude = fields.Float(string="Latitude")
    longitude = fields.Float(string="Longitude")
    date = fields.Date(string="Date", required=True)
    no_tower = fields.Integer(string="Number Of Tower", default=0)
    gfa_sqit = fields.Integer(string="GFA(sqit)", default=0)
    gfa_meter = fields.Integer(string="GFA(meter)", default=0)
    active = fields.Boolean(string="Active")

    property_type_id = fields.Many2one('property.type.details', string="Property Type", required=True)
    property_manager_id = fields.Many2one('res.users', string="Property Manager", required=True)
    furnishing = fields.Selection(
        [('none', 'None'), ('semi_furnishing', 'Semi Furnishing'), ('full_furnishing', 'Full Furnishing')],
        default='none')
    bedrooms = fields.Integer(string="Bed Rooms", required=True)
    facing = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string="Facing")
    property_category = fields.Char(string="Property Category")
    company_id = fields.Many2one('res.company', string="Property ManagementCompany", required=True)
    company_url = fields.Char(string="Company Video URL")
    currency_id = fields.Many2one('res.currency', string="Currency", required=True)

    already_product = fields.Boolean(string="Already Partner")
    income_account_id = fields.Many2one('account.account', string="Income Account", required=True)
    external_account_id = fields.Many2one('account.account', string="External Account", required=True)

    state = fields.Selection([('available', 'Available'), ('sold', 'Sold'), ('booked', 'Booked'), ('sale', 'Sale'),
                              ('on_lease', 'On Lease')],
                             default='available')
    tenancy_line = fields.One2many("tenancy.details", "property_id", string="Tenancy Details")

    @api.multi
    def button_available(self):
        for rec in self:
            rec.write({'state': 'available'})

    @api.multi
    def button_sold(self):
        for rec in self:
            rec.state = 'sold'

    @api.multi
    def button_booked(self):
        for rec in self:
            rec.state = 'booked'

    @api.multi
    def button_sale(self):
        for rec in self:
            rec.write({'state': 'sale'})

    @api.multi
    def button_lease(self):
        for rec in self:
            rec.state = 'on_lease'

    @api.model
    def create(self, vals):
        if vals.get('number', 'New') == 'New':
            vals['number'] = self.env['ir.sequence'].next_by_code(
                'property.details') or '/'
        return super(PropertyDetails, self).create(vals)
