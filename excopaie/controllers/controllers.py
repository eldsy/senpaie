# -*- coding: utf-8 -*-
# from odoo import http


# class Excopaie(http.Controller):
#     @http.route('/excopaie/excopaie/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/excopaie/excopaie/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('excopaie.listing', {
#             'root': '/excopaie/excopaie',
#             'objects': http.request.env['excopaie.excopaie'].search([]),
#         })

#     @http.route('/excopaie/excopaie/objects/<model("excopaie.excopaie"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('excopaie.object', {
#             'object': obj
#         })
