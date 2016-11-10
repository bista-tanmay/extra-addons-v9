from openerp import fields,models,api, _
from openerp.exceptions import except_orm
from openerp import tools

class ResUsers(models.Model):
    _name ='res.users'
    _inherit = ['res.users','mail.thread']

    def calculate_commission(self):
        print True

    commission = fields.Float("Commission",default='1.0')

    # @api.model
    # def create(self,vals):
    #     res = super(ResUsers,self).create(vals)
    #     print "Create Commission Context",self._context
    #     print "Create Commission Vals",vals
    #
    #     if vals['commission'] > 5.0:
    #         # curr_commission = vals['commission']
    #         # if curr_commission > 5.0:
    #         raise except_orm("Warning", "Commission cannot be more than 5%")
    #     elif vals['commission'] < 1.0:
    #         raise except_orm("Warning", "Commission cannot be less than 1%")
    #     return res

    # @api.multi
    # def write(self,vals):
    #     user_id = self._context.get('params')['id']
    #     if vals['commission'] > 5.0:
    #         raise except_orm("Warning", "Commission cannot be more than 5%")
    #     elif vals['commission'] < 1.0:
    #         raise except_orm("Warning", "Commission cannot be less than 1%")
    #     my_id = self.env['res.users'].browse(user_id)
    #     print "my_id",my_id
    #     log_message = _('Commission changed for %s i.e %s ->> %s' % (self.name, self.commission, vals['commission']))
    #     get_message_post_id = my_id.message_post(body=log_message, type='comment', author_id=my_id.partner_id.id, attachments=[])
    #     # print "get_message_post_id", get_message_post_id
    #     if get_message_post_id:
    #         get_message_post_id.write({'res_id': user_id, 'model': 'res.users'})
    #     res = super(ResUsers, self).write(vals)
    #     return res

    # Ojas Ka Code
    @api.multi
    def write(self, vals):
        # print "FIELDS WRITE=============================="
        var = vals.get('commission', 0)
        # print "FIELDS WRITE=====================", var
        if var >= 1 and var <= 5:
            pass
        else:
            raise except_orm(_("Values Should be Between 1 to 5 Only!!!"))
        # print "SELF===============================", self.commission_field
        # print "SELF===============================", self.name
        # print "VALS===============================", vals['commission_field']
        # print "CONTXT========================", self._context.get('params')['id']
        my_id = self._context.get('params')['id']
        record_id = self.env['res.users'].browse(my_id)
        # print "record", record_id
        log_message = _('Options changed for %s i.e %s ->> %s' % (self.name, self.commission, vals['commission']))
        a = record_id.message_post(body=log_message, type='comment', author_id=record_id.partner_id.id, attachments=[])
        print "a", a
        if a:
            a.write({'res_id': my_id, 'model': 'res.users'})
        return super(ResUsers, self).write(vals)
    # Ojas Ka Code

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commission = fields.Float("Commission")

    @api.model
    def create(self,vals):
        print "Commission Sale Order vals['user_id']",vals['user_id']
        # print self._context
        # print self
        # print vals
        user_id = vals['user_id']
        get_user_commission = self.env['res.users'].browse(user_id)
        vals['commission'] = get_user_commission.commission
        res = super(SaleOrder, self).create(vals)
        return res
#
# Not Working Already Tried
# class MailThread(models.Model):
#     _inherit = ['mail.thread']

