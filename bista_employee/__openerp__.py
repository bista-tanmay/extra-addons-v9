{
    'name': 'Bista Employee Management',
    'version': '1.0',
    'category': 'Employee Management',
    "sequence": 1,
    'complexity': "easy",
    'description': """
            This module provide overall Employee Management System over OpenERP
            Features includes managing
                * Employee Details
                * Food Facilities
                * Leave Management
    """,
    'author': 'Bista Solutions',
    'website': 'www.bistaemployee.com',
    'depends': ['base','sale','report'],
    'data': [
        'views/employee_detail_view.xml',
        'wizard/employee_view_wizard.xml',
        'report/employee_report.xml',
        'report/report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
