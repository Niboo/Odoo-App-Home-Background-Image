# -*- coding: utf-8 -*-
{
    'name': "Home background image",

    'summary': """
        Set a background image for the Odoo company.
    """,

    'description': """
        Set a background image for the Odoo company.
        The background image is shown in the Odoo backend only.
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-system.ch",
    'category': 'Customizations',
    'version': '14.0.1.0.0',

    'depends': ['base'],

    'data': [
        'views/assets.xml',
        'views/views.xml',
    ],

    'installable': True,
    'application': False,
}