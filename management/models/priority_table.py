from openerp import models,fields,api,_
from openerp.exceptions import except_orm

class PriorityTable(models.Model):
    _name = 'priority.table'
    _description = 'Priority Table'

    name = fields.Char("Name",required=1)
    set_priority = fields.Boolean("Set Priority")
    res_partner_id = fields.Many2one('res.partner','Partner')

    @api.multi
    def write(self, vals):
        # print "Write Vals Of Priority Table",vals
        # print "Write Context Of Priority Table",self._context
        # print self.res_partner_id.id
        curr_id = self.res_partner_id.id
        search_priorities = self.env['priority.table'].search(['&',('res_partner_id','=',curr_id),('set_priority','=',True)])
        for each in search_priorities:
            # print "Current Name",each.name
            # print "Priority In DB", each.set_priority
            if vals['set_priority'] == True:
                each['set_priority'] = False
        return super(PriorityTable, self).write(vals)

    @api.model
    def create(self, vals):
        print "Create Context Of Priority Table",self._context
        print "Create Vals Of Priority Table",vals
        # print "Create Context Of Priority Table self._context.get('params')['id']",self._context.get('params')['id']
        # print "Create Context Of Priority Table self._context.get('params')['id']",vals.get('res_partner_id')
        curr_id = vals['res_partner_id']
        search_priorities = self.env['priority.table'].search(['&',('res_partner_id', '=', curr_id),('set_priority','=',True)])
        # search_priorities = self.env['priority.table'].search([('res_partner_id', '=', vals['res_partner_id']),('set_priority','=',True)])
        for each in search_priorities:
            # print "Current Name", each.name
            # print "Priority In DB", each.set_priority
            if vals['set_priority'] == True:
                each['set_priority'] = False
        return super(PriorityTable, self).create(vals)

class PriorityTableResPartner(models.Model):
    _inherit = 'res.partner'

    res_priority_table = fields.One2many('priority.table', 'res_partner_id', string='Priorities')

    # @api.multi
    # def write(self, vals):
    #     print "Write Of Res Partner Vals",vals
    #     print "Write Of Res Partner Context",self._context
    #     # self._context['res_partner_id'] =
    #     return super(PriorityTableResPartner,self).write(vals)

    # @api.model
    # def create(self, vals):
    #     print "Create Of Res Partner Vals", vals
    #     print "Create Of Res Partner Context", self._context
    #     return super(PriorityTableResPartner,self).create(vals)

class PriorityTableSaleOrder(models.Model):
    _inherit = 'sale.order'

    priority_table_id = fields.Many2one('priority.table','Priority')

    @api.multi
    @api.onchange('partner_id')
    def onPartnerIdChange(self):
        curr_field_id = self.partner_id.id
        search_ids = self.env['priority.table'].search(['&',('res_partner_id','=',curr_field_id),('set_priority','=',True)])
        curr_id = 0
        for eachSearch in search_ids:
            curr_id = eachSearch.id
        self.priority_table_id = curr_id
