from odoo import models, fields, api

class CERVEZA(models.Model):
    _name = 'cerveza.cerveza'
    name = fields.Char('Nombre', required=True)
    tipo = fields.Char('Tipo', required=True)
    Description = fields.Text('Descripcion')
    Alcohol = fields.Float('Alcohol %')
    Precio_unidad = fields.Float('Precio unidad')
    Volumen_unidad = fields.Float('Volumen unidad (ml)')
    Disponible = fields.Boolean('Disponible', compute='_compute_disponible', store=True)

    @api.depends('Volumen_unidad')
    def _compute_disponible(self):
        for cerveza in self:
            cerveza.Disponible = cerveza.Volumen_unidad > 0

    # Filtros de búsqueda
    def buscar_cervezas_agotadas(self):
        return self.search([('Disponible', '=', False)])

    def buscar_cervezas_disponibles(self):
        return self.search([('Disponible', '>', True)])


    def buscar_por_tipo(self, tipo):
        return self.search([('Tipo', '=', tipo)])

    def buscar_por_contenido_alcohol(self, contenido_alcohol):
        return self.search([('Alcohol', '=', contenido_alcohol)])

    def buscar_por_volumen_unidad(self, volumen_unidad):
        return self.search([('Volumen_unidad', '=', volumen_unidad)])

    def buscar_por_precio_unidad(self, precio_unidad):
        return self.search([('Precio_Unidad', '=', precio_unidad)])

class LOTE_PRODUCCION(models.Model):
    _name = 'cerveza.lote_produccion'
    lote_produccion_ids = fields.Many2one('cerveza.cerveza', 'Cerveza', required=True)
    fecha_inicio = fields.Date('Fecha inicio')
    fecha_fin = fields.Date('Fecha fin')
    cantidad_producida = fields.Integer('Cantidad')
    estado = fields.Selection([('en_proceso', 'En Proceso'), ('completo', 'Completo'), ('en_espera', 'En espera de empaquetado')], 'Estado', default='en proceso')


class INGREDIENTE(models.Model):
    _name= 'cerveza.ingrediente'
    name = fields.Char('Nombre', required=True)
    tipo = fields.Selection([('malta', 'Malta'), ('lupulo', 'Lúpulo'), ('levadura', 'Levadura'), ('agua', 'Agua'),('otro','Otro')], 'Tipo', required=True)
    cantidad_disponible = fields.Float('Cantidad disponible (kg/l)')
    cerveza_ids = fields.Many2many('cerveza.cerveza', string='Cervezas')

class EMPAQUETADO(models.Model):
    _name = 'cerveza.empaquetado'
    lote_produccion_id = fields.Many2one('cerveza.lote_produccion', 'Lote de producción', required=True)
    fecha_empaquetado = fields.Date('Fecha empaquetado')
    cantidad_empaquetada = fields.Integer('Cantidad empaquetada')


class DISTRIBUIDOR(models.Model):
    _name = 'cerveza.distribuidor'
    name = fields.Char('Nombre', required=True) 
    direccion = fields.Char('Dirección', required=True)
    telefono = fields.Char('Teléfono', required=True)
    cervezas_suministradas = fields.Many2many('cerveza.cerveza', string='Cervezas suministradas')
    