from openerp import fields, models, api, _

class student_wizard_data(models.TransientModel):
    _name = 'student.wizard.data'

    student_wizard_id = fields.Many2one('student.wizard','Student')
    description = fields.Text('Description')
    student_id = fields.Many2one('student', 'Student')
    res_partner_id = fields.Many2one('res.partner', 'Customer')
    employee_information_id = fields.Many2one('employee.information', 'Employee')