from openerp import models, fields, api, _

class TeacherRecords(models.Model):
    _name = 'teacher.records'

    name = fields.Char('Name', required='True')
    subject_ids = fields.One2many('subject.records','teacher_id','Subjects')