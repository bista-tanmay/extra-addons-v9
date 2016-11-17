from openerp import models, fields, api,_
from openerp.osv import osv
from openerp.osv import expression


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    extra_notes = fields.Text('Extra Notes')

    # def get_context_sale_orders(self,cr, uid, ids=None, context=None):
    #     print "Inside get_sale_orders Method"
    #     print context
    #     print self
    #     cr.execute("select so.name,so.amount_total from sale_order so inner join sale_order_line sl on so.id = sl.order_id GROUP BY so.name,so.amount_total HAVING count(sl.order_id) > 2 AND so.amount_total > 100")
    #     results = cr.dictfetchall()
    #     print results
    #     for each in results:

    # result = {
    #     'view_type': 'form',
    #     'view_mode': 'form',
    #     'res_model': 'sale.order',
    #     # 'views': [(view_id, 'form')],
    #     'view_id': False,
    #     'type': 'ir.actions.act_window',
    #     'target': 'new',
    #     'res_id': False,
    #     'domain':
    # }
    # return result

    # def name_get(self, cr, uid, ids, context=None):
    #     # print "Context",context
    #     context = dict(context or {})
    #     # print "Curr Context", context
    #     curr_show_sale = context.get('show_sale') or False
    #     # print curr_show_sale
    #     curr_sale_state = False
    #     # print context
    #     if (curr_show_sale):
    #         # curr_sale_state = True
    #         context.update({'curr_state':True})
    #         # print context
    #     else:
    #         context.update({'curr_state': False})
    #         # print context
    #     # print context
    #     # curr_state = False
    #     # return curr_state
    #     return super(SaleOrderInherit, self).name_get(cr, uid, ids, context=context)

# class ResPartner(models.Model):
#     _inherit = 'res.partner'

    # @api.model
    # def create(self,vals):
    #     print "Create Self", self
    #     print "Res Partner Create vals", vals
    #     return super(ResPartner, self).create(vals)
    #
    # @api.multi
    # def write(self,vals):
    #     print "Write Self Context",self._context
    #     print "Res Partner Write vals", vals
    #     return super(ResPartner,self).write(vals)
    #
    # @api.model
    # def default_get(self):
    #     print "Default Self",self
    #
    # def name_get(self,cr, uid, ids, context):
    #     print "Name Get",self
    #     return super(ResPartner, self).name_get(cr, uid, ids, context=context)

    # def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
    #     print "name_search self",self
    #     print "name_search context",context
    #
    # def read(self, cr, uid, ids, fields=None, context=None, load='_classic_read'):
    #     print "read self",self
    #     print "read context", context
    #     return super(ResPartner, self).read(cr, uid, ids, fields=fields, context=context, load=load)

class SaleOrderInheritView(models.Model):
    _name = 'sale.order.inherit.new'
    # _rec_name = 'sale_order_name'

    # To create new model without sale order form views
    # sale_order_name = fields.Char('Sale Order')
    # sale_order_amount = fields.Float('Total Amount')
    # nos = fields.Integer('No. Of Order Lines')

    @api.multi
    def get_context_sale_orders(self):
        # self.env.cr.execute("delete from sale_order_inherit_new")
        self.env.cr.execute("select so.name,so.amount_total, count(sl.order_id) as Nos from sale_order so inner join sale_order_line sl on so.id = sl.order_id GROUP BY so.name,so.amount_total HAVING count(sl.order_id) > 10 AND so.amount_total > 1000")
        results = self.env.cr.dictfetchall()
        # sale_order_ids = []
        sale_order_names = []
        for each_sale_order in results:
            # Creates new records in new model
            # new_id = self.create({
            #     'sale_order_name':each['name'],
            #     # 'sale_order_amount':each['amount_total'],
            #     # 'nos':each['nos']
            # })

            # sale_order_ids.append(new_id.id)
            sale_order_names.append(each_sale_order['name'])
        return {'name': _("Sale Order"),
                'view_mode': 'tree,form',
                'res_id': False,
                'view_type': 'form',
                'res_model': 'sale.order',
                'type': 'ir.actions.act_window',
                'nodestroy': False,
                'view_id': False,
                'target': 'current',
                # 'domain': "[('id','in',%s)]" % sale_order_ids
                'domain': "[('name','in',%s)]" % sale_order_names
                }

class ResCountry(models.Model):
    _inherit = 'res.country'

    @api.multi
    def name_get(self):
        print "name_get Method Called"
        print "name_get self",self
        return super(ResCountry,self).name_get()

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        print "name_search Method Called"
        print "name_search self", self
        if name:
            domain = ['|', ('code', '=ilike', name + '%'), ('name', operator, name)]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = ['&', '!'] + domain[1:]
        country = self.search(domain + args, limit=limit)
        return country.name_get()

    @api.multi
    def write(self,vals):
        print "Write self",self
        print "Write vals",vals
        return super(ResCountry,self).write(vals)
