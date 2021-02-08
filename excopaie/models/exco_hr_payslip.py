# -*- coding:utf-8 -*-

from odoo import api, fields, models


class ExcoPayslip(models.Model):
    _inherit = 'hr.payslip'
    _description = 'Payslip'


    state_id = fields.Many2one('excopaie.financial_statement',ondelete='set null', string="Etats", related_field="payslip_ids")
