from flectra import fields, models, api


class MaintenanceType(models.Model):
    _name = 'maintenance.type'
    _description = 'Maintenance Type'

    name = fields.Char(string='Name', size=64, required=True)
