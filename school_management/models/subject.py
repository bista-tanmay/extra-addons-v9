import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8

class student(models.Model):
    _name = 'subject'
    
    name = fields.Char('Name', required=1)
    lectures_required = fields.Integer('Lectures')
    active = fields.Boolean('Active',  default=1)