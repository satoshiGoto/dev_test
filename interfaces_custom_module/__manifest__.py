# -*- coding: utf-8 -*-
{
    'name': "Módulo de Ventas Customizado",

    'summary': "Personalización del módulo de ventas",

    'description': """
Personalización del módulo de ventas
    """,

    'author': "Interfaces S.A",
    'website': "https://www.interfaces.com.py/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale'],

    # always loaded
    'data': [

        'reports/sale_order_report.xml',
        'views/res_partner_view_form_inherit.xml',
        'views/sale_order_view_form_inherit.xml',

    ],
    'installable': True,
    'auto_install': False,
}
