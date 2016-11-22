# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Copyright (c) All rights reserved:
#        (c) 2015  
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
###############################################################################
{
    'name': 'Fresh New Adv Tasks',
    'summary': 'Fresh New Adv Tasks Module Project',
    'version': '1.0',
    'description': """
Fresh New Adv Tasks Module Project.
==============================================
    """,

    'author': 'Tanmay @ Bista Solutions Inc.',
    'depends': [
        'base','sale'
    ],
    'data': [
        'views/sale_order_inherit_view.xml',
        'views/sale_order_confirm_wizard_view.xml'
    ],

    'installable': True,
    'auto_install':False,
    'application':True
}