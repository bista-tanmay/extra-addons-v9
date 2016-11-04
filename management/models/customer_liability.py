from openerp import models, fields, api, _

class customer_liability(models.Model):
    _name = 'customer.liability'

    customer_id = fields.Many2one('res.partner', 'Customer')
    points_earned = fields.Float('Points Earned')
    state = fields.Selection([('draft', 'Draft'),
                              ('approved', 'Approved'),
                              ('cancel', 'Cancel'),
                              ], default='draft')

    # This function is triggered when the user clicks on the button 'Set to started'
    @api.one
    def draft_progressbar(self):
        self.write({
            'state': 'draft',
        })

    # This function is triggered when the user clicks on the button 'Set to started'
    @api.one
    def in_progress_progressbar(self):
        self.write({
            'state': 'in_progress'
        })

    # This function is triggered when the user clicks on the button 'In progress'
    @api.one
    def approved_progressbar(self):
        self.write({
            'state': 'approved'
        })

    # This function is triggered when the user clicks on the button 'Done'
    @api.one
    def cancel_progressbar(self):
        self.write({
            'state': 'cancel',
        })

