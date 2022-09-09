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
    def move_get(self, db=None, login=None, password=None, number=False, company=1, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                move = request.env['account.move'].search_read([('l10n_latam_document_number', '=', number),('company_id', '=', company)], limit=1, fields=['name', 'id'])
                return {'status': 'Ok', 'move_id': move.id, 'move_name': move.name}
        except Exception as e:
            return {'status': "Error", 'error': str(e)}