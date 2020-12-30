from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MedicinePurchaseWizard(models.TransientModel):
    _name = 'medicine.purchase.wizard'

    medicine_id = fields.Many2one('pharmacy.medicine', string='Medicines')
    customer_name = fields.Char(string='Customer Name')
    qty = fields.Integer(string='Quantity')

    def purchase_medicine(self):
        medicines = self.medicine_id
        customer_name = self.customer_name
        qty = self.qty
        if medicines.stock:
            if qty <= medicines.stock:
                c = self.env['res.partner'].create({'name': customer_name})
                self.env['pharmacy.inventory.stock.purchase.line'].create(
                    {'customer_id': c.id, 'medicine_id': medicines.id, 'stock_purchase': qty,
                     'stock_id': medicines.stock_id.id})
                medicines.stock = medicines.stock - qty
            else:
                raise ValidationError(_("We have only %d stock left of %s and you are buying %d") % (
                    medicines.stock, medicines.name, qty))
        else:
            raise ValidationError("Medicines are out of stock")
