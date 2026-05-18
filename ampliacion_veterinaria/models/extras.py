from odoo import api
from odoo.exceptions import ValidationError

from mascota import Mascota

@api.constrains('peso')
def _validar_peso(self):

    for mascota in self:

        if mascota.peso <= 0:

            raise ValidationError("El peso debe ser mayor que 0.")
        
Mascota._validar_peso = _validar_peso