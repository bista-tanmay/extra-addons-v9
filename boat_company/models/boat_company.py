from openerp import models, fields, api, _

class ProductTemplate(models.Model):

    _inherit = 'product.template'

    boat_length = fields.Char('Boat Length',size=10)
    fuel_capacity = fields.Char('Fuel Capacity',size=10)
    model_options_id = fields.Many2one('product.category','Model Options')
    variant_group_id = fields.Many2one('product.variant.group','Variant Group')

class ProductProduct(models.Model):

    _inherit = "product.product"

    def _search(self, cr, user, args, offset=0, limit=None, order=None, context=None, count=False,
                access_rights_uid=None):
        if context is None:
            context = {}
        if context.get('boat_model_id'):
            local_boat_model_id = context.get('boat_model_id')
            # context: {u'lang': u'en_US', u'tz': False, u'uid': 1, u'boat_model_id': id}
            # where id is an integer i.e. id saved in product.template
            if local_boat_model_id:
                product_obj = self.pool.get('product.template').browse(cr, user, [local_boat_model_id], context=context)
                # product_obj: product.template(id,) where id is an integer
                # Using product_obj we can access other fields in product.template
                # e.g. product_obj.list_price which price of the Boat Model.
                args = [('categ_id', '=', product_obj['model_options_id'].id)] + args
                # print product_obj['model_options_id'].id
                # print product_obj['boat_length']
                # print product_obj['fuel_capacity']
                # print product_obj['type']
                # args: [('categ_id', '=', id), [u'sale_ok', u'=', True]]
                # where id is an integer i.e. id saved in product.category
        return super(ProductProduct, self)._search(cr, user, args, offset=offset, limit=limit, order=order,context=context, count=count, access_rights_uid=access_rights_uid)


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    # boat_model_id = fields.Many2one('product.template',"Boat Model",domain=[('categ_id.name','=','Boat Models')])
    boat_model_id = fields.Many2one('product.template',"Boat Model",domain=[('categ_id.name','=','Boat Models')])

class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    variant_id = fields.Many2one('product.variant',"Variant")

class ProductVariantGroup(models.Model):

    _name = 'product.variant.group'

    name = fields.Char('Variant Group',size=64)
    description = fields.Text('Description')
    variants = fields.One2many('product.variant','variant_group_id','Variants')


class ProductVariant(models.Model):
    _name = 'product.variant'

    name = fields.Char('Variant', size=64)
    description = fields.Text('Description')
    variant_group_id = fields.Many2one('product.variant.group','Variant Group')

    def _name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100, name_get_uid=None):
        if context is None:
            context = {}
        if context.get('product_lookup'):
            product_look_up = context.get('product_lookup')
            product_obj = self.pool.get('product.product').browse(cr, user, [product_look_up], context=context)

            # In Openerp v7 we get error if variant_group_id is False
            # To counter it we specify this if...else condition
            # if product_obj['variant_group_id']:
            #     args = [('variant_group_id', '=', product_obj['variant_group_id'].id)] + args
            # else:
            #     args = [('variant_group_id', '=', 0)] + args

            # For Odoo v8, the method has already handled this exception
            args = [('variant_group_id', '=', product_obj['variant_group_id'].id)] + args

        return super(ProductVariant,self)._name_search(cr, user, name=name, args=args, operator=operator, context=context, limit=limit, name_get_uid=name_get_uid)