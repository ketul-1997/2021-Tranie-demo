{
    'name' : 'vehicle sale',
    'depends' : ["base","website"],
    'data' : [  
                'security/ir.model.access.csv',

                'views/category_view.xml',
                'views/company_view.xml',
                'views/vehicle_view.xml',
                'views/fuel_view.xml',
                'views/seller_view.xml',
                'views/seller_website.xml',
                'views/buyer_view.xml',
                'views/buyer_website.xml',
                'views/request_view.xml',

                'menu/menu.xml'
    ],
    'demo' : [],
    'category' : 'vehicle_sale',
    'installable' : True,
    'auto_install' : True
}