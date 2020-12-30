from flectra import fields, models, api


class TenantDetails(models.Model):
    _inherit = 'res.partner'

    occupation = fields.Char(string="Occupation")
    company_id = fields.Many2one('res.company', string="Company")
    identity_proof = fields.Binary(
        "Identity Proof", attachment=True,
        help="Medium-sized photo of the employee. It is automatically "
             "resized as a 128x128px image, with aspect ratio preserved. "
             "Use this field in form views or some kanban views.")

    sales = fields.Char(string="Sales And Purchase")
    accounting = fields.Char(string="Accounting")
    location = fields.Char(string="Get Location")
    open_folder = fields.Char(string="Open")

    tenancy_line = fields.One2many("tenancy.details", "tenant_id", string="Tenancy Details")

