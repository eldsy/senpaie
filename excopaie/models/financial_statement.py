# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExcoFinancialStatement(models.Model):
    _name = 'excopaie.financial_statement'
    _description = 'excopaie.financial_statement'

    name = fields.Char(string='Nom')
    date_from = fields.Date('Debut', readonly=False, default=fields.Date.today)
    date_to = fields.Date('Fin', readonly=False, default=fields.Date.today)
    company_id = fields.Many2one('res.company', readonly=True, required=True, default=lambda self: self.env.company)
    payslip_ids = fields.One2many('hr.payslip', compute="_calcul_payslip")


    @api.depends('company_id', 'date_from', 'date_to')
    def _calcul_payslip(self):
        for record in self:
            record.payslip_ids = record.payslip_ids.search([('company_id', '=', record.company_id.id), ('date_from', '>=', record.date_from),('date_to', '<=', record.date_to)])