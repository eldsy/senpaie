from odoo import models, fields, api


class Shop(models.Model):
    _inherit = 'odootest.shop'
    _description = 'Shop'
    
    
    name = fields.Char()
    merchant_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
    
    
class Shop(models.Model):
    _inherit = 'odootest.shop'
    _description = 'Shop'
    
    
    name = fields.Char()
    merchant_id = fields.Many2one('res.partner', ,ondelete='cascade', required=True)