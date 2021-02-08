# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExcoConventionType(models.Model):
    _name = 'excopaie.convention_type'
    _description = 'excopaie.convention_type'

    name = fields.Char(string='Conventions')