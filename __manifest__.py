{
    'name': "Home background image",

    'summary': """
        Set a background image for the Odoo company.
    """,

    'author': "Mint System GmbH, Odoo Community Association (OCA)",
    'website': "https://www.mint-system.ch",
    'category': 'Customizations',
    'version': '14.0.1.1.0',
    'license': 'AGPL-3',

    'depends': ['base'],

    'data': [
        'views/assets.xml',
        'views/views.xml',
    ],

    'installable': True,
    'application': False,
}
