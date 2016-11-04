{
    'name': 'Upload Excel File',
    'author': 'Tanmay @ Bista Solutions',
    'version': '1.0',
    'category': 'Utilities',
    'sequence': 2,
    'description': """
    Upload CSV files
    """,
    'summary': 'Upload Excel File',
    'depends': ['base','sale','mrp','purchase','account_accountant'],
    'demo': [],
    'data': [
        'views/upload_view.xml',
        'menu/menu.xml',
    ],
    'installable': True,
    'auto-install': False,
    'application': True,
}