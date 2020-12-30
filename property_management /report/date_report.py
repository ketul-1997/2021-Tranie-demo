from flectra import models, api, fields
import time


class ReportDate(models.AbstractModel):
    _name = 'report.property_management.report_date_property'

    @api.model
    def get_report_values(self, tenant_id):
        print("======tenant_id========", tenant_id)
        for inv in self.env['tenancy.details'].search([('id', '=', self.tenant_id.id)]):
            print(".......inv", inv)
            print("===tenant_id========", tenant_id)

    def get_object(self, data):
        print("hello")
        data_list = []
        x = data['tenant_id']
        print("===================xxxxxxxxxxx", x)
        for i in x:
            y = i
            print("---------------y----------", y)
        time_table_ids = self.env['tenancy.details'].search([('tenant_id', '=', data['tenant_id'][0])])
        print("----------time_table_ids-----", time_table_ids)
        for rec in time_table_ids:
            te = rec.env['res.partner'].search([('tenancy_line.tenant_id', '=', data['tenant_id'][0])])
            print("--------------te---------", te)
            for pro in te:
                print("------------------pro-----------", pro)
                for pr in pro.tenancy_line:
                    sr = self.env['res.partner'].search(
                        [('tenancy_line.start_date', '>', data['s_date']),
                         ('tenancy_line.expiration_date', '<', data['e_date'])
                         ])
                    for res in pr:
                        # print("==============product==========", pr.property_id.name)
                        # print("==============product==========", pr.tenant_id.id)
                        # print("==============product==========", pr.start_date)
                        # print("==============product==========", pr.expiration_date)
                        timetable_data = {
                            'number': pr.tenancy_name,
                            'property': pr.property_id.name,
                            'tenant': pr.tenant_id.name,
                            'start_date': pr.start_date,
                            'end_date': pr.expiration_date,
                            'currency': pr.currency,
                            'rent': pr.total_rent,

                        }
                        print("====timetable_data==", timetable_data)
                        data_list.append(timetable_data)
                return data_list

            # for pro in rec.tenancy_line:
            #     te = self.env['res.partner'].search(
            #         [('id', 'in', pro.tenant_id.id), ('start_date', '>', data['s_date']),
            #          ('expiration_date', '<', data['e_date'])])
            #     print("---------------pro-----",pro)
            #
            #     print("----pro---", pro)
            #     print("ggggggg", pro.tenant_id.id)
            #     timetable_data = {
            #         'start_date': data['s_date'],
            #         'expiration_date': data['e_date'],
            #         'property_id': pro.property_id.id,
            #         'tenant_id': pro.tenant_id.id,
            #     }
            #
            #     data_list.append(timetable_data)
            # return data_list

    # def get_object(self, data):
    #     print("================")
    #     # data_list = []
    #     time_table_ids = self.env['tenancy.details'].search([('tenant_id', '=', data['tenant_id'])])
    #     print("====time_table_ids======", time_table_ids)
    #     data.update({'time_table_ids': time_table_ids.ids})
    #     print(',,,,,,,,,,SSSSSSSSss', time_table_ids)
    # for rec in time_table_ids:
    #     print("======rec=====", rec)
    #     product = rec.tenant_id.name
    #     for pro in rec.tenancy_line:
    #         print("........moves", pro)
    #         te = self.env['res.partner'].search(
    #             [('id', 'in', pro.tenant_id.id)])
    #         print("..pro...", pro)
    #         print("ggggggg", pro.tenant_id.id)
    #
    #         # for timetable_obj in self.env['tenancy.details'].browse(data['time_table_ids']):
    #         timetable_data = {
    #             'start_date': data['s_date'],
    #             'expiration_date': data['e_date'],
    #             'property_id': pro.property_id.id,
    #             'tenant_id': pro.tenant_id.id,
    #         }
    #
    #     data_list.append(timetable_data)
    # return data_list

    @api.model
    def get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        docargs = {
            'doc_ids': self.ids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'time': time,
            'start_date': data['s_date'],
            'expiration_date': data['e_date'],
            'get_object': self.get_object(data)
        }
        print("-------docargs--------", docargs)
        return docargs
