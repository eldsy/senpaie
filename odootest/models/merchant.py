# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Merchant(models.Model):
    _name = 'odootest.merchant'
    _inherits = 'res.partner'
    _description = 'Merchant'

    validation_state = fields.Selection([
        ('created', 'Créé'),
        ('checked', 'Vérifié'),
        ('validated', 'Validé'),
        ('rejected', 'Rejeté'),
    ], default='created')
    
    
class RejectionComment(models.Model):
    _name = 'odootest.rejection_comment'
    _description = 'Rejection Comment'
    
    comment = fields.Char()
    merchant_id = fields.Many2one('odootest.merchant', ondelete='cascade', required=True)
    rejected_state = fields.Selection([
        ('verification', 'Vérification'),
        ('validation', 'Validation'),
    ], default='created', compute="__calcul_rejected_state", store=True)


    @api.depends('merchant_id')
    def __calcul_rejected_state(self):
        for record in self:
            if record.merchant_id.validation_state == 'created':
                record.rejected_state = 'verification'
            if record.merchant_id.validation_state == 'checked':
                record.rejected_state = 'validation'