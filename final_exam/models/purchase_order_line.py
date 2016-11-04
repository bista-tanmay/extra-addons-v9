from openerp import models, fields, api,_
from openerp.exceptions import except_orm,UserError, ValidationError
import re

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_type = fields.Selection([('product', 'Product'),('service', 'Service'),('consu', 'Consumable')], 'Product Type')

    @api.onchange('product_id')
    def onproductid_change(self):
        prod_id = self.product_id.id
        search_results = self.env['product.product'].browse(prod_id)
        template_id = search_results.product_tmpl_id.id
        template_search = self.env['product.template'].browse(template_id)
        self.product_type = template_search.type

class sale_order(models.Model):
    _inherit = 'sale.order'

    def _cal_weight(self):
        total_weight = 0
        for each in self.order_line:
            total_weight = total_weight + each.product_id.weight * each.product_uom_qty
            self.total_weight = total_weight

    @api.onchange('partner_id')
    def onpartnerid_change(self):
        print self._context
        print self.partner_id.company_type
        company_type = self.partner_id.company_type
        print company_type
        if company_type == 'company':
            self.is_company = True
        else:
            self.is_company = False

    total_weight = fields.Char('Total Weight',compute='_cal_weight')
    is_company = fields.Boolean('Is Company')

    def view_order_line_wizard(self):
        return True

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def check_email(self,email):
        email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$)")
        if not email_regex.match(email):
            raise except_orm(_("Warning"), "Email is not valid")
        else:
            pass

    def check_number(self,number):
        mobile_regex = re.compile(r'^[91]+([0-9]{8})$')
        if not mobile_regex.match(number):
            raise except_orm(_("Warning"), "Mobile is not valid")
        else:
            pass

    @api.model
    def create(self, vals):
        if vals.get('email', False):
            email = vals.get('email', False)
            self.check_email(email)
        if vals.get('mobile', False):
            mobile = vals.get('mobile', False)
            self.check_number(mobile)
        return super(ResPartner,self).create(vals)

    @api.multi
    def write(self, vals):
        print vals
        if vals.get('email', False):
            email = vals.get('email', False)
            self.check_email(email)
        if vals.get('mobile', False):
            mobile = vals.get('mobile', False)
            self.check_number(mobile)
        return super(ResPartner, self).write(vals)

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    states = fields.Selection([('new', 'New'),('probation', 'Probation'),('confirmed', 'Confirmed'),('terminated', 'Terminated'),('resigned', 'Resigned')], 'State', readonly=False)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def unlink(self):
        if self.amount_total > 10000:
            raise except_orm(_("Warning"), ("Your invoice amount is greater than 10000 therefore cannot be deleted"))
        else:
            pass
        return super(AccountInvoice,self).unlink()

class SaleOrderLineWizard(models.TransientModel):
    _name = 'sale.order.line.wizard'
    _defaults = {
        'product_qty': 1,
    }

    product_id = fields.Many2one('product.product',string='Product')
    product_qty = fields.Integer('Quantity')
    unit_price = fields.Integer('Unit Price')

    @api.multi
    def add_sale_order_line(self):
        print "Self",self._context
        print self.product_id.id
        print self._context.get('active_id')
        current_view_id = self._context.get('active_id')
        current_product_qty = self.product_qty
        if current_product_qty > 0:
            pass
        else:
            current_product_qty = 1
        self.env['sale.order.line'].create({
            'product_id': self.product_id.id,
            'order_id': current_view_id,
            'product_uom_qty': current_product_qty,
            'price_unit': self.unit_price,
        })

    @api.onchange('product_id')
    def _onchange_product_id(self):
        # print self._context
        # print self.product_id.id
        search_qty = self.env['product.product'].browse(self.product_id.id)
        # print search_qty.list_price
        self.unit_price = search_qty.list_price


