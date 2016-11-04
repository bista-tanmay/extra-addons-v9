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

class student_search(models.Model):
    _name = 'student.search'
    
    name = fields.Char('Name',)
    roll_no = fields.Integer('Roll No')
    details = fields.Text("Details")

    @api.multi
    def search_student_info(self):
        stud_name = self.name
        stud_roll_no = self.roll_no
        stud_details = self.env['student'].search(['&',('name','=',stud_name),('roll_no','=',stud_roll_no)])
        print stud_details
        string_details = ''
        for each_detail in stud_details:
            string_details += '****Record****\n'
            string_details += 'Name = ' + each_detail.name + '\nRoll No.' + str(each_detail.roll_no) + '\nTelephone. ' + each_detail.telephone + '\n'
        self.details = string_details

    @api.multi
    def browse_student_info(self):
        stud_name = self.name
        stud_roll_no = self.roll_no
        stud_search = self.env['student'].search(['&',('name','=',stud_name),('roll_no','=',stud_roll_no)])
        string_details = ''
        for each_detail in stud_search:
            stud_details = self.env['student'].browse(each_detail.id)
            string_details += '****Record****\n'
            string_details += 'Name = ' + stud_details.name + '\nRoll No.' + str(stud_details.roll_no) + '\nTelephone. ' + stud_details.telephone + '\n'
        self.details = string_details