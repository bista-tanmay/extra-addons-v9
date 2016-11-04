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

from openerp import models, fields, api

# from openerp.tools.translate import _

class teacher_salary(models.TransientModel):
    _name = "teacher.salary"
    _description = "Make Salary"

    name = fields.Char('Name')
    salary = fields.Float('Salary')
    extra = fields.Float('Extra Salary')

    @api.model
    def default_get(self, fields_list):
        res = super(teacher_salary, self).default_get(fields_list)
        print "res+++++",res
        print "context++++++",self._context
