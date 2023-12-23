from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Hospital Appointment'
    _rec_name = "name"

    name = fields.Char()
    patient_id = fields.Many2one("hospital.patient", string="Patient")
    reference = fields.Char(string="Reference")
    gender = fields.Selection(string='Gender', related="patient_id.gender")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection(
        selection=[
            ("0", "Low"),
            ("1", "Medium"),
            ("2", "High"),
            ("3", "Very High")])
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("in_consultation", "In Consultation"),
            ("done", "Done"),
            ("cancel", "Cancelled")], default="draft", string="Status", required=True)
    
    @api.onchange("patient_id")
    def onchange_patient_id(self):
        self.reference = self.patient_id.reference
        