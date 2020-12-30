{
    'name': 'jon_management',
    'version': '1.1',
    'category': 'Sales/Sales',
    'summary': 'job management',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': ['base','website','mail',],
    
    'data': ['security/ir.model.access.csv',
            'security/user_group.xml',
            'wizard/coustom_report.xml',
            'report/employee_information.xml',
            'report/report_emoloyee_information.xml',
            'views/registration_company_view.xml',
            'views/company_job_post.xml',
            'views/employee_information_view.xml',
        # 'views/kanban_view.xml',
        
            'views/employee_data_view.xml',
            'views/job_post.xml',
            'data/mail_sending_tamplate.xml',
            
            'menu/menu.xml',
        ],

    'demo': [
    'demo/company_registration.xml',
    'demo/job_post_demo.xml',
        
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False
}
