from odoo import api, fields, models

class Employee(models.Model):
    _name = "employee.name"
    _description = "Employee"

    # name = fields.Char(string='Account Type', required=True, translate=True)
    # include_initial_balance = fields.Boolean(string="Bring Accounts Balance Forward", help="Used in reports to know if we should consider journal items from the beginning of time instead of from the fiscal year only. Account types that should be reset to zero at each new fiscal year (like expenses, revenue..) should not have this option set.")
    # type = fields.Selection([
    #     ('other', 'Regular'),
    #     ('receivable', 'Receivable'),
    #     ('payable', 'Payable'),
    #     ('liquidity', 'Liquidity'),
    # ], required=True, default='other',
    #     help="The 'Internal Type' is used for features available on "\
    #     "different types of accounts: liquidity type is for cash or bank accounts"\
    #     ", payable/receivable is for vendor/customer accounts.")
    # internal_group = fields.Selection([
    #     ('equity', 'Equity'),
    #     ('asset', 'Asset'),
    #     ('liability', 'Liability'),
    #     ('income', 'Income'),
    #     ('expense', 'Expense'),
    #     ('off_balance', 'Off Balance'),
    # ], string="Internal Group",
    #     required=True,
    #     help="The 'Internal Group' is used to filter accounts based on the internal group set on the account type.")
    # note = fields.Text(string='Description')
