from odoo import models, fields

class Dueno(models.Model):
    _name = 'veterinaria.dueno'
    _description = 'Dueño de Mascota'

    nombre = fields.Char(string="Nombre", required=True)
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")

    mascota_ids = fields.One2many('veterinaria.mascota', 'dueno_id', string="Mascotas")