from openerp import models, fields, api

class download_attachment(models.Model):
    _inherit = 'ir.attachment'

    is_help = fields.Boolean('Is Help Attachment?')