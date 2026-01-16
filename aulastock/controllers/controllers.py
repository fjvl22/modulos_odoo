# -*- coding: utf-8 -*-
# from odoo import http


# class Aulastock(http.Controller):
#     @http.route('/aulastock/aulastock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aulastock/aulastock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aulastock.listing', {
#             'root': '/aulastock/aulastock',
#             'objects': http.request.env['aulastock.aulastock'].search([]),
#         })

#     @http.route('/aulastock/aulastock/objects/<model("aulastock.aulastock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aulastock.object', {
#             'object': obj
#         })

