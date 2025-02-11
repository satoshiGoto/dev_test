# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class interfaces_custom_module_sale_order_inheritance(models.Model):
    _inherit = 'sale.order'

    sale_limit = fields.Float(string="Límite de monto de ventas", related="partner_id.sale_limit")

    #Método encargado de verificar que el monto de la venta no sobrepase el límite de venta
    def action_confirm(self):
        for rec in self:
            if rec.amount_total > (rec.sale_limit*1.2):
                raise UserError(f"El monto límite de venta es de {rec.sale_limit:,.2f} {rec.order_line.currency_id.symbol}")

        result = super(interfaces_custom_module_sale_order_inheritance, self).action_confirm()

        return result

    #Método encargado de calcular el porcentaje de crédito de la venta respecto al límite de venta
    def _sale_limit_porcentage(self):
        for rec in self:
            if rec.sale_limit and rec.sale_limit != 0:
                return round(((rec.amount_total/rec.sale_limit)*100), 1)
