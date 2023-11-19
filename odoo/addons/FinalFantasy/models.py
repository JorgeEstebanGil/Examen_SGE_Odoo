from odoo import api, models, fields

class SHINRA(models.Model):
    _name = 'finalfantasy.shinra'
    nombre = fields.Char()
    fechaNacimiento = fields.Date()

    @api.constrains('fechaNacimiento')
    def _check_fechaNacimiento(self):
        for record in self:
            if record.fechaNacimiento > fields.Date.today():
                raise models.ValidationError("La fecha de nacimiento no puede ser mayor a la fecha actual")
            if record.fechaNacimiento < fields.Date.to_date('1900-01-01'):
                raise models.ValidationError("La fecha de nacimiento no puede ser menor a 1900-01-01")
    
class TURCOS(models.Model):
    __name__ = 'finalfantasy.trucos'
    nombre = fields.Char()
    fechaNacimiento = fields.Date()
    rango = fields.Selection([('soldado','Soldado'),('capitan','Capitan'),('general','General')])

class SOLDADOS(models.Model):
    __name__ = 'finalfantasy.soldados'
    fechaNacimiento = fields.Date()
    armaEspecial = fields.Char()
    clase = fields.Selection([('primera','Primera Clase'),('segunda','Segunda Clase')])
    
    def _check_fechaNacimiento(self):
        for record in self:
            if record.fechaNacimiento > fields.Date.today():
                raise models.ValidationError("La fecha de nacimiento no puede ser mayor a la fecha actual")
            if record.fechaNacimiento < fields.Date.to_date('1900-01-01'):
                raise models.ValidationError("La fecha de nacimiento no puede ser menor a 1900-01-01")

class SOLDADOSPRIMERA(models.Model):
    nombre = fields.Char()
    fechaNacimiento = fields.Date()
    armaEspecial = fields.Char()
    clase = fields.Selection([('primera','Primera Clase'),('segunda','Segunda Clase')])
    mision = fields.Char()
    mision2 = fields.Char()
    mision3 = fields.Char()


