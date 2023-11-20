from odoo import models, fields, api

class CERVEZA(models.Model):
    __name__ = 'cerveza.cerveza'
    name = fields.Char('Nombre', required=True)
    tipo = fields.Char('Tipo', required=True)
    Description = fields.Text('Descripcion')
    Alcohol = fields.Float('Alcohol %')
    Precio_unidad = fields.Float('Precio unidad')
    Volumen_unidad = fields.Float('Volumen unidad (ml)')
    Disponible = fields.Boolean('Disponible', compute='_compute_disponible', store=True)
    #Realiza un filtro de búsqueda para conocer las cervezas agotadas
    #Realiza un filtro de búsqueda para conocer las cervezas disponibles
    #Debes permitir buscar por Tipo, Contenido de alcohol, Volumen por unidad, Precio por unidad

    @api.depends('Disponible')
    def _compute_disponible(self):
        for cerveza in self:
            if cerveza.Alcohol > 0:
                cerveza.Disponible = True
            else:
                cerveza.Disponible = False

class LOTE_PRODUCCION(models.Model):
    __name__ = 'cerveza.lote_produccion'
    cerveza = fields.Many2one('cerveza.cerveza', 'Cerveza', required=True)
    fecha_inicio = fields.Date('Fecha inicio')
    fecha_fin = fields.Date('Fecha fin')
    cantidad = fields.Integer('Cantidad')
    estado = fields.Selection([('en proceso', 'En Proceso'), ('completo', 'Completo'), ('enEsperadeEmpaquetado', 'En espera de empaquetado')], 'Estado', default='en proceso')
#En el calendario se mostrarán los lotes de producción según la fecha de inicio, y su fecha de finalización








