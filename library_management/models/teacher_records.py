from openerp import fields, models, api, _


class TeacherRecords(models.Model):
    _name = 'teacher.records'

    profile_pic = fields.Binary('Profile Pic')
    name = fields.Char('Teacher Name')
    subject_id = fields.Many2one('subject.records','Subject')
    course_id = fields.Many2one('course.records','Course',related='subject_id.course_id')