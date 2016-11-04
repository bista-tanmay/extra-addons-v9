from openerp import fields, models, api

class help_wizard_data(models.TransientModel):
    _name = "help.wizard.data"

    help_wizard_id = fields.Many2one('help.wizard')
    attachment_name = fields.Char("Name")
    attachment_data = fields.Binary('Attachments')

