{
  'name': 'OpenAcademy',
  'author': 'OpenERP SA',
  'summary': 'Openacademy Training course, session ,attendee',
  'category': 'Tools',
  'website': 'www.openerp.com',
  'description': """
This Module is used for 
=================================
Training course,
Training Session,
Register Attendee,
  """,
  'depends': ['base', 'mail', 'board', 'sale'],
  'data': ['wizard/openacademy_wiz_view.xml', 
           'security/openacademy_security.xml',
           'security/ir.model.access.csv',
           'openacademy_sequence.xml', 
           'openacademy_view.xml', 
           'board_openacademy_view.xml', 
           'openacademy_workflow.xml',
           'openacademy_report.xml'],
  'installable': True
}