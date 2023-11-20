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

    @api.depends('Volumen_Unidad')
    def _compute_disponible(self):
        for cerveza in self:
            cerveza.Disponible = cerveza.Volumen_Unidad > 0

    # Filtros de búsqueda
    def buscar_cervezas_agotadas(self):
        return self.search([('Disponible', '=', False)])

    def buscar_cervezas_disponibles(self):
        return self.search([('Disponible', '>', True)])


    def buscar_por_tipo(self, tipo):
        return self.search([('Tipo', '=', tipo)])

    def buscar_por_contenido_alcohol(self, contenido_alcohol):
        return self.search([('Contenido_Alcohol', '=', contenido_alcohol)])

    def buscar_por_volumen_unidad(self, volumen_unidad):
        return self.search([('Volumen_Unidad', '=', volumen_unidad)])

    def buscar_por_precio_unidad(self, precio_unidad):
        return self.search([('Precio_Unidad', '=', precio_unidad)])

class LOTE_PRODUCCION(models.Model):
    __name__ = 'cerveza.lote_produccion'
    cerveza = fields.Many2one('cerveza.cerveza', 'Cerveza', required=True)
    fecha_inicio = fields.Date('Fecha inicio')
    fecha_fin = fields.Date('Fecha fin')
    cantidad_producida = fields.Integer('Cantidad')
    estado = fields.Selection([('en_proceso', 'En Proceso'), ('completo', 'Completo'), ('en_espera', 'En espera de empaquetado')], 'Estado', default='en proceso')

class INGREDIENTE(models.Model):
    __name__ = 'cerveza.ingrediente'
    name = fields.Char('Nombre', required=True)
    tipo = fields.Selection([('malta', 'Malta'), ('lupulo', 'Lúpulo'), ('levadura', 'Levadura'), ('agua', 'Agua'),('otro','Otro')], 'Tipo', required=True)
    cantidad_disponible = fields.Float('Cantidad disponible (kg/l)')
    cerveza_ids = fields.Many2many('cerveza.cerveza', string='Cervezas')

class EMPAQUETADO(models.Model):
    __name__ = 'cerveza.empaquetado'
    lote_produccion = fields.One2many('cerveza.lote_produccion', 'lote_produccion', 'Lote de producción', required=True)
    fecha_empaquetado = fields.Date('Fecha empaquetado')
    cantidad_empaquetada = fields.Integer('Cantidad empaquetada')

class DISTRIBUIDOR(models.Model):
    __name__ = 'cerveza.distribuidor'
    name = fields.Char('Nombre', required=True) 
    direccion = fields.Char('Dirección', required=True)
    telefono = fields.Char('Teléfono', required=True)
    cervezas_suministradas = fields.Many2many('cerveza.cerveza', string='Cervezas suministradas')
    