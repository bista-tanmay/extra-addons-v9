{
    'name': 'Vet Clinic',
    'version': '1.0',
    'description': """
    A Vet Clinic build using Openerp.
    """,
    'author': 'Tanmay @ Bista Solutions',
    'depends': ['base','sale'],
    'data': [
             'views/vet_clinic_animal_view.xml',
             ],
    'installable': True,
    'auto_install': False,
}
