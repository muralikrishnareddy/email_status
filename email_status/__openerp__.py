# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'To show Email Status related to Message',
    'category': 'Social Network', 
    'version': '1.0',
    'description': """
Email Status
========================================

To show the Status of Emails sent while creating Messages in Odoo (Shows the Status till Email not get Deleted).

    """,
    'author': 'Murali Krishna Reddy',
    'website': 'http://www.credativ.in',
    'sequence':0,
    'depends': ['base', 'web', 'mail'],
    'images':['images/main_screenshot.png'],
    'data': [
        'views/email_status.xml',
        'mail_message_view.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
