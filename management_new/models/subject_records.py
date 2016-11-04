from openerp import models, fields, api, _
from openerp.exceptions import except_orm

class subject_records(models.Model):
    _name = 'subject.records'

    # Only useful when there is no name field defined. By default Odoo recognizes a name field from our model.
    # _rec_name = 'name'

    _description = 'Subject Records'

    name = fields.Char('Subject Name')
    # Student ID field as a Many to One field
    # Syntax: fields.Many2One('opposite.model.name','string')
    student_id = fields.Many2one('student.records', 'Student Name')
    # minimum_marks = fields.Integer('Minimum Marks')
    marks_obtained = fields.Integer('Marks Obtained')
    # total_marks = fields.Integer('Total Marks')
    teacher_id = fields.Many2one('teacher.records','Teachers')
