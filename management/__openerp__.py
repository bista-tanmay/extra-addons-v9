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
{
    'name' : 'School-Employee Management',
    'version' : '1.0',
    'author' : 'Tanmay @ Bista Solutions',
    'category' : 'Management',
    'description' : """
    School/Employee Management
    """,
    'depends' : ['base','report','sale'],
    'data': [
        'views/student_view_form.xml',
        'views/teacher_view_form.xml',
        'views/subject_view_form.xml',
        'views/student_search_view.xml',
        'views/employee_information_view.xml',
        'views/attendance_information_view.xml',
        'views/management_information_view.xml',
        'views/customer_liability_view.xml',
        'views/priority_customer_view.xml',
        'views/achievement_view.xml',
        'report/reports.xml',
        # 'views/sale_order_report.xml',
        'wizard/student_wizard_view.xml',
        'report/student_records_report.xml',
        'views/priority_table_view.xml',
    ],
    'css': ['static/src/css/office.css',
            'static/src/css/school.css'],
    'demo': ['demo/teacher_data.xml',
             'demo/student_data.xml',
             'demo/achievement_data.xml',
            ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
