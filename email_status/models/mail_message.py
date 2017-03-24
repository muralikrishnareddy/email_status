# -*- coding: utf-8 -*-
# Copyright 2017, credativ Ltd
#                 Kinner Vachhani <kin.vachhani@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


import logging

from openerp import models, fields, api

_logger = logging.getLogger(__name__)


class mail_message(models.Model):
    _inherit = 'mail.message'

    @api.one
    @api.depends('mail_ids.state')
    def _set_state(self):
        """
            update message state when mail state gets updated
        """

        # TODO self.state is always false -- Investigate
        mail = self.mail_ids and self.mail_ids[0] or False
        if mail:
            self.state = mail.state
        else:
            # Following statement return state
            # to database else sends false value
            return self.read(['state'])[0].get('state')

    def _get_state(self):
        ''' Return the mail.mail selection state '''
        return self.env['mail.mail']._columns.get('state').selection

    state = fields.Selection(selection='_get_state',
                             string='Status',
                             compute='_set_state',
                             store=True,
                             )
    mail_ids = fields.One2many('mail.mail',
                               'mail_message_id',
                               auto_join=True,
                               )

    @api.model
    def _message_read_dict(self, message, parent_id=False):
        ret = super(mail_message, self)._message_read_dict(
                                                           message,
                                                           parent_id=parent_id,
                                                           )
        # Super method do not return State field by default
        # Read the state from message and update the return dict
        if 'id' in ret:
            ret['state'] = message.state
        return ret
