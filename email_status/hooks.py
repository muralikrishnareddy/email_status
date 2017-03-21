# -*- coding: utf-8 -*-
# Copyright 2017, credativ Ltd
#                 Kinner Vachhani <kin.vachhani.gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging
from psycopg2.extensions import AsIs

_logger = logging.getLogger(__name__)


def column_exists(cr, table, column):
    cr.execute("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = %s AND column_name = %s""", (table, column))
    return bool(cr.fetchall())


def column_add_with_value(cr, table, column, field_type, value):
    if not column_exists(cr, table, column):
        cr.execute("""
            ALTER TABLE %s
            ADD COLUMN %s %s""", (AsIs(table), AsIs(column), AsIs(field_type)))


def pre_init_hook(cr):
    """ Set Mail state on Mail Message """
    # Update state field using sql query. When you install this module on
    # database with large mail_message table then module installation could
    # take hours to update state field so instead update using sql query.

    _logger.info("Adding State column on mail_message")
    column_add_with_value(
        cr, "mail_message", "state", "character varying", False)

    _logger.info("Updating state column on table mail_mail")
    cr.execute("UPDATE mail_message msg SET state=mail.state FROM \
               mail_mail mail WHERE mail.mail_message_id = msg.id")
