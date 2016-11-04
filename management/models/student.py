# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import SUPERUSER_ID, api
from openerp.exceptions import except_orm,UserError, ValidationError
from openerp import tools
from openerp import models, fields, api, _ # v8
import datetime

class student(models.Model):
    _name = 'student'

    @api.model
    def set_fees_amt(self):
        return 2000

    _defaults = {
    'fees_amt': set_fees_amt
    }

    image = fields.Binary('Image')
    name = fields.Char('Name', required=1)
    address = fields.Text('Address')
    pincode = fields.Char('Pincode')
    telephone = fields.Char('Telephone')
    birthdate = fields.Date('Birthdate')
    teacher_id = fields.Many2one('teacher','Teachers')
    achievement_ids = fields.One2many('achievement','student_id','Achievements')
    joindate = fields.Datetime('Join Date')
    roll_no = fields.Integer('Roll Number')
    fees_amt = fields.Float('Fees')
    details = fields.Text('Details')
    stand = fields.Selection([('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four')], 'Stand.')
    list = ['0','1','2','3','4','5','6','7','8','9']

    @api.multi
    def concatenate(self):
        student_name = self.name
        student_address = self.address
        self.details = "Name: %s \n Address: %s" %(student_name,student_address)
        print student_name

    @api.multi
    def write(self,vals):
        
        if vals.get('name',False):
            for obj in vals.get('name'):
                if obj.isalpha():
                   pass
                else:
                    raise except_orm(_("Warning"),("You are not allowed to enter numbers in name field"))
        return super(student, self).write(vals)

    @api.model
    def create(self,vals):
        # list = ['0','1','2','3','4','5','6','7','8','9']
        if vals.get('name',False):
            for obj in vals.get('name'):
                if obj.isalpha():
                    pass
                else:
                    raise except_orm(_("Warning"),("You are not allowed to enter numbers in name field"))
        return super(student, self).create(vals)

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})
        default.update(name=("%s") % (''))
        default.update(address=("%s") % (''))
        return super(student, self).copy(default)

    # @api.multi
    # def unlink(self):
    #     if self.active == 1:
    #         raise except_orm(_("Warning"),("You are not allowed to delete an active student"))
    #     else:
    #         pass
    #     return  super(student, self).unlink()

    # @api.multi
    # def read(self,fields=None,load='_classic_read'):
    #     res = super(student, self).read(fields=fields)
    #     print "fields Name",fields
    #     print "Self", self
    #     for each in res:
    #         if each.has_key('active'):
    #             each['name'] = each['name']
    #             each['roll_no'] = each['roll_no']
    #             each['details'] = 'This student Is Active'
    #     return res

    @api.model
    def default_get(self, fields):
        res = super(student, self).default_get(fields)
        new_no = res.get('roll_no',0) + 1
        res.update({'roll_no':new_no})
        return res

    def hello(self):
        my_date = datetime.datetime.now()
        return my_date

    @api.multi
    def open_wizard(self):
        wiz = self.env['student.wizard'].create({'name': self.name,
                                                 'roll_no': self.roll_no,
                                                 })
        context = {}
        context['active_id'] = wiz.id

        return {
            'name': _('Results'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'student.wizard',
            'res_id': wiz.id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': context,
        }
    

