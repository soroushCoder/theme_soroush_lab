# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Royal Theme',
    'description': 'website theme to customization possibilities.',
    'category': 'Theme/Shoping',
    'sequence': 1000,
    'version': '1.1',
    'depends': ['website','product', 'sale','website_sale','theme_default'],
	'author':'Soroush Ebadi',
    'data': [
        'data/theme_default_data.xml',
        'views/theme_default_templates.xml',  
        'views/ecommerce_snippest_extra.xml',
        'views/website_ecommerce_template_views.xml',
        'views/template.xml'
    ],
    'images': [
        'static/description/cover.png',
        'static/description/theme-soroush.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
