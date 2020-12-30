{
    'name': 'library',
    'version': '1.1',
    'category': '',
    'summary': 'library managment system',
    'description': """
                  This module contains all the common features of Library Management.
    """,
    'depends': ['base','website',],
    'data': [
        'security/ir.model.access.csv',
        'security/group_view.xml',
        'wizards/checkbook_wizard.xml',
        'views/main_view.xml',  
        'views/category_view.xml',
        'views/stock_view.xml',
        'views/reader_view.xml',
        'views/register_view.xml',
        'views/br_sequence_view.xml',
        'views/book_request_view.xml',
        'views/reader_registration.xml',
        'menu/menu.xml',
    ],
    'demo': [
        'demo/category_demo.xml',
        'demo/book_demo.xml',
        
    ],
    'qweb': [
       
    ],
    'installable': True,
    'auto_install': False,
}
