from odoo import models, fields, api


class Shop(models.Model):
    _name = 'odootest.shop'
    _description = 'Shop'
    
    
    
    name = fields.Char()
    merchant_id = fields.Many2one('odootest.merchant', ondelete='set null', related_field="shop_ids")
    validation_state = fields.Selection([
        ('created', 'Créé'),
        ('checked', 'Vérifié'),
        ('validated', 'Validé'),
        ('rejected', 'Rejeté'),
    ], default='created')