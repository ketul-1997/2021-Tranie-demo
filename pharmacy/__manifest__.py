{
    'name': 'Pharmacy',
    'depends': ['stock', 'base', 'website', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/medicine.xml',
        'views/stock_inventory_inherit.xml',
        'views/res_company_inherit.xml',
        'views/res_users_inherit.xml',
        'views/website_pharmacy_medicine_template.xml',
        'views/inventory_stock_purchase_line.xml',
        'views/res_partner_inherit.xml',
        'wizard/medicine_purchase_wizard.xml',
        'menu/menu.xml'
    ],
    'installable': True,
    'auto_install': False
}
