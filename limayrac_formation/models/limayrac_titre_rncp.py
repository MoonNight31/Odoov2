# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracTitreRNCP(models.Model):
    _name = 'limayrac.titre.rncp'
    _description = 'Titre RNCP'
    _rec_name = 'code_rncp'

    code_rncp = fields.Char(string='Code RNCP', required=True)
    intitule = fields.Char(string='Intitulé', required=True)
    date_debut = fields.Date(string='Date de début')
    date_fin = fields.Date(string='Date de fin')
    
    formation_id = fields.Many2one('limayrac.formation', string='Formation', required=True)
    
    is_active = fields.Boolean(string='Actif', compute='_compute_is_active', store=True)
    
    @api.depends('date_debut', 'date_fin')
    def _compute_is_active(self):
        today = fields.Date.today()
        for record in self:
            if record.date_debut and record.date_fin:
                record.is_active = record.date_debut <= today <= record.date_fin
            elif record.date_debut:
                record.is_active = record.date_debut <= today
            elif record.date_fin:
                record.is_active = today <= record.date_fin
            else:
                record.is_active = True
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.code_rncp} - {record.intitule}"
            result.append((record.id, name))
        return result
