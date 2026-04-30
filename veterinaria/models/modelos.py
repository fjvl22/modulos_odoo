from odoo import models, fields

class Dueno(models.Model):
    _name = 'veterinaria.dueno'
    _description = 'Dueño de Mascota'

    nombre = fields.Char(string="Nombre", required=True)
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")

    mascota_ids = fields.One2many('veterinaria.mascota', 'dueno_id', string="Mascotas")

class Mascota(models.Model):
    _name = 'veterinaria.mascota',
    _description = 'Mascota'

    nombre = fields.Char(string="Nombre", required=True)


    especie = fields.Selection([('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otro')], string="Especie", required=True)

    edad = fields.Integer(string="Edad")

    dueno_id = fields.Many2one('veterinaria.dueno', string="Dueño", required=True)

    observaciones = fields.Text(string="Observaciones")