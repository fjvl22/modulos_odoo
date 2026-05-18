from odoo import models, fields, api
from datetime import date

class Mascota(models.Model):
    _name = 'veterinaria.mascota'
    _description = 'Mascota'

    nombre = fields.Char(string="Nombre", required=True)
    
    especie = fields.Selection([('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otro')], string="Especie", required=True)

    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")

    edad = fields.Integer(string="Edad", compute="_calcular_edad", store=True)

    peso = fields.Float(string="Peso (kg)")

    vacunado = fields.Boolean(string="Vacunado")

    fecha_registro = fields.Date(string="Fecha de registro", default=fields.Date.today, readonly=True)
    
    dueno_id = fields.Many2one('veterinaria.dueno', string="Dueño", required=True)
    
    observaciones = fields.Text(string="Observaciones")

    @api.depends('fecha_nacimiento')
    def _calcular_edad(self):

        for mascota in self:

            if mascota.fecha_nacimiento:

                hoy = date.today()

                mascota.edad = (hoy.year - mascota.fecha_nacimiento.year)

            else:

                mascota.edad = 0