from openerp import tools
from openerp.osv import fields,osv

class special_sale_order_pivot(osv.osv):
    _name='special.sale.order.pivot'
    _description = "Sales Orders Statistics"
    _auto = False
    _rec_name = 'product_id'

    _columns = {
        'product_id': fields.many2one('product.product', 'Product', readonly=True),
        'price_total': fields.float('Total Amount', readonly=True),
        'qty_invoiced': fields.float('Total Qty', readonly=True),
        'avg_unit_price': fields.float('Avg. Unit Price', readonly=True),
    }

    def _select(self):
        select_str = """
                SELECT distinct(product_id),min(id) as id,
                SUM(product_uom_qty * price_unit) AS price_total,
                SUM(product_uom_qty) AS qty_invoiced,
                SUM(product_uom_qty * price_unit) / SUM(product_uom_qty) AS avg_unit_price
           """
        return select_str

    def _from(self):
        from_str = """sale_order_line"""
        return from_str

    def _group_by(self):
        group_by_str = """
               GROUP BY product_id
           """
        return group_by_str

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        # tools.drop_table
        cr.execute("""CREATE or REPLACE VIEW %s as (
                   %s
                   FROM %s
                   %s
                   )""" % (self._table, self._select(), self._from(), self._group_by()))
