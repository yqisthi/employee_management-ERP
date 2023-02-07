from odoo import api, fields, models

class ManagementEmployee(models.Model):
    _name = "management.employee"
    _description = "Employee"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),], 
        string="Gender")
