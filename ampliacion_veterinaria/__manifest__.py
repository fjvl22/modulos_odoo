{
    'name': 'Veterinaria',
    'version': '2.0',
    'summary': 'Versión ampliada de la gestión de mascotas y dueños en veterinaria',
    'author': 'odoo17',
    'category': 'Services',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/veterinaria_views.xml',
    ],
    'installable': True,
    'application': True,
}