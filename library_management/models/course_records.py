from openerp import fields, models, api, _


class CourseRecords(models.Model):
    _name = 'course.records'

    name = fields.Char('Name',size=50)
    duration = fields.Float('Duration (in Months)',digits=(2,0),size=2)
    subject_ids = fields.One2many('subject.records','course_id','Subjects')

