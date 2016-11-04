import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression  # V7
from openerp import models, fields, api, _  # v8
from datetime import datetime
import calendar


class student(models.Model):
    _name = "student.student"

    name = fields.Many2one('res.partner', string="student name")
    roll_no = fields.Integer('roll no')
    student_class = fields.Char('student class')
    fees_structure = fields.One2many('fees.structure', 'student_fee_id', 'fees')


class fees_structure(models.TransientModel):
    _name = "fees.structure"

    student_fee_id = fields.Many2one('student.student', 'student fees id')
    computer_fee = fields.Float('computer fees')
    tution_fees = fields.Float('tution fees')
    monthly_fee = fields.Float('monthly fees')
    month_date = fields.Date('month date')
    month_name = fields.Char('month name')
    state = fields.Selection([
        ('start','start'),
        ('end','end'),
    ])


    _defaults={
        'state':'start'
    }

    def calculate_total_fees(self):
        total_fee = 0
        total_fee = total_fee + self.computer_fee + self.tutuion_fees + self.monthly_fee
        return total_fee

    total_fee = fields.Float('total fees',compute='calculate_total_fees',store=1)
    paid_fees = fields.Float('paid balance')

    def calculate_remaining_fee(self):
        left_to_pay = 0
        left_to_pay = left_to_pay + self.total_fee - self.paid_fees
        return left_to_pay

    left_to_pay = fields.Float('balace remaining',compute='calculate_remaining_fee',store=1)

    @api.multi
    @api.onchange('month_date')
    def task(self):
        if self.month_date:
            d1 = datetime.strptime(self.month_date, "%Y-%m-%d").date()
            my_calendar_month = calendar.month_name[d1.month]
            self.month_name = my_calendar_month
