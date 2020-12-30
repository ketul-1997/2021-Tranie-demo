from flectra import fields, models, api


class RentTypeDetails(models.Model):
    _name = 'rent.type.details'
    _description = 'Rent Type'

    name = fields.Char(string='Name', size=64, required=True)
    repeat_number = fields.Integer('Repeat every', required=True)
