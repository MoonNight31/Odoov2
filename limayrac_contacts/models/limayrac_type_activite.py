# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracTypeActivite(models.Model):
    _name = 'limayrac.type.activite'
    _description = "Type d'activité"
    _rec_name = 'intitule'

    intitule = fields.Char(string='Intitulé', required=True)
    description = fields.Text(string='Description')
    
    # Relations
    service_ids = fields.Many2many('limayrac.service', string='Services')
    
    @api.model
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.intitule))
        return result
