from odoo import api, fields, models

class job_stage(models.Model):
    _name = 'job.stage'

    name = fields.Char()
    sequence = fields.Integer()
    fold = fields.Boolean()

    job_state = fields.Selection(
        [('intial qualification', 'Intial qualification'),
        ('interview', 'Interview'),
        ('contract proposal', 'contract proposal')] )