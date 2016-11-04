import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8

class subject(models.Model):
    _name = 'subject'
    
    name = fields.Char('Name', required=1)
    lectures_required = fields.Integer('Lectures Required')
    teacher_ids = fields.Many2many('teacher','teacher_subject_rel','subject_id','teacher_id','Teachers')