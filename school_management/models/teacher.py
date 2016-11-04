import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8

class student(models.Model):
    _name = 'teacher'
    
    name = fields.Char('Name', required=1)
    address = fields.Text('Address')
    pincode = fields.Char('Pincode')
    telephone = fields.Char('Telephone')
    birthdate = fields.Date('Birthdate')
    joindate = fields.Datetime('Join Date')
    active = fields.Boolean('Active',  default=1)

    def active_action(self):
        print self