from openerp.osv import osv
from openerp.report import report_sxw



class CommissionReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(CommissionReport, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
                    'get_commission':self.get_commission,
            })

    def get_commission(self):
        get_user_details = self.pool.get('res.users').browse(self.cr, self.uid, self.localcontext['active_ids'])
        # Current User for whom the report is being printed
        user_name = get_user_details.partner_id.name
        # Get all sale order related to user above
        get_all_saleorders = self.pool.get('sale.order').search(self.cr, self.uid,
                                                                [('user_id', '=', self.localcontext['active_ids']),
                                                                 ('state', '=', 'done')])
        # Initialize an empty list
        single_sale_order_row = []
        # Loop through each sale order result set i.e. set returned by search query
        for each_sale_order in get_all_saleorders:
            # Get Single Sale Order Details
            get_sale_order_details = self.pool.get('sale.order').browse(self.cr, self.uid, each_sale_order)
            # Sale Order Name E.g. SO010
            sale_order_name = get_sale_order_details.name
            # Total Sale Order Amount
            sale_order_total_amount = get_sale_order_details.amount_total
            # Percentage Commission per Sale Order
            commission_per_sale_order = get_sale_order_details.commission
            # Commission Amount per Sale Order
            curr_commission_amount = (get_sale_order_details.amount_total * commission_per_sale_order) / 100
            # Append each value to a list in order to form a single row of values
            single_sale_order_row.append({'Username':user_name,'SaleOrder':sale_order_name,'SaleOrderAmount':sale_order_total_amount,'CurrCommission':curr_commission_amount})
        # Return the list
        return single_sale_order_row


class ReportManagementQweb(osv.AbstractModel):
    # name must be report.module_name.template_id
    _name ='report.extra_tasks.report_res_users_commission'
    _inherit = 'report.abstract_report'
    _template = 'extra_tasks.report_res_users_commission'
    _wrapped_report_class = CommissionReport