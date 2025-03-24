{
    'name': "Personalizaciones Ventas",
    'version': '1.0',
    'summary': "Módulo que agrega límite de ventas al cliente, validación en pedido y reporte de porcentaje",
    'author': "Tu Nombre",
    'category': 'Sales',
    'depends': ['sale', 'base'],
    'data': [
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/sale_order_line_views.xml',
        'views/sale_report_templates.xml',
    ],
    'installable': True,
    'application': False,
}
