from odoo import fields, models, api

class Room(models.Model):
    _name = 'room'

    name = fields.Char('Name')
    type = fields.Selection([('general','General'),('sharing ward','Sharing Ward'),('private','Private')],'type')
    patient_id = fields.Many2many('res.partner',string= 'patients')
    total_beds = fields.Integer('Beds')
    occupied_beds = fields.Integer('Occupied',compute = '_compute_no_beds',default= 6)


    @api.onchange('patient_id')
    def available_bed(self):

        self.occupied_beds = self.occupied_beds - 1

    @api.depends('patient_id', 'occupied_beds')
    def _compute_no_beds(self):
        for rec in self:
            rec.occupied_beds = rec.occupied_beds + len(rec.patient_id)



