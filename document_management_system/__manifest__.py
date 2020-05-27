# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "Document1234",
    'summary': "Enterprise online document management",
    'author': "renjie <i@renjie.me>",
    'website': "https://renjie.me",
    'support': 'i@renjie.me',
    'category': 'Document Management',
    'version': '1.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/webclient_templates.xml',
        'views/document.xml',
    ],
    'images': [
        'static/description/main_screenshot.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}