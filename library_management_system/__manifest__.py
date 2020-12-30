{
    'name': 'Library Management System',
    'depends': ['product', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/books.xml',
        'views/product_template_inherit.xml',
        'views/website_book_details.xml',
        'menu/menu.xml'
    ],

    'installable': True,
    'auto_install': False,

}
