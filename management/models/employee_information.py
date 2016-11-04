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
from openerp import tools
from openerp import models, fields, api, _ # v8

class employee_information(models.Model):
    _name = 'employee.information'
    
    emp_id  = fields.Integer('ID')
    name = fields.Char('Name')
    city = fields.Char('City')
    pincode = fields.Integer('Pincode')
    work_address = fields.Text('Work Address')
    work_email = fields.Char('Work Email')
    work_phone = fields.Integer('Work Phone')
    work_mobile = fields.Integer('Work Mobile')
    office_location = fields.Char('Office Location')
    company_code = fields.Integer('Company Code')
    nationality = fields.Char('Nationality',required=1)
    education_level = fields.Char('Education Level',required=1)
    college_name = fields.Char('College Name')
    date_of_birth = fields.Date('Date Of Birth')
    place_of_birth = fields.Char('Place Of Birth')


class statusbar(models.Model):
    _name = 'statusbar.demo'
    name = fields.Char('Name', required=True)
    """
    This selection field contains all the possible values for the statusbar.
    The first part is the database value, the second is the string that is showed. Example:
    ('finished','Done'). 'finished' is the database key and 'Done' the value shown to the user
    """
    state = fields.Selection([
            ('concept', 'Concept'),
            ('started', 'Started'),
            ('progress', 'In progress'),
            ('finished', 'Done'),
            ],default='concept')

    # This function is triggered when the user clicks on the button 'Set to started'
    @api.one
    def concept_progressbar(self):
        self.write({
            'state': 'concept',
            })

    # This function is triggered when the user clicks on the button 'Set to started'
    @api.one
    def started_progressbar(self):
        self.write({
            'state': 'started'
            })

    # This function is triggered when the user clicks on the button 'In progress'
    @api.one
    def progress_progressbar(self):
        self.write({
            'state': 'progress'
        })

    # This function is triggered when the user clicks on the button 'Done'
    @api.one
    def done_progressbar(self):
        self.write({
            'state': 'finished',
        })
