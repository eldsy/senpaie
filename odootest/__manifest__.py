# -*- coding: utf-8 -*-
{
    'name': "odootest",

    'summary': """
        Odoo
        Test""",

    'description': """
        Odoo Test description
    """,

    'author': "Test",
    'website': "http://www.test.com",
    
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml'
        'views/menu.xml',
        'views/merchant.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
