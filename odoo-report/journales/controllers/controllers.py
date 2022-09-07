# -*- coding: utf-8 -*-
# from odoo import http


# class Journales(http.Controller):
#     @http.route('/journales/journales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/journales/journales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('journales.listing', {
#             'root': '/journales/journales',
#             'objects': http.request.env['journales.journales'].search([]),
#         })

#     @http.route('/journales/journales/objects/<model("journales.journales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('journales.object', {
#             'object': obj
#         })
