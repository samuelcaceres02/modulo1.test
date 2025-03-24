from odoo import models, fields
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_sales_limit = fields.Float(
        string="Límite de ventas",
        related='partner_id.sales_limit',
        readonly=True
    )

    def action_confirm(self):
        for order in self:
            limit = order.partner_id.sales_limit
            if limit:
                # Total confirmado excluyendo el pedido actual
                confirmed = sum(self.env['sale.order'].search([
                    ('partner_id', '=', order.partner_id.id),
                    ('state', '=', 'sale'),
                    ('id', '!=', order.id)
                ]).mapped('amount_total'))
                if confirmed + order.amount_total > limit:
                    raise UserError(
                        f"El pedido ({order.amount_total:.2f}) + ventas previas ({confirmed:.2f}) "
                        f"supera el límite de crédito ({limit:.2f})."
                    )
        return super().action_confirm()

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_barcode = fields.Char(
        string="Código de Barras",
        related='product_id.barcode',
        readonly=True
    )
