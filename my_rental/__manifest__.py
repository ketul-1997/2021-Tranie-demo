# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'first_rental',
    'version': '1.1',
    'category': 'house/Houses',
    'summary': 'Rental internal machinery',
    'description': """
    This is module for renting properties/houses.
    """,
    'depends': ['base','account','website','mail'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/house_wizard_view.xml',
        'wizards/complaint_wizard_view.xml',
        'reports/rental_report_template.xml',
        'reports/rental_report.xml',
        'templates/rental_templates.xml',
        'data/email_templates.xml',
        'views/house_view.xml',
        'views/landlord_view.xml',
        'views/broker_view.xml',
        'views/rental_view.xml',
        'views/complaint_view.xml',
        'views/tenant_view.xml',
        'menu/house_menus.xml',
    ],

    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'auto_install': False
}