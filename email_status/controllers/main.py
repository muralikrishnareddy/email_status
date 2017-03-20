# -*- coding: utf-8 -*-
# Copyright 2017, credativ Ltd
#                 Kinner Vachhani <kin.vachhani.gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging
import time

import openerp
from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp.addons.web.controllers.main import ensure_db
import openerp.pooler as pooler
_logger = logging.getLogger(__name__)


# ----------------------------------------------------------
# Controller
# ----------------------------------------------------------
class LockoutSign(openerp.addons.web.controllers.main.Home):

    @http.route()
    def web_login(self, *args, **kw):
        ensure_db()
        cr = request.cr
        response = super(LockoutSign, self).web_login(*args, **kw)
        if response.is_qweb and 'error' in response.qcontext:
            error = response.qcontext['error']
            if error:
                if request.httprequest.method == 'POST':
                    company_ids = pooler.get_pool(request.session.db).\
                        get('res.company').search(cr, SUPERUSER_ID, [])
                    company = pooler.get_pool(request.session.db).\
                        get('res.company').browse(cr, SUPERUSER_ID,
                                                  company_ids[0])
                    attempt_cnt = company.attempt_cnt
                    unlock_after = company.lockouttime_id.value
                    unlock_after_name = company.lockouttime_id.name
                    uid = request.session.authenticate(
                        request.session.db,
                        request.params['login'],
                        request.params['password'],
                    )
                    if uid is False:
                        uloginids = pooler.get_pool(request.session.db).\
                            get('res.users').search(cr,
                                                    SUPERUSER_ID,
                                                    [('login',
                                                      '=',
                                                      request.params['login'])
                                                     ])
                        for lid in pooler.get_pool(request.session.db).\
                            get('res.users').browse(cr,
                                                    SUPERUSER_ID,
                                                    uloginids):
                            if lid.flg_userlocked:
                                if unlock_after == 0:
                                    error = 'Your Login is temporarily Locked.\
                                             Please Contact Administrator to \
                                             Unlock it.'
                                else:
                                    error = 'Your Login is temporarily Locked. \
                                        Please try after ' + unlock_after_name
                            else:
                                wronglogin_cnt = lid.wronglogin_cnt \
                                            and lid.wronglogin_cnt+1 or 1
                                pooler.get_pool(request.session.db).\
                                    get('res.users').write(cr,
                                                           SUPERUSER_ID,
                                                           [lid.id],
                                                           {'wronglogin_cnt':
                                                            wronglogin_cnt})
                                if int(lid.wronglogin_cnt) >= int(attempt_cnt):
                                    pooler.get_pool(request.session.db).\
                                        get('res.users').write(
                                            cr,
                                            SUPERUSER_ID,
                                            [lid.id],
                                            {'flg_userlocked':
                                             True,
                                             'userlocked_datetime':
                                             time.strftime('%Y-%m-%d %H:%M:%S')
                                             })
                                    if unlock_after == 0:
                                        error = 'Your Login is temporarily \
                                        Locked. Please Contact Administrator \
                                        to Unlock it.'
                                    else:
                                        error = 'Your Login is temporarily \
                                        Locked. Please try after ' \
                                        + unlock_after_name
                response.qcontext['error'] = error
        return response
