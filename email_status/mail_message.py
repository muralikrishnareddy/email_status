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

import logging

from openerp import tools

from email.header import decode_header
from email.utils import formataddr
from openerp import SUPERUSER_ID, api
from openerp.osv import osv, orm, fields
from openerp.tools import html_email_clean
from openerp.tools.translate import _
from HTMLParser import HTMLParser

_logger = logging.getLogger(__name__)

class mail_message(osv.Model):
    _inherit = 'mail.message'
    
    def _get_mail_state(self, cr, uid, ids, name, arg, context=None):
        res = dict((id, False) for id in ids)
        for rec in self.browse(cr, uid, ids, context=context):
            datas = self.pool.get('mail.mail').search_read(cr, uid, [('mail_message_id','=',rec.id)],['state'], context=context)
            if datas:
                res[rec.id] = datas[0]['state']
        return res  
        
    def _get_mail_status(self, cr, uid, ids, context=None):
        res = set()
        for mail in self.browse(cr, uid, ids, context=context):
            if mail.state and mail.mail_message_id:
                res.add(mail.mail_message_id.id)
        return list(res)
        
    _columns = {
        'state': fields.function(_get_mail_state, type='selection',selection=[('outgoing', 'Outgoing'),('sent', 'Sent'),('received', 'Received'),('exception', 'Delivery Failed'),('cancel', 'Cancelled')], string='Status', store={'mail.mail': (_get_mail_status, ['state'], 10)}),
    }
    
    def _message_read_dict(self, cr, uid, message, parent_id=False, context=None):
        ret = super(mail_message,self)._message_read_dict(cr, uid, message, parent_id=parent_id, context=context)
        if 'id' in ret:
            ret['state'] = message.state 
        return ret
    
    
    
    
    
    
    
    
    
    

