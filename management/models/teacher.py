import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8

class teacher(models.Model):
    _name = 'teacher'

    name = fields.Char('Name', required=1)
    address = fields.Text('Address')
    pincode = fields.Char('Pincode')
    telephone = fields.Char('Telephone')
    birthdate = fields.Date('Birthdate')
    joindate = fields.Datetime('Join Date')
    subject_ids = fields.Many2many('subject','teacher_subject_rel','teacher_id','subject_id','Subjects')
    active = fields.Boolean('Active', default=1)

    @api.multi
    def active_action(self):
        if self.active:
            self.write({'active': False})
        elif not self.active:
            self.write({'active': True})
        else:
            self.write({'active': True})
        print "Is Active", self.active
