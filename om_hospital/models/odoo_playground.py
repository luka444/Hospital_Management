from odoo import fields, models, api


class OdooPlayground(models.Model):
    _name = "odoo.playground"
    _description = "Odoo Playground"

    model_id = fields.Many2one("ir.model")
    code = fields.Text()
    result = fields.Text()