from flectra import fields, models, api


class RoomDetails(models.Model):
    _name = 'room.details'
    _description = 'Room Type'

    name = fields.Char(string='Name', size=64, required=True)

