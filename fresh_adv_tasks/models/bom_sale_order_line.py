from datetime import datetime
from openerp import fields,models,api,_
from tools import DEFAULT_SERVER_DATETIME_FORMAT


class BoMLine(models.Model):
    _inherit = 'mrp.bom.line'

    is_standard = fields.Boolean('Standard')

class BoMSaleOrder(models.Model):
    _inherit = 'sale.order'

    bom_sale_order_line_id = fields.Many2one('product.product','Product')
    sequence = 0

    @api.multi
    def add_order_line(self):
        oldest_date = datetime.strptime("1990-01-01 00:00:00",DEFAULT_SERVER_DATETIME_FORMAT)
        mrp_bom_id = None
        current_sale_order_id = self._context.get('params')['id']
        product_product_id = self.bom_sale_order_line_id
        get_sale_order_line = self.env['sale.order.line'].search([('order_id','=',current_sale_order_id)])
        get_sale_order_line_length = len(get_sale_order_line)
        product_template_id = self.bom_sale_order_line_id.product_tmpl_id
        mrp_bom_row = self.env['mrp.bom'].search([('product_tmpl_id', '=', product_template_id.id)])
        for each_mrp_bom_row in mrp_bom_row:
            if oldest_date < datetime.strptime(each_mrp_bom_row.write_date,DEFAULT_SERVER_DATETIME_FORMAT):
                oldest_date = datetime.strptime(each_mrp_bom_row.write_date,DEFAULT_SERVER_DATETIME_FORMAT)
                mrp_bom_id = each_mrp_bom_row.id
        if get_sale_order_line_length == 0:
                self.sequence = 1
        else:
            for each_order_line in get_sale_order_line:
                    self.sequence = each_order_line.sequence
            self.sequence = self.sequence + 1
        parent_id = self.env['sale.order.line'].create({
            'order_id': current_sale_order_id,
            'product_id': product_product_id.id,
            'sequence':self.sequence,
            'is_bom_of_product': False,
        })

        mrp_bom_line_row = self.env['mrp.bom.line'].search([('bom_id','=',mrp_bom_id),('is_standard','=',True)])
        for each_mrp_bom_line_row in mrp_bom_line_row:
            if each_mrp_bom_line_row.is_standard == True:
                self.env['sale.order.line'].create({
                    'order_id': current_sale_order_id,
                    'product_id': each_mrp_bom_line_row.product_id.id,
                    'sequence':self.sequence,
                    'is_bom_of_product':True,
                    'is_child_of':parent_id.id
                })

class IsBoMComponentSaleOrderLine(models.Model):
    _inherit ='sale.order.line'

    is_bom_of_product = fields.Boolean("Component")
    is_child_of = fields.Many2one('sale.order.line','Child Of')

    @api.multi
    def unlink(self):
        current_child_id = self.is_child_of
        current_id = self.id
        # obj_sale_order_line = self.env['sale.order.line']
        if not current_child_id:
            # start_duration = datetime.now()
            # print "Start Time",start_duration
            child_lists = self.search([('is_child_of','=',current_id)])
            # end_duration = datetime.now()
            # print "End Time",end_duration
            for each_child in child_lists:
                # print each_child.id
                each_child.unlink()
            # self.reorder_lines()
        # res = super(IsBoMComponentSaleOrderLine, self).unlink()
        # return res

    @api.model
    def reorder_lines(self):
        sequence = 0
        sale_order_id = self.order_id.id
        search_results = self.search([('order_id','=',sale_order_id)])
        for each_search_results in search_results:
            if each_search_results.id == self.id:
                continue
            else:
                if each_search_results.is_bom_of_product == False:
                    sequence = sequence + 1
                    each_search_results.write({'sequence':sequence})
                else:
                    each_search_results.write({'sequence': sequence})





