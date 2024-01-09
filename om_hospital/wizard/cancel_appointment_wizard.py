import datetime
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res["date_cancel"] = datetime.date.today()
        res["appointment_id"] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancel Date")

    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_("Cancelation is not allowed on the same day of booking"))
        return
        