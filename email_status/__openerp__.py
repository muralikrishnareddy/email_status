# -*- coding: utf-8 -*-
# Copyright 2017, credativ Ltd
#                 Kinner Vachhani <kin.vachhani.gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    'name': 'To show Email Status related to Message',
    'category': 'Social Network',
    'version': '8.0.1.1.0',
    'author': 'Murali Krishna Reddyi, Kinner Vachhani',
    'license': 'AGPL-3',
    'website': 'http://www.credativ.in',
    'depends': ['base',
                'web',
                'mail',
                ],
    'data': [
        'views/email_status.xml',
        'views/mail_message_view.xml',
        ],
    'qweb': ['static/src/xml/mail.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'pre_init_hook': "pre_init_hook",
}
