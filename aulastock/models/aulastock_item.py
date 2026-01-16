from odoo import fields, models
class AulaStockItem(models.Model):
    _name = "aulastock.item"
    _description = "Material del aula"
    _order = "name asc"

    name = fields.Char(string="Nombre",required=True)
    code = fields.Char(string="Código")
    category = fields.Selection(
        [
            ("periferico","Periférico"),
            ("cable","Cable"),
            ("componente","Componente"),
            ("otro","Otro"),
        ],
        string="Categoría",
        default="otro",
        required=True,
    )
    quantity = fields.Integer(string="Unidades",default=1)
    price = fields.Float(string="Precio unitario")
    purchase_date = fields.Date(string="Fecha de compra")
    active = fields.Boolean(default=True)
    notes = fields.Text(string="Observaciones")
    location_id = fields.Many2one(
        comodel_name="aulastock.location",
        string="Ubicación"
    )