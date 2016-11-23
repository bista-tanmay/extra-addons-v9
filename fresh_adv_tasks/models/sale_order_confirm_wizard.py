from openerp import fields,models,api,_
from openerp.exceptions import except_orm,UserError
import time

class SaleOrderConfirmWizard(models.TransientModel):
    _name = 'sale.order.confirm.wizard'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(SaleOrderConfirmWizard, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        # Get current ids from context
        curr_active_ids = self._context.get('active_ids')
        # Initialize two empty strings to store sale order names & their respective states
        name_of_sale_orders = ''
        state_of_sale_orders = ''
        # Loop through all sale order active ids
        for all_ids in curr_active_ids:
            # Get each sale order record using active ids
            curr_sale_order = self.env['sale.order'].browse(all_ids)
            # Check
            if curr_sale_order.state == 'draft':
                pass
            else:
                if name_of_sale_orders == '' and state_of_sale_orders == '':
                    name_of_sale_orders = curr_sale_order.name
                    state_of_sale_orders = curr_sale_order.state
                else:
                    name_of_sale_orders += ',' + curr_sale_order.name
                    state_of_sale_orders += ',' + curr_sale_order.state
        if name_of_sale_orders != '':
            raise UserError(_("Sale Order %s is in %s state") % (name_of_sale_orders, state_of_sale_orders))
        return res

    @api.multi
    def confirmSale(self):
        # Get list of all sale order ids
        curr_active_ids = self._context.get('active_ids')
        # Loop through all curr_active_ids
        for all_ids in curr_active_ids:
            # Browse records using ids
            curr_sale_order = self.env['sale.order'].browse(all_ids)
            # Save current sale order state
            # sale_order_state = curr_sale_order.state
            # Check if state is draft
            # if sale_order_state == 'draft':
            # Confirm Sale Order if state is draft
            curr_sale_order.action_confirm()
            # Create records in sale.advance.payment.inv wizard
            wiz = self.env['sale.advance.payment.inv'].create({
                'advance_payment_method': 'delivered',
                'amount': curr_sale_order.amount_total,
                })
            # Create a invoice for the sale order
            wiz.create_invoices()
            # Search for related invoice(s)
            curr_account_invoice = self.env['account.invoice'].search([('origin','=',curr_sale_order.name)])
            # Loop through all curr_account_invoice
            for each_account_invoice in curr_account_invoice:
                # Validate invoice by calling workflow as below
                each_account_invoice.signal_workflow('invoice_open')
            # else:
            #     raise UserError("Sale Order already confirmed")