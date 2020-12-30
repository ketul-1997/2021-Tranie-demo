from flectra import fields, models, api


class TenancyDetails(models.Model):
    _name = 'tenancy.details'
    _rec_name = 'tenancy_name'

    tenancy_name = fields.Char('Sequence Number', readonly=True, default='New')
    property_id = fields.Many2one('property.details', string="Property", required=True)
    account_manager = fields.Char(string="Account Manager")
    currency = fields.Integer(string="Currency")
    tenant_id = fields.Many2one('res.partner', string="Tenant", required=True)
    company_id = fields.Many2one('res.company', string="Company", required=True)

    tenancy_rent = fields.Float(string="Tenancy Rent", default=100)
    account_deposit = fields.Float(string="Account Deposit", default=100)
    deposit_receive = fields.Boolean(string="Deposit Receive")
    date = fields.Date(string="Date")
    deposit_return = fields.Float(string="Deposit Return", default=0)
    d_return = fields.Boolean(string="Deposit Return")
    contact = fields.Integer(string="Contact")

    start_date = fields.Date(string="Start Date", required=True)
    rent_type = fields.Integer(string="Rent Type")
    tenancy_contact = fields.Integer(sring="Tenancy Contact")
    expiration_date = fields.Date(string="Expiration Date", required=True)
    total_rent = fields.Integer(string="Total Rent", required=True)

    # tenancy_line = fields.One2many("tenancy.details", "property_id", string="Tenancy Details")
    state = fields.Selection(
        [('new', 'New'), ('in_progress', 'In Progress'), ('close', 'Close'), ('invoice', 'Invoice')], string='Status',
        readonly=True)

    bool_field = fields.Boolean('Same text', default=True)

    @api.multi
    def confirm_new(self):
        self.state = 'new'

    @api.multi
    def confirm_inprogress(self):
        self.state = 'in_progress'

    @api.multi
    def confirm_close(self):
        self.state = 'close'

    @api.model
    def create(self, vals):
        if vals.get('tenancy_name', 'New') == 'New':
            vals['tenancy_name'] = self.env['ir.sequence'].next_by_code(
                'tenancy.details') or '/'
        return super(TenancyDetails, self).create(vals)

    @api.multi
    def make_invoices(self):
        for rec in self:
            crm_lead = self.env['account.invoice'].search([('tenancy_detail_id', '=', rec.id)])
            print("======crm_lead===", crm_lead)
            if crm_lead:
                view = self.env.ref('account.invoice_form')
                # print("======view===", view)
                # return {
                #     'partner_id': self.tenant_id.id,
                #     'account_id': self.tenant_id.property_account_receivable_id.id,
                #     'tenancy_detail_id': rec.id,
                #     'name': 'Opportunity created',
                #     'view_type': 'form',
                #     'view_mode': 'form',
                #     'view_id': view.id,
                #     'res_model': 'account.invoice',
                #     'type': 'ir.actions.act_window',
                #     'res_id': crm_lead.id,
                #     'context': self.env.context,
                # }

            else:
                invoice_data = self.env['account.invoice'].create({
                    'partner_id': self.tenant_id.id,
                    'account_id': self.tenant_id.property_account_receivable_id.id,
                    'tenancy_detail_id': rec.id,
                })
                print("----invoice_data----", invoice_data)
                view = self.env.ref('account.invoice_form')
                print("======view2===", view)
                self.bool_field = False

                # return {
                #     # 'name': 'Opportunity created',
                #     # 'view_type': 'form',
                #     # 'view_mode': 'form',
                #     # 'view_id': view.id,
                #     # 'res_model': 'account.invoice',
                #     # 'type': 'ir.actions.act_window',
                #     # 'partner_id': crm_lead.id,
                #     # 'context': self.env.context,
                #     # 'views': [(self.env.ref('account.invoice_tree').id, 'tree'),
                #     #           (self.env.ref('account.invoice_form').id, 'form'), ],
                # }
            self.state = 'invoice'

            # self.active = True

    @api.multi
    def view_invoices(self):
        for rec in self:
            # self.active = True
            crm_lead = self.env['account.invoice'].search([('tenancy_detail_id', '=', rec.id)])
            print("======crm_lead===", crm_lead)
            if crm_lead:
                view = self.env.ref('account.invoice_form')
                print("======view===", view)

                return {

                    'partner_id': self.tenant_id.id,
                    'account_id': self.tenant_id.property_account_receivable_id.id,
                    'tenancy_detail_id': rec.id,
                    'name': 'Opportunity created',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'view_id': view.id,
                    'res_model': 'account.invoice',
                    'type': 'ir.actions.act_window',
                    'res_id': crm_lead.id,
                    'context': self.env.context,


                }





class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    _inherits = {'tenancy.details': 'tenancy_detail_id'}

    tenancy_detail_id = fields.Many2one("tenancy.details", string="Tenancy Details")

# payment = self.env['account.payment'].create({
# 'payment_method_id': payment_methods and payment_methods[0].id or False,
# 'payment_type': total >0 and 'inbound' or 'outbound',
# 'partner_id': partner_id.id,
# 'partner_type': partner_type,
# 'journal_id': self.statement_id.journal_id.id,
# 'payment_date': self.date,
# 'state': 'reconciled',
# 'currency_id': currency.id,
# 'amount': abs(total),
# 'communication': self._get_communication(payment_methods[0] if payment_methods else False),
# 'name': self.statement_id.name or _("Bank Statement %s") % self.date,
# })
#
#
#
#
#
#
# @api.multi
# def make_invoices(self):
#     if not self._context.get('active_ids'):
#         return {'type': 'ir.actions.act_window_close'}
#     new_invoice = {}
#     for wizard in self:
#         repairs = self.env['mrp.repair'].browse(self._context['active_ids'])
#         new_invoice = repairs.action_invoice_create(group=wizard.group)
#
#         We have to udpate the state of the given repairs, otherwise they remain 'to be invoiced'.
#         Note that this will trigger another call to the method 'action_invoice_create',
#         but that second call will not do anything, since the repairs are already invoiced.
#         repairs.action_repair_invoice_create()
#     return {
#         'domain': [('id', 'in', list(new_invoice.values()))],
#         'name': 'Invoices',
#         'view_type': 'form',
#         'view_mode': 'tree,form',
#         'res_model': 'account.invoice',
#         'view_id': False,
#         'views': [(self.env.ref('account.invoice_tree').id, 'tree'), (self.env.ref('account.invoice_form').id, 'form')],
#         'context': "{'type':'out_invoice'}",
#         'type': 'ir.actions.act_window'
#     }
#
#
#         # return True
#
#         # payment = self.env['account.payment'].create({
#         #     'payment_method_id': payment_methods and payment_methods[0].id or False,
#         #     'payment_type': total > 0 and 'inbound' or 'outbound',
#         #     'partner_id': partner_id.id,
#         #     'partner_type': partner_type,
#         #     'journal_id': self.statement_id.journal_id.id,
#         #     'payment_date': self.date,
#         #     'state': 'reconciled',
#         #     'currency_id': currency.id,
#         #     'amount': abs(total),
#         #     'communication': self._get_communication(payment_methods[0] if payment_methods else False),
#         #     'name': self.statement_id.name or _("Bank Statement %s") % self.date,
#         # })
#
#         # inv_obj = self.env['account.invoice']
#         #      property_id = self.property_id.id
#         #      tenant_id = self.tenant_id.id
#         #      company_id = self.company_id.id
#         #      self.tenancy_id = self.tenancy_id.id
#         #      print("jjjjjjjjjjj", inv_obj)
#
#         # 't_name': tenancy_detail.tenancy_name,
#         # 'account_manager': tenancy_detail.account_manager,
#         # 'currency': tenancy_detail.currency,
#         # 'tenant': tenancy_detail.tenant_id,
#         # 'company':tenancy_detail. company_id,
#         # 'tenancy_rent': tenancy_detail.tenancy_rent,
#         # 'deposit': tenancy_detail.account_deposit,
#         # 'receive': tenancy_detail.deposit_receive,
#         # 'date': tenancy_detail.date,
#         # 'deposit return': tenancy_detail.deposit_return,
#         # 'contact': tenancy_detail.contact,
#         # 'start date': tenancy_detail.start_date,
#         # 'rent type': tenancy_detail.rent_type,
#         # 'tenancy contact': tenancy_detail.tenancy_contact,
#         # 'expiration date': tenancy_detail.expiration_date,
#         # 'rent': tenancy_detail.total_rent,
#         # 'total rent': tenancy_detail.total_rent,
#         # 'tenancy rent': tenancy_detail.tenancy_id,
#
#         # 'fiscal_position_id': tenancy_data.tenant_id.id,
#         #            'account_id': tenancy_data.company_id.id
#
#
# shakir6:57 PM
# @api.multi
# def create_opportunity(self):
#     for rec in self:
#         crm_lead = self.env['crm.lead'].search([('sale_order_id', '=', rec.id)])
#         if crm_lead:
#             view = self.env.ref('crm.crm_case_form_view_oppor')
#             return {
#                 'name': 'Opportunity created',
#                 'view_type': 'form',
#                 'view_mode': 'form',
#                 'view_id': view.id,
#                 'res_model': 'crm.lead',
#                 'type': 'ir.actions.act_window',
#                 'res_id': crm_lead.id,
#                 'context': self.env.context,
#             }
#         else:
#             crm_lead = self.env['crm.lead'].create({
#                 'name': rec.name,
#                 'partner_id': rec.partner_id.id,
#                 'email_from': rec.partner_id.email,
#                 'planned_revenue': rec.amount_total,
#                 'type': 'opportunity',
#                 'sale_order_id': rec.id,
#
#             })
#             view = self.env.ref('crm.crm_case_form_view_oppor')
#             return {
#                 'name': 'Opportunity created',
#                 'view_type': 'form',
#                 'view_mode': 'form',
#                 'view_id': view.id,
#                 'res_model': 'crm.lead',
#                 'type': 'ir.actions.act_window',
#                 'res_id': crm_lead.id,
#                 'context': self.env.context,
#             }
