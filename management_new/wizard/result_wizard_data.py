import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8
from openerp.exceptions import except_orm,UserError, ValidationError

class result_wizard_data(models.TransientModel):
    _name = 'result.wizard.data'
    _description = 'New Description'

    wiz_id = fields.Many2one('result.wizard', 'Wizard')
    name = fields.Char('Subject Name')
    marks_obtained = fields.Integer('Marks Of Student:')



