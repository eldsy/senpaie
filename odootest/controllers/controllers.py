# -*- coding: utf-8 -*-
# from odoo import http


# class Odootest(http.Controller):
#     @http.route('/odootest/odootest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odootest/odootest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odootest.listing', {
#             'root': '/odootest/odootest',
#             'objects': http.request.env['odootest.odootest'].search([]),
#         })

#     @http.route('/odootest/odootest/objects/<model("odootest.odootest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odootest.object', {
#             'object': obj
#         })
