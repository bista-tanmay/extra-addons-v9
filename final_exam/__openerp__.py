{
    'name': 'Final Exam',
    'author': 'Tanmay @ Bista Solutions',
    'version': '1.0',
    'category': 'Examination',
    'sequence': 1,
    'website':'https://www.practicalexam.com',
    'description': """
    The Final Practical Test
    """,
    'summary': 'Practical Test.Pushing the limits',
    'depends': ['base','sale','purchase','hr'],
    'demo': [],
    'data': [
        'security/final_exam_security.xml',
        'security/ir.model.access.csv',
        'views/purchase_order_view.xml',
        'report/purchase_order_report_new.xml',
        'report/reports.xml',
        'report/custom_purchase_order_report.xml',
    ],
    'installable': True,
    'auto-install': False,
    'application': True,
}