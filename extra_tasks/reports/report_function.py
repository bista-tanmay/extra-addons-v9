from openerp.osv import osv
from openerp.report import report_sxw
from datetime import datetime

from pytz import timezone


class CommissionReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(CommissionReport, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
                    'get_commission':self.get_commission,
            })

    # def get_commission(self):
    #     # print "get_commission self._context in report_function.py",self.localcontext
    #     # get_partner_id = self.pool.get('res.users').browse(self.cr, self.uid, self.localcontext['active_ids'])
    #     # print get_partner_id
    #     get_user_details = self.pool.get('res.users').browse(self.cr, self.uid, self.localcontext['active_ids'])
    #     print get_user_details
    #     user_name = get_user_details.partner_id.name
    #     print user_name
    #     # Save partner ID in variable
    #     # partner_id = get_partner_id.partner_id.id
    #     # get_user_id =
    #     # print partner_id
    #     get_all_saleorders = self.pool.get('sale.order').search(self.cr, self.uid,[('user_id', '=', self.localcontext['active_ids']),('state','=','done')])
    #     total_commission = 0
    #     sale_order_total_amount_sum = 0
    #     single_sale_order_row = ''
    #     for each_sale_order in get_all_saleorders:
    #         get_sale_order_details = self.pool.get('sale.order').browse(self.cr, self.uid, each_sale_order)
    #         print get_sale_order_details.name
    #         sale_order_name = get_sale_order_details.name
    #         print "Amount Total", get_sale_order_details.amount_total
    #         sale_order_total_amount = get_sale_order_details.amount_total
    #         sale_order_total_amount_sum = sale_order_total_amount_sum + sale_order_total_amount
    #         print "Commission Value",  get_user_details.commission
    #         commission = (get_sale_order_details.amount_total * get_user_details.commission)/100
    #         print "Commission",commission
    #         curr_commission = commission
    #         total_commission = total_commission + commission
    #         single_sale_order_row = single_sale_order_row + "<tr><td>"+user_name+"</td><td>"+sale_order_name+"</td><td>" + str(sale_order_total_amount) + "</td><td>" + str(curr_commission) + "</td></tr>"
    #     return single_sale_order_row + "<tr><td colspan='2'><b>Total Sale Order Amount</b></td><td colspan='2'>"+str(sale_order_total_amount_sum)+"</td></tr><tr><td colspan='2'><b>Total Commission</b></td><td colspan='2'>"+str(total_commission)+"</td></tr>"

    def get_commission(self):
        get_user_details = self.pool.get('res.users').browse(self.cr, self.uid, self.localcontext['active_ids'])
        print get_user_details
        user_name = get_user_details.partner_id.name
        print user_name
        get_all_saleorders = self.pool.get('sale.order').search(self.cr, self.uid,
                                                                [('user_id', '=', self.localcontext['active_ids']),
                                                                 ('state', '=', 'done')])
        total_commission = 0
        sale_order_total_amount_sum = 0
        single_sale_order_row = ''
        for each_sale_order in get_all_saleorders:
            get_sale_order_details = self.pool.get('sale.order').browse(self.cr, self.uid, each_sale_order)
            print get_sale_order_details.name
            sale_order_name = get_sale_order_details.name
            print "Amount Total", get_sale_order_details.amount_total
            sale_order_total_amount = get_sale_order_details.amount_total
            sale_order_total_amount_sum = sale_order_total_amount_sum + sale_order_total_amount
            print "Commission Value", get_sale_order_details.commission
            commission_per_sale_order = get_sale_order_details.commission
            commission = (get_sale_order_details.amount_total * commission_per_sale_order) / 100
            print "Commission", commission
            curr_commission = commission
            total_commission = total_commission + commission
            single_sale_order_row = single_sale_order_row + "<tr><td>" + user_name + "</td><td>" + sale_order_name + "</td><td>" + str(
                sale_order_total_amount) + "</td><td>" + str(curr_commission) + "</td></tr>"
        return single_sale_order_row + "<tr><td colspan='2'><b>Total Sale Order Amount</b></td><td colspan='2'>" + str(
            sale_order_total_amount_sum) + "</td></tr><tr><td colspan='2'><b>Total Commission</b></td><td colspan='2'>" + str(
            total_commission) + "</td></tr>"


class ReportManagementQweb(osv.AbstractModel):
    #    name must be report.module_name.template_id
    _name ='report.extra_tasks.report_res_users_commission'
    _inherit = 'report.abstract_report'
    _template = 'extra_tasks.report_res_users_commission'
    _wrapped_report_class = CommissionReport