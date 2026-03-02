# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracOpportunite(models.Model):
    _name = 'limayrac.opportunite'
    _description = 'Opportunité'
    _rec_name = 'id_opportunite'
    _order = 'create_date desc'

    id_opportunite = fields.Char(string='ID Opportunité', compute='_compute_id_opportunite', store=True)
    
    # Relations
    formation_id = fields.Many2one('limayrac.formation', string='Formation', required=True)
    besoin_id = fields.Many2one('limayrac.besoin', string='Besoin', required=True)
    
    @api.depends('formation_id', 'besoin_id')
    def _compute_id_opportunite(self):
        for record in self:
            if record.formation_id and record.besoin_id:
                record.id_opportunite = f"OPP-{record.formation_id.id}-{record.besoin_id.id}"
            else:
                record.id_opportunite = "Nouveau"
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.formation_id.nom_commercial} - {record.besoin_id.titre}"
            result.append((record.id, name))
        return result
