from flectra import fields, models, api


class UtilityType(models.Model):
    _name = 'utility.type'
    _description = 'Utility Type'

    name = fields.Char(string='Name', size=64, required=True)
