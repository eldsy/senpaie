# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExcoConventionCategory(models.Model):
    _name = 'excopaie.convention_category'
    _description = 'excopaie.convention_category'

    name = fields.Char(string='Categories')
    hourly_wage = fields.Float(string='Salaires horaires')
    salary_for173h = fields.Float(string='Salaires pour 173,33')
    convention_type = fields.Many2one('excopaie.convention_type',ondelete='cascade', string="Types de conventions", required=True)
    
    
