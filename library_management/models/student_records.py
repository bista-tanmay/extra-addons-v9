from openerp import fields, models, api, _
from datetime import datetime


class StudentRecords(models.Model):
    _name = 'student.records'

    @api.model
    def create(self, vals):
        if vals.get('roll_no',1) == 1:
            vals['roll_no'] = self.env['ir.sequence'].next_by_code('studentrecords')
        res = super(StudentRecords, self).create(vals)
        return res

    profile_pic = fields.Binary('Profile Pic')
    name = fields.Char('Student Name')
    user_id = fields.Many2one('res.users','User')
    roll_no = fields.Integer('Roll No', copy=False,default=1,readonly=True)
    course_ids = fields.Many2one('course.records','Course Opted')
    subject_ids = fields.One2many('subject.records','course_id','Subjects',related='course_ids.subject_ids')
    birth_date = fields.Date('Birth Date')
    age = fields.Char('Age')

    @api.onchange('birth_date')
    def on_birth_date_change(self):
        birth_date = datetime.strptime(self.birth_date or '2001-01-01', "%Y-%m-%d")
        today = datetime.now().year
        diff = today - birth_date.year
        self.age = str(diff)
