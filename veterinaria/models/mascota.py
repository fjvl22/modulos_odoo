from odoo import models, fields

class Mascota(models.Model):
    _name = 'veterinaria.mascota'
    _description = 'Mascota'

    nombre = fields.Char(string="Nombre", required=True)
    
    especie = fields.Selection([('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otro')], string="Especie", required=True)

    edad = fields.Integer(string="Edad")
    
    dueno = fields.Many2one('veterinaria.dueno', string="Dueño", required=True)
    
    observaciones = fields.Text(string="Observaciones")