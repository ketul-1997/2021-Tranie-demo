from odoo import models, fields, api

class House_Wizard(models.TransientModel):
    _name='house.wizard'

    society = fields.Char('Society Name')
    area = fields.Char('Area')
    landmark = fields.Char('Landmark')
    city= fields.Char('City')


    def house_record_update(self):
        active_ids = self.env['house.data'].browse(self._context.get('active_ids'))
        print(active_ids)
        for active_id in active_ids:
            active_id.city= self.city
            active_id.area= self.area
            active_id.landmark= self.landmark
            active_id.society= self.society
