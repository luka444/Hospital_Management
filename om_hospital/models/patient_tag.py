from odoo import fields, models


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char()
    active = fields.Boolean(default=True)
    color = fields.Integer()
    color_2 = fields.Char(string="Color")
