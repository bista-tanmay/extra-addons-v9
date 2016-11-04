import base64
from zipfile import ZipFile

from openerp.exceptions import except_orm,UserError, ValidationError
from openerp import models, fields, api, _ # v8



class help_wizard(models.TransientModel):
    _name = 'help.wizard'

    models_id = fields.Many2one('ir.model',string='Models')
    data = fields.Binary('File')
    name = fields.Char('File Name', readonly=True)
    attachments = fields.One2many('help.wizard.data', 'help_wizard_id', 'Attachments')

    @api.multi
    def download_all_docs(self):
        self.env['help.wizard.data'].search([('attachment_name', '!=', '')]).unlink()
        res = self.env['ir.attachment'].search(['&', ('res_model', '=', self.models_id.model),('is_help','=',True)])
        if not res:
            raise except_orm(_("Warning"), ("No attachments found for %s model" % self.models_id.model))

        for each_attach in res:
            file_name = each_attach.name
            self.env['help.wizard.data'].create(
                {'help_wizard_id': self.id, 'attachment_name': file_name,
                 'attachment_data': each_attach.datas,
                 })

        with ZipFile('/home/bista/Documents/Downloads/all-attachments.zip', 'w') as myzip:
            for each in res:
                file_datas = base64.b64decode(each.datas)
                each_file = open(each.name, "w")
                each_file.write(file_datas)
                each_file.close()
                # print file.name
                myzip.write(str(each_file.name))
        file_open = open('/home/bista/Documents/Downloads/all-attachments.zip', "rb+")
        encode_zip = base64.encodestring(file_open.read())
        self.write({'data': encode_zip,'name': 'all-documents.zip'})

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'help.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(False, 'form')],
            'target': 'new',
        }
