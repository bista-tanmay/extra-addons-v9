# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Training module',
    'version' : '9.0.1.0.0',
    'summary': 'Qweb Reports',
    'sequence': 30,
    'description': """
Qweb Reports
    """,
    'category' : 'Reports',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['sale'],
    'data': [
    'views/custom_ppr_frmt.xml',
    'views/reports.xml',
    'views/sale_order_report.xml',
    
        
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}