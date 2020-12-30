from flectra import fields, models, api


class PropertyTypeDetails(models.Model):
    _name = 'property.type.details'
    _description = 'Property Type'

    name = fields.Char(string="Name")
