from odoo import fields, models
class AulaStockLocation(models.Model):
    _name = "aulastock.location"
    _description = "Ubicación de material"
    _order = "name asc"

    name = fields.Char(string="Nombre", required=True)
    room = fields.Char(string="Código / Referencia")
    notes = fields.Text(string="Observaciones")
    active = fields.Boolean(default=True)
    item_ids = fields.One2many(
        comodel_name="aulastock.item",
        inverse_name="location_id",
        string="Materiales"
    )