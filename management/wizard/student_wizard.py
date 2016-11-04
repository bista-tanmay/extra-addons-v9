from openerp import fields, models, api, _

class student_wizard(models.TransientModel):
    _name = 'student.wizard'

    name = fields.Char("Student Name")
    roll_no = fields.Integer("Student Roll No")
    english = fields.Integer("English Marks")
    marathi = fields.Integer("marathi Marks")
    hindi = fields.Integer("hindi Marks")
    science = fields.Integer("science Marks")
    achievement_ids = fields.One2many('student.wizard.data', 'student_wizard_id', 'Achievements')

    @api.depends('english', 'marathi','hindi','science')
    def _compute_marks(self):
        for record in self:
            record.total_marks = record.english + record.marathi + record.hindi + record.science
            record.average_percent = (record.total_marks * 100) / 600

    total_marks = fields.Integer(string="Total Marks", compute='_compute_marks')
    average_percent = fields.Float(string="Average Percentage %", compute='_compute_marks')

    @api.model
    def create(self, vals):
        print self._context
        print vals
        print "Self", self
        # print "Self Conte..xt In Create Of Wizard",self._context
        # print "Self In Create Of Wizard",self
        # print "Vals In Create Of Wizard",vals
        # print "Button Context", self.env['student.wizard']._context
        # wiz = self.env['student.wizard'].get('wiz_id')
        # my_context = self.env['student.wizard']._context.copy()
        # my_context.update({'wiz_id': wiz.id})
        # 'context': my_context,
        return super(student_wizard,self).create(vals)



