{
    'name': 'Open Library',
    'author': 'Tanmay @ Bista Solutions',
    'version': '1.0',
    'category': 'Education',
    'website':'https://www.openlibrary.com',
    'description': """
    A Library build using the awesomeness of Odoo v9.
    Library functions include various business logic including:
       - Book
            - Add Book
            - Delete Book
            - Issue Book
            - Return Book
       - Members
            - Add Members
            - Delete Members
    """,
    'summary': 'Manage a library using the power of Odoo',
    'depends': ['base'],
    'demo': [],
    'data': [
        'security/library_management_security.xml',
        'security/ir.model.access.csv',
        'views/course_records_view.xml',
        'views/subject_records_view.xml',
        'views/student_records_view.xml',
        'views/teacher_records_view.xml',
        'menu/menu.xml',
    ],
    'installable': True,
    'auto-install': False,
    'application': True,
}