from flectra import fields, models, api


class TenancyValuation(models.TransientModel):
    _name = 'tenancy.detail.report.wizard'

    property_id = fields.Many2one('property.details', string="Property")

    tenant_id = fields.Many2one('res.partner', string="Tenant")
    company_id = fields.Many2one('res.company', string="Company")
    currency = fields.Integer(string="Currency")
    start_date = fields.Date(string="Start Date")
    expiration_date = fields.Date(string="Expiration Date")
    total_rent = fields.Integer(string="Total Rent")

    @api.multi
    def invoice(self):
        # recs = self.env['tenancy.details'].search([('property_id', '=', self.property_id.id)])
        data = self.read(
            ['property_id', 'tenant_id', 'company_id', 'start_date', 'expiration_date'])[
            0]
        print("===data==", data)
        # print(',,,,,,,,,,SSSSSSSSss', recs)

        res = self.env.ref('property_management.action_property_report')
        print("==========res=======", res)
        return res.report_action(self,data=data)














    # @api.multi
    # def print_report(self):
    #     start_date = fields.Date.from_string(self.start_date)
    #     expiration_date = fields.Date.from_string(self.expiration_date)
    #     print("hadfashdshhd", start_date)
    #     print("jfhsjffhf", expiration_date)
    #     if start_date > expiration_date:
    #         raise ValidationError(("End Date cannot be set before \
    #         Start Date."))
    #     else:
    #         recs = self.env['tenancy.details'].search([('id', '=', self.property_id.id)])
    #         print("====rec=========", recs)
    #         data = self.read(
    #             ['property_id', 'tenant_id', 'company_id', 'currency', 'start_date', 'expiration_date', 'total_rent'])[
    #             0]
    #         print("helo---data---", data)
    #         for report in data:
    #             report = self.env.ref(
    #                 'property_management.action_repo_tenancy_details')
    #             print("hi--report---", report)
    #             return report.report_action(self, data=data)
    #



        #
        # recs = self.env['tenancy.details'].search([('id', '=', self.property_id.id)])
        # print(',,,,,,,,,,SSSSSSSSss', recs)
        # data = self.read(
        #     ['property_id', 'tenant_id', 'company_id', 'currency', 'start_date', 'expiration_date', 'total_rent'])[
        #     0]
        # print("helo---data---", data)
        # for res in data:
        #     res = self.env.ref('property_management.action_tenancy_del_repo').report_action(recs)
        #     print("==========res=======", res)
        #     return res
