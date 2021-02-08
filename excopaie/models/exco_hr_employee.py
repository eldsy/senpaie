# -*- coding:utf-8 -*-

from odoo import api, fields, models


class ExcoEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee'
    
    
    spouse_with_income = fields.Boolean(string='Conjoint(e) avec un revenu')
    marital = fields.Selection([
        ('single', 'Célibataire'),
        ('married', 'Marié'),
        ('cohabitant', 'Cohabitant légal'),
        ('widower', 'Veuf(ve)'),
        ('divorced', 'Divorcé(e)')
    ], string="État Civil")