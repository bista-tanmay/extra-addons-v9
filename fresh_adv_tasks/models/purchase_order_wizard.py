from openerp import fields,api,models,_
from openerp.exceptions import except_orm,UserError

class PurchaseorderWizard(models.Model):
    _name = 'purchase.order.wizard'

    @api.multi
    def confirm_purchase_orders(self):
        all_active_ids = self._context.get('active_ids')
        copy_curr_active_ids = all_active_ids
        for each_current_active_ids in all_active_ids:
            browse_active_ids = self.env['purchase.order'].browse(each_current_active_ids)
            origin_name_list = ''
            for each_copy in copy_curr_active_ids:
                browse_copy_active_ids = self.env['purchase.order'].browse(each_copy)
                if browse_copy_active_ids.id == browse_active_ids.id:
                    continue
                if browse_active_ids.partner_id.id == browse_copy_active_ids.partner_id.id and \
                    browse_active_ids.payment_term_id.id == browse_copy_active_ids.payment_term_id.id and browse_active_ids.state != 'cancel' and browse_copy_active_ids.state != 'cancel':
                    origin_name = browse_copy_active_ids.name or ''
                    origin_name_list += str(origin_name) + ','
                    for each_order_line in browse_copy_active_ids.order_line:
                        copy_order_line_object = each_order_line.copy()
                        copy_order_line_object.update({'order_id':browse_active_ids.id})
                    browse_copy_active_ids.write({'state': 'cancel'})
                browse_active_ids.write({'origin':origin_name_list})

class StockPickingWizard(models.Model):
    _name = 'stock.picking.wizard'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(StockPickingWizard, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,submenu=submenu)
        not_transfered_name_list = ''
        not_transfered_state_list = ''
        all_active_ids = self._context.get('active_ids')
        for each_current_active_ids in all_active_ids:
            browse_active_ids = self.env['stock.picking'].browse(each_current_active_ids)
            if browse_active_ids.state != 'assigned':
                if not_transfered_name_list == '' and not_transfered_state_list == '':
                    not_transfered_name_list += browse_active_ids.name
                    not_transfered_state_list += browse_active_ids.state
                else:
                    not_transfered_name_list += ','+browse_active_ids.name
                    not_transfered_state_list += ','+browse_active_ids.state
        if not_transfered_name_list != '':
            raise UserError(_("Stock Picking %s are in %s state(s) respectively") % (not_transfered_name_list, not_transfered_state_list))
        return res

    @api.multi
    def confirm_stock_transfer(self):
        # Get active record ids from context
        all_active_ids = self._context.get('active_ids')
        for each_current_active_ids in all_active_ids:
            # Get record information from stock.picking table
            browse_active_ids = self.env['stock.picking'].browse(each_current_active_ids)
            print browse_active_ids
            # Check if state of record is available
            if browse_active_ids.state == 'assigned':
                print browse_active_ids.state
                # Search for transferable record in stock.immediate.transfer
                immediate_id = self.env['stock.immediate.transfer'].search([('pick_id','=',browse_active_ids.id)])
                # Loop through each record if multiple records exists
                for each in immediate_id:
                    # Transfer the stock.picking records
                    each.process()
            else:
                pass
