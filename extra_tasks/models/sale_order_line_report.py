from openerp import tools
from openerp import fields,models,api,_

class special_sale_order_pivot(models.Model):
    _name='special.sale.order.pivot'
    _description = "Sales Orders Statistics"
    _auto = False
    # _rec_name = 'product_id'

    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    price_total = fields.Float('Total Amount', readonly=True)
    qty_invoiced = fields.Float('Total Qty', readonly=True)
    avg_unit_price = fields.Float('Avg. Unit Price', readonly=True)
    internal_code = fields.Char('Default Code',readonly=True)

    # def _select(self):
    #     select_str = """
    #             SELECT distinct(product_id),min(id) as id,
    #             SUM(product_uom_qty * price_unit) AS price_total,
    #             SUM(product_uom_qty) AS qty_invoiced,
    #             SUM(product_uom_qty * price_unit) / SUM(product_uom_qty) AS avg_unit_price
    #        """
    #     return select_str
    #
    # def _from(self):
    #     from_str = """sale_order_line"""
    #     return from_str
    #
    # def _group_by(self):
    #     group_by_str = """
    #            GROUP BY product_id
    #        """
    #     return group_by_str
    #
    # def init(self, cr):
    #     tools.drop_view_if_exists(cr, self._table)
    #     # tools.drop_table
    #     cr.execute("""CREATE or REPLACE VIEW %s as (
    #                %s
    #                FROM %s
    #                %s
    #                )""" % (self._table, self._select(), self._from(), self._group_by()))

    def _select(self):
        select_str = """
                   SELECT distinct(product_id),
                   min(sol.id) as id,
                   pp.default_code AS internal_code,
                   SUM(product_uom_qty * price_unit) AS price_total,
                   SUM(product_uom_qty) AS qty_invoiced,
                   SUM(product_uom_qty * price_unit) / SUM(product_uom_qty) AS avg_unit_price
              """
        return select_str

    def _from(self):
        from_str = """sale_order_line sol inner join product_product pp
        on pp.id = sol.product_id"""
        return from_str

    def _group_by(self):
        group_by_str = """
                  GROUP BY product_id,pp.default_code
              """
        return group_by_str

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        cr.execute("""CREATE or REPLACE VIEW %s as (
                      %s
                      FROM %s
                      %s
                      )""" % (self._table, self._select(), self._from(), self._group_by()))
