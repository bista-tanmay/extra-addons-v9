from openerp import models, fields, api, _
from openerp.exceptions import except_orm


class student_records(models.Model):
    _name = 'student.records'

    # Only useful when there is no name field defined. By default odoo recognizes a name field from our model.
    # _rec_name = 'name'

    _description = 'Student Records'

    # Name field as a Character type field
    name = fields.Char('Name',required='True')
    # Standard field as a Selection type field
    standard = fields.Selection([('first', '1st'), ('second', '2nd'), ('third', '3rd'), ('fourth', '4th'), ('fifth', '5th'), ('sixth', '6th'), ('seventh', '7th'), ('eight', '8th'), ('ninth', '9th'), ('tenth', '10th')], 'Standard.')
    division = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], 'Division.')

    # Roll No field as a Integer type field
    roll_no = fields.Integer('Roll No')
    # Birth Date field as a Date type field
    birth_date = fields.Date('Date Of Birth')
    # Birth Date field as a Date type field
    fees_amt = fields.Float('Fees')
    # Subject IDs field as a One to Many type field
    # Syntax: fields.One2many('opposite.model.name','many2one_field_name_in_opposite_model','string that appears in UI')
    subject_ids = fields.One2many('subject.records', 'student_id', 'Subjects')

    # Subject IDs field as a Many to Many type field
    # Syntax: fields.Many2many('opposite.model.name','current_model_opposite_model_rel','opposite_model_id_field_name','current_model_id_field_name','string that appears in UI')
    # subject_ids = fields.Many2many('subject.records', 'student_subject_rel', 'subject_id', 'student_id', 'Subjects')

    _defaults = {
        'standard': 'first',
        'division': 'a',
    }

    # Model decorator used when records/rows are not present in database. Used in create and default_get methods
    @api.model
    # Called on save operation after create is clicked.
    def create(self, vals):
        # Check if name has value or empty
        if vals.get('name', False):
            # Loop through all elements in name
            for obj in vals.get('name'):
                # Check if element is character not a digit
                if obj.isalpha():
                    # Do nothing
                    pass
                else:
                    # Raise exception if user is trying to input numeric values in character fields
                    raise except_orm("Warning", "You are not allowed to enter numbers in name field")
        # Call the parent class create method & pass all current values to it.
        return super(student_records, self).create(vals)

    # Multi decorator used when operation needs to be performed on multiple rows or ids.
    @api.multi
    # Called on save operation after edit is clicked.
    def write(self, vals):
        # Check if name has value or empty
        if vals.get('name', False):
            # Loop through all elements in name
            for obj in vals.get('name'):
                # Check if element is character not a digit
                if obj.isalpha():
                    # Do nothing
                    pass
                else:
                    # Raise exception if user is trying to input numeric values in character fields
                    raise except_orm("Warning", "You are not allowed to enter numbers in name field")
        # Call the parent class write method & pass all current values to it.
        return super(student_records, self).write(vals)

    # Opening & passing values to wizard on method call on button type object.
    # @api.multi
    # def show_result(self):
    #     wiz = self.env['result.wizard'].create({'name': self.name,
    #                                             'standard': self.standard,
    #                                             'division': self.division,
    #                                             'roll_no': self.roll_no,
    #                                             'birth_date': self.birth_date,
    #                                             'fees_amt': self.fees_amt,
    #                                             'subject_ids': self.subject_ids})
    #     # for line in self.subject_ids:
    #     #     vals = {}
    #     #     vals.update({'name': line.name,
    #     #                  'marks_obtained': line.marks_obtained,
    #     #                  'wiz_id': wiz.id
    #     #                  })
    #     #     self.env['result.wizard.data'].create(vals)
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