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

class ResPartner(models.Model):
    _inherit = 'res.partner'


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

    def name_get(self,cr, uid, ids, context):
        curr_code = []
        # We get context while editing a res.partner model record
        # While the record is being edited we keep the country names intact
        if context.get('c_id',False):
            # We browse through all records while
            # setting the the id and country name
            for each_country in self.browse(cr, uid, ids, context):
                curr_code.append((each_country.id,each_country.name))
        else:
            # Once we loose the context we replace
            # the name with country code while passing id with it
            # i.e. we pass id and country code
            for each_country in self.browse(cr, uid, ids, context):
                curr_code.append((each_country.id,each_country.code))
        return curr_code
