from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    sales_limit = fields.Float(
        string="Límite de monto de ventas",
        help="Define el límite máximo de ventas asignado al cliente."
    )
    credit_used = fields.Float(
        string="Crédito usado",
        compute="_compute_credit_used",
        readonly=True
    )

    @api.depends('sales_limit')
    def _compute_credit_used(self):
        for partner in self:
            orders = self.env['sale.order'].search([
                ('partner_id', '=', partner.id),
                ('state', '=', 'sale')
            ])
            partner.credit_used = sum(orders.mapped('amount_total'))
