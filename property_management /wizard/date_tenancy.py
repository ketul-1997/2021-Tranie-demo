from flectra import fields, models, api
import time
from flectra.exceptions import ValidationError


class DateTenancy(models.TransientModel):
    _name = 'date.tenancy.report.wizard'

    property_id = fields.Many2one('property.details', string="Property")
    tenancy_line = fields.One2many("tenancy.details", "tenant_id", string="Tenancy Details")
    tenant_id = fields.Many2one('res.partner', string="Tenant")
    company_id = fields.Many2one('res.company', string="Company")
    s_date = fields.Date(string="Start Date")
    e_date = fields.Date(string="Expiration Date")

    @api.multi
    @api.constrains('s_date', 'e_date')
    def _check_dates(self):
        for session in self:
            s_date = fields.Date.from_string(session.s_date)
            e_date = fields.Date.from_string(session.e_date)
            if e_date < s_date:
                raise ValidationError(('End Date cannot be set before \
                   Start Date.'))

    @api.multi
    def print_report(self):
        # template = self.env.ref('property_management.action_tenancy_report')
        data = self.read(
            ['property_id', 'tenant_id', 'company_id', 's_date', 'e_date'])[
            0]
        print("===data==", data)
        # time_table_ids = self.env['tenancy.details'].search(
        #     [('property_id', '=', self.property_id.id),
        #      ('tenant_id', '=', data['tenant_id'][0]),
        #      ('company_id', '=',self.company_id.id),
        #      ('start_date', '>', data['s_date']),
        #      ('expiration_date', '<', data['e_date'])])
        # data.update({'time_table_ids': time_table_ids.ids})
        # print(',,,,,,,,,,SSSSSSSSss', time_table_ids)
        res = self.env.ref('property_management.action_tenancy_date_report')
        # print("==========res=======", template)
        return res.report_action(self, data=data)
