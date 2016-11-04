from openerp import models
from openerp import api, _
from openerp.tools import float_compare, float_is_zero
from openerp import workflow, fields


class Teacher(models.Model):
    _name = 'college.teacher'
    name = fields.Char('Name')
    salary = fields.Float('Salary')

class Student(models.Model):
    _name = 'college.student'
    name = fields.Char('Name')
    roll_no = fields.Integer('Roll NO')
    subject = fields.Char('Subject')
