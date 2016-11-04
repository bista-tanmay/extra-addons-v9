import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression # V7
from openerp import models, fields, api, _ # v8
from openerp.exceptions import except_orm,UserError, ValidationError

class result_wizard(models.TransientModel):
    _name = 'result.wizard'
    _description = 'New Description'

    name = fields.Char('Name')
    standard = fields.Selection([('first', '1st'), ('second', '2nd'), ('third', '3rd'), ('fourth', '4th'), ('fifth', '5th'), ('sixth', '6th'), ('seventh', '7th'), ('eight', '8th'), ('ninth', '9th'), ('tenth', '10th')], 'Standard.')
    division = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], 'Division.')
    roll_no = fields.Integer('Roll No')
    birth_date = fields.Date('Date Of Birth')
    fees_amt = fields.Float('Fees')
    subject_ids = fields.Many2many('subject.records', 'student_subject_rel', 'subject_id', 'student_id', 'Subjects')

    # student_subject_ids = fields.One2many('result.wizard.data', 'wiz_id', 'Subjects')

    # @api.model
    # def default_get(self,fields_list):
    #     curr_active_model = self._context.get('active_model')
    #     curr_active_id = self._context.get('active_id')
    #     stud_details = self.env['student.records'].browse(curr_active_id)
    #     wiz = self.env['result.wizard'].create({'name': stud_details.name,
    #                                             'standard': stud_details.standard,
    #                                             'division': stud_details.division,
    #                                             'roll_no': stud_details.roll_no,
    #                                             'birth_date': stud_details.birth_date,
    #                                             'fees_amt': stud_details.fees_amt})
    #     for line in self.subject_ids:
    #         vals = {}
    #         vals.update({'name': line.name,
    #                      'marks_obtained': line.marks_obtained,
    #                      'wiz_id': wiz.id
    #                      })
    #         self.env['result.wizard.data'].create(vals)
    #
    #     return {
    #         'name': _('Results'),
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'res_model': 'result.wizard',
    #         'res_id': wiz.id,
    #         'type': 'ir.actions.act_window',
    #         'target' : 'new',
    #     }
