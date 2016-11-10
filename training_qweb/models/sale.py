from openerp import models,api

class SaleOrder(models.Model):
    _inherit='sale.order'

    @api.multi
    def get_total(self):
        total=self.amount_total
        rounding=round(total,0)
        return rounding
        
