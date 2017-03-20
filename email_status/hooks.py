# -*- coding: utf-8 -*-
# Copyright 2017, credativ Ltd
#                 Kinner Vachhani <kin.vachhani.gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging


_logger = logging.getLogger(__name__)


def post_init_hook(cr, pool):
    """ Set Mail state on Mail Message """
    # Update state field using sql query. When you install this module on
    # database with large mail_message table then module installation could
    # take hours to update state field so instead update using sql query.

    _logger.info("Updating mail message state")
    cr.execute("UPDATE mail_message msg SET state=mail.state FROM \
               mail_mail mail WHERE mail.mail_message_id = msg.id")
