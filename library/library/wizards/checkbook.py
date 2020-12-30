from odoo import api,fields, models

class CheckbookWizard(models.TransientModel):
    _name = 'checkbook'
    
    def get_detail(self):
        print(self)
        var = self.env['bookrequest'].browse(self.env.context.get('active_ids'))
        print(var.name)
        var1 = self.env['stock'].search([('name','=',var.name)])
        print(var1.id)
        if var1.id is False:
    
            return "Not Available"
        
        else:
            if var1.quantity == 0:
                return "Not Available"
            else:
                return "Available"
        print(var1.id)
        print(type(var1))
        # return {
        # 'type': 'ir.actions.act_window',
        # 'res_model': 'checkbook',
        # 'view_mode': 'form',
        # 'res_id': self.id,
        # 'views': [(False, 'form')],
        # 'target': 'new',
        # }
                    


    name=fields.Char("Book",default=get_detail , readonly=True)
    
    # def get_default_agreements(self):
    #     return self.env['agreement'].browse(self.env.context.get('active_ids'))

    # agreement_ids = fields.Many2many('agreement',default=get_default_agreements)

    