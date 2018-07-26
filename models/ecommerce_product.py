# -*- coding: utf-8 -*-
from odoo import fields, models
class EcommerceProducts(models.Model):
    _inherit = 'product.template'
    fetures_product = fields.Boolean('fetures_product', default=True)
    recommended_product = fields.Boolean("recommended_product", default=True)
    shop_product = fields.Boolean('shop_product', default=True)
class Website(models.Model):
    _inherit = 'website'
    def get_recommended_products(self):

        recommended_products_ids = self.env['product.template'].search([('recommended_product', '=', True)])
        return recommended_products_ids
    def get_recommended_length(self):
        r_length = []
        r_items_is = []
        count = 1

        recommended_products_ids = self.env['product.template'].search([('recommended_product', '=', True)])
        for record in recommended_products_ids:
            con = count % 3
            r_length.append(record)
            if con == 0:
                r_items_is.append(r_length)
                r_length = []

            count = count + 1
        con = count % 3
        if con != 1:
            r_items_is.append(r_length)
        return r_items_is
