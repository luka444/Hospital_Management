from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    confirmed_user_id = fields.Many2one("res.users", readonly=True, help="This field will be set with the current user when the Confirm button is clicked")

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        self.confirmed_user_id = self.env.user.id
        