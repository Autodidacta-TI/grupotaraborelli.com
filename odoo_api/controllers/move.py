# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request
import re
import xmlrpc.client

_logger = logging.getLogger(__name__)
CORS = '*'

class RentylOdooMoveApi(http.Controller):

    @http.route('/odoo-api/move/get', type="json", auth='none', cors=CORS)
    def move_get(self, db=None, login=None, password=None, name=False, company=1, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                move = request.env['account.move'].search_read([('name', '=', name),('company_id', '=', company)], limit=1, fields=['name', 'id', 'l10n_ar_afip_auth_code'])
                return {'status': 'Ok', 'move_id': move.id, 'move_name': move.name, 'cae': move.l10n_ar_afip_auth_code}
        except Exception as e:
            return {'status': "Error", 'error': str(e)}