from flectra import models, api, fields
import time


class ReportDate(models.AbstractModel):
    _name = 'report.property_management.report_property_details'

    @api.model
    def get_report(self, property_id):
        print("======tenant_id========", property_id)
        for inv in self.env['tenancy.details'].search([('id', '=', self.property_id.id)]):
            print(".......inv", inv)
            print("===tenant_id========", property_id)

    def get_data(self, data):
        print("hello")
        data_list = []
        x = data['property_id']
        print("===================xxxxxxxxxxx", x)
        for i in x:
            y = i
            print("---------------y----------", y)
        time_table_ids = self.env['tenancy.details'].search([('property_id', '=', data['property_id'][0])])
        print("----------time_table_ids-----", time_table_ids)
        for rec in time_table_ids:
            te = rec.env['property.details'].search([('tenancy_line.property_id', '=', data['property_id'][0])])
            print("--------------te---------", te)
            for pro in te:
                print("------------------pro-----------", pro)
                for pr in pro.tenancy_line:
                    sr = self.env['property.details'].search(
                        [('tenancy_line.property_id', 'in', data['property_id']),
                         ('tenancy_line.tenant_id', 'in', data['tenant_id'])
                         ])
                    print("xxxxxxxxxxxxxxxxxxxxxxxx", sr)
                    for res in pr:
                        # print("==============product==========", pr.property_id.name)
                        # print("==============product==========", pr.tenant_id.id)
                        # print("==============product==========", pr.start_date)
                        # print("==============product==========", pr.expiration_date)
                        timetable_data = {
                            'number':pr.tenancy_name,
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
            'start_date': data['start_date'],
            'expiration_date': data['expiration_date'],
            'get_data': self.get_data(data)
        }
        print("-------docargs--------", docargs)
        return docargs
