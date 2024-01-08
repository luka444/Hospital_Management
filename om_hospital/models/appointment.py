from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Hospital Appointment'
    _rec_name = "name"

    name = fields.Char()
    patient_id = fields.Many2one("hospital.patient", string="Patient")
    reference = fields.Char(string="Reference", help="Reference from patient record")
    gender = fields.Selection(string='Gender', related="patient_id.gender")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today, help="Date of booking")
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
    doctor_id = fields.Many2one("res.users", string="Doctor")
    pharmacy_line_ids = fields.One2many("appointment.pharmacy.lines", "appointment_id", string="Pharmacy Lines")
    hide_sales_price = fields.Boolean(string="Hide Sales Price")
    
    @api.onchange("patient_id")
    def onchange_patient_id(self):
        self.reference = self.patient_id.reference

    def action_test(self):
        print("Button clicked !!!!!!!")
        return {
            "effect":{
                "fadeout": "slow",
                "message": "Button clicked",
                "type": "rainbow_man",
                "img_url": "om_hospital/static/description/icon.png"
            }
        }
    
    def action_in_consultation(self):
        for rec in self:
            rec.state = "in_consultation"
    
    def action_done(self):
        for rec in self:
            rec.state = "done"
    
    def action_canel(self):
        action = self.env.ref('om_hospital.cancel_appointment_wizard_action').read()[0]
        return action

    def action_draft(self):
        for rec in self:
            rec.state = "draft"
