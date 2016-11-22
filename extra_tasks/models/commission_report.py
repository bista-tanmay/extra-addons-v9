from openerp import fields,models,api, _
from openerp.exceptions import except_orm
from openerp import tools

class ResUsers(models.Model):
    _name ='res.users'
    _inherit = ['res.users','mail.thread']

    def calculate_commission(self):
        print True

    commission = fields.Float("Commission",default='1.0')

    @api.model
    def create(self,vals):
        res = super(ResUsers,self).create(vals)
        if vals['commission'] > 5.0:
            raise except_orm("Warning", "Commission cannot be more than 5%")
        elif vals['commission'] < 1.0:
            raise except_orm("Warning", "Commission cannot be less than 1%")
        return res

    # The operations in this method prevents creation of users
    # Logging Mail Message through user id will prevent creation of res.users
    # @api.multi
    # def write(self,vals):
    #     res = super(ResUsers, self).write(vals)
    #     user_id = self._context.get('params')['id']
    #     if vals['commission'] > 5.0:
    #         raise except_orm("Warning", "Commission cannot be more than 5%")
    #     elif vals['commission'] < 1.0:
    #         raise except_orm("Warning", "Commission cannot be less than 1%")
    #     user_details = self.env['res.users'].browse(user_id)
    #     log_message = _('Commission changed for %s from %s ->> %s' % (self.name, self.commission, vals['commission']))
    #     get_message_post_id = user_details.message_post(body=log_message, type='comment', author_id=user_details.partner_id.id, attachments=[])
    #     # Check if message_post exists
    #     if get_message_post_id:
    #         self.env['mail.message'].browse(get_message_post_id).write({'res_id': user_details, 'model': 'res.users'})
    #         # get_message_post_id.write({'res_id': user_details, 'model': 'res.users'})
    #     return res

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commission = fields.Float("Commission")

    @api.model
    def create(self,vals):
        user_id = vals['user_id']
        get_user_commission = self.env['res.users'].browse(user_id)
        vals['commission'] = get_user_commission.commission
        res = super(SaleOrder, self).create(vals)
        return res

