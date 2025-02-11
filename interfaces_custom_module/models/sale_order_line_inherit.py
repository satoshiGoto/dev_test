# -*- coding: utf-8 -*-

from odoo import models, fields, api


class interfaces_custom_module_sale_order_line_inheritance(models.Model):
    _inherit = 'sale.order.line'

    bar_code = fields.Char(string="Código de barra", related='product_id.barcode')
    reference = fields.Char(string="Referencia Interna", related="product_id.default_code")



