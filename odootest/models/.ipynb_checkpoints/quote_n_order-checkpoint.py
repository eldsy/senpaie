from odoo import models, fields, api


class Shop(models.Model):
    _name = 'odootest.shop'
    _description = 'Shop'
    
    
    name = fields.Char()
    merchant_id = fields.Many2one('odootest.merchant', ondelete='cascade', required=True)

    
class Shop(models.Model):
    _name = 'odootest.shop'
    _description = 'Shop'

    
    name = fields.Char()
    merchant_id = fields.Many2one('odootest.merchant', ,ondelete='cascade', required=True)