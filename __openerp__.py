# -*- coding: utf-8 -*-
{
    'name': "Website Sitemap Customizer",

    'summary': """
        Specify which pages should be listed in sitemap.xml""",

    'description': """
        For SEO purposes a concise and useful sitemap is top
        priority. This module provides tools to customize it.
    """,

    'author': "Technikum Wien GmbH",
    'website': "http://www.lllacademy.at",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}