{
    'name': 'Bon Voyage',
    'version': '1.0',
    'category':'Paani',
    'description': """
    A Boat Company build using Openerp.
    """,
    'author': 'Tanmay @ Bista Solutions',
    'depends': ['base','sale','mrp'],
    'data': [
             'views/boat_company_view.xml',
             ],
    'installable': True,
    'auto_install': False,
}
