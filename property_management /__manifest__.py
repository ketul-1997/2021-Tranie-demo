# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': "Property Management",
    'author': 'Tech Receptives1',
    'sequence': 10,
    'installable': True,
    'auto_install': False,
    'version': '1.1',
    'summary': 'Manage Property',
    'depends': ['sale_management', 'product', 'sale'],
    'data': ['views/tenant_views.xml',
             'views/tenancy_views.xml',
             'views/property_views.xml',
             'views/property_type_views.xml',
             'views/rent_type_views.xml',
             'views/room_views.xml',
             'views/utility_views.xml',
             'views/maintaince_view.xml'
             'report/date_report.xml',
             'report/date_menu.xml',
             'report/tenancy_report.xml',
             'report/tenancy_menu.xml',
             'wizard/tenancy_valuation_views.xml',
             'wizard/date_views.xml',
             'data/queue_sequence.xml', ],
    'demo': ['demo/property_demo.xml', ],
    'category': 'Hidden',
    'description': 'TEST'
}
