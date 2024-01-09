from datetime import date
from odoo import api, fields, models



class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    reference = fields.Char(string="Reference")
    age = fields.Integer(string='Age', compute="_compute_age", tracking=True, store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(default=True)
    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many("patient.tag", string="Tags")

    @api.model
    def create(self, vals):
        vals["reference"] =  self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    @api.depends("date_of_birth")
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year - ((today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 1
    