from openerp import fields,models,api, _
from openerp.exceptions import except_orm

class ResUsers(models.Model):
    _inherit = ['res.users']

    def calculate_commission(self):
        print True

    commission = fields.Float("Commission",default='1.0')

    # @api.onchange('commission')
    # def on_commission_change(self):
        # if self.commission > 5:
        #     raise except_orm("Warning", "Commission cannot be more than 5%")
        # elif self.commission < 1:
        #     raise except_orm("Warning", "Commission cannot be less than 1%")
        # if self.commission < 1:
        #     raise except_orm("Warning", "Commission cannot be less than 1%")

    @api.model
    def create(self,vals):
        res = super(ResUsers,self).create(vals)
        print "Create Commission Context",self._context
        print "Create Commission Vals",vals

        if vals['commission'] > 0:
            curr_commission = vals['commission']
            if curr_commission > 5:
                raise except_orm("Warning", "Commission cannot be more than 5%")
            elif curr_commission < 1:
                raise except_orm("Warning", "Commission cannot be less than 1%")
        return res

    @api.multi
    def write(self,vals):
        print"vals['commission']****",vals['commission'], type(vals['commission'])
        print "Write Commission Context", self._context
        print "Write Commission Vals", vals
        if vals['commission'] > 5.0:
            # curr_commission = vals['commission']
            # if curr_commission > 5.0:
            raise except_orm("Warning", "Commission cannot be more than 5%")
        elif vals['commission'] < 1.0:
            raise except_orm("Warning", "Commission cannot be less than 1%")
        res = super(ResUsers, self).write(vals)
        return res

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

# Not Working Already Tried
class MailThread(models.Model):
    _name ='res.users'
    _inherit = ['mail.thread']