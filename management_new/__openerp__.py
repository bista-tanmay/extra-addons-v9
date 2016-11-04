{
    'name': 'School-Employee Management',
    'version': '1.0',
    'author': 'Tanmay @ Bista Solutions',
    'category':'learning',
    'description':"""
    Different management applications are incorporated in this module
        - School Management includes:
            - Student Records
            - Subject Records
            - Teacher Records
    """,
    'depends': ['base'],
    'data': [
        'views/student_records_view.xml',
        'views/subject_records_view.xml',
        'views/teacher_records_view.xml',
        'wizard/result_wizard_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}