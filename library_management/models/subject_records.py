from openerp import fields, models, api, _


class SubjectRecords(models.Model):
    _name = 'subject.records'

    name = fields.Char('Name',size=50)
    marks_obtained = fields.Integer('Marks Obtained',digits=(2,0))
    course_id = fields.Many2one('course.records','Courses')

