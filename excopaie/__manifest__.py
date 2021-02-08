# -*- coding: utf-8 -*-
{
    'name': "excopaie",

    'summary': """
        Module de paie de ExcoSenegal """,

    'description': """
        Module de paie de ExcoSenegal 
    """,

    'author': "ExcoSenegal",
    'website': "http://www.exco-senegal.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'l10n_fr_hr_payroll'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/exco_hr_employee.xml',
        'views/exco_hr_contract.xml',
        'views/menu.xml',
        'views/convention_type.xml',
        'views/convention_category.xml',
        'views/exco_hr_salary_rule.xml',
        'views/financial_statement.xml',
        'report/exco_hr_payslip_report_fr.xml',
        'report/exco_hr_payslip_report.xml',
        'report/exco_payroll_book_report.xml',
        'report/exco_wage_costs_report.xml',
        'report/exco_employer_charges_report.xml',
        'report/action_menu_report.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
