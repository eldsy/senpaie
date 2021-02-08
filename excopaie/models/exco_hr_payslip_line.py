# -*- coding:utf-8 -*-

from odoo import api, fields, models


class ExcoPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'
    _description = 'PayslipLine'
    
    
    financial_statements_display = fields.Selection(string='Affichages dans les etats', related="salary_rule_id.financial_statements_display", store=True)
