# -*- coding:utf-8 -*-

from odoo import api, fields, models


class ExcoSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'
    _description = 'SalaryRule'
    
    
    financial_statements_display = fields.Selection([
        ('chp_ipres', 'Patronales IPRES'),
        ('chs', 'Salariales'),
        ('brut', 'Bruts'),
        ('noim', 'Non imposables'),
        ('cache', 'Caches'),
        ('totaux', 'Totaux'),
        ('chp_css', 'Patronales CSS'),
        ('chp_vrs', 'Patronales VRS'),
        ('chp_ipm', 'Patronales IPM')
    ], string="Affichage dans les etats")