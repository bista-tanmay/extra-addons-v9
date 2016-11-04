from openerp import models, fields, api, _


class priority_customer(models.Model):

    _inherit = 'res.partner'

    is_priority = fields.Boolean("Is Priority Partner:?")
    registration_date = fields.Date("Registration Date:")
    liability_card_number = fields.Char("Liability Card Number:")
