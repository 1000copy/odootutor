# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "TodoApp",
    'summary': "Todo",
    'author': "Reco",
    'website': "Reco",
    'support': 'Reco',
    'category': 'Todo',
    'version': '1.0',
    'depends': ['base','mail'],
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/document.xml',
    ],    
    'installable': True,
    'auto_install': False,
    'application': True,
}