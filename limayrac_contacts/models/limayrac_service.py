# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracService(models.Model):
    _name = 'limayrac.service'
    _description = 'Service dans une structure'
    _rec_name = 'type_service'

    type_service = fields.Char(string='Type de Service', required=True)
    structure_id = fields.Many2one('res.partner', string='Structure', 
                                   domain=[('is_company', '=', True)],
                                   required=True)
    siret = fields.Char(related='structure_id.siret', string='SIRET', store=True, readonly=True)
    
    is_active = fields.Boolean(string='Actif', default=True)
    is_blacklist = fields.Boolean(string='Liste noire', default=False)
    
    date_created = fields.Datetime(string='Date de création', default=fields.Datetime.now, readonly=True)
    date_updated = fields.Datetime(string='Date de mise à jour', readonly=True)
    
    # Personnes liées à ce service
    personne_ids = fields.One2many('res.partner', 'service_id', string='Personnes')
    
    # Contrats liés à ce service
    contrat_ids = fields.One2many('limayrac.contrat', 'service_id', string='Contrats')
    
    @api.model
    def create(self, vals):
        vals['date_created'] = fields.Datetime.now()
        return super(LimayracService, self).create(vals)
    
    def write(self, vals):
        vals['date_updated'] = fields.Datetime.now()
        return super(LimayracService, self).write(vals)
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.type_service} - {record.structure_id.name}"
            result.append((record.id, name))
        return result
