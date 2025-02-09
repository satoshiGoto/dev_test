# -*- coding: utf-8 -*-

from odoo import models, fields, api


class interfaces_custom_module_res_partner_inheritance(models.Model):
    _inherit = 'res.partner'

    sale_limit = fields.Float(string="Límite de monto de ventas")

