import datetime
from odoo import fields, models, api


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res["date_cancel"] = datetime.date.today()
        return res

    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancel Date")

    def action_cancel(self):
        return
        