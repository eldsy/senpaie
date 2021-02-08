# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import date, datetime, time
from collections import defaultdict
from odoo import api, fields, models
from odoo.tools import date_utils

import pytz


class ExcoContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'
    
    medical_fees = fields.Float(string='Frais médicaux')
    transport_premium = fields.Float(string='Prime de transport')
    reimbursement_expenses = fields.Float(string='Remboursement de prêt')
    loan_repayment = fields.Float(string='Remboursement de prêt')
    net_salary = fields.Float(string='Salaire net')
    convention_type = fields.Many2one('excopaie.convention_type',ondelete='cascade', string="Types de conventions", required=True)
    convention_category = fields.Many2one('excopaie.convention_category',ondelete='cascade', string="Categories de conventions", required=True)
    base_salary = fields.Float(string='Salaire de base', related="convention_category.salary_for173h", store=True)
    is_executive = fields.Boolean(string='Cadre')
    coefficient = fields.Float(string='Nombre de part TRIMF', compute="_calcul_coefficient", store=True)
    level = fields.Float(string='Nombre de part IR', compute="_calcul_level", store=True)


            
    @api.depends('employee_id')
    def _calcul_coefficient(self):
        for record in self:
          coef = 1
          if record.employee_id.gender== 'male' and  record.employee_id.marital == 'married' and record.employee_id.spouse_with_income is False:
              coef = 2
  
          record['coefficient'] = coef
    


    @api.depends('employee_id')
    def _calcul_level(self):
        for record in self:
            niv_ec = 1
            niv_ne = record.employee_id.children*0.5
            if record.employee_id.marital == 'married' or record.employee_id.marital == 'windower': 
                niv_ec = 1.5
                if record.employee_id.marital == 'married' and record.employee_id.spouse_with_income is False:
                    niv_ec = 2
            record['level'] = min(niv_ec + niv_ne, 5)

    
    


