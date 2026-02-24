# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracFormation(models.Model):
    _name = 'limayrac.formation'
    _description = 'Formation Limayrac'
    _rec_name = 'nom_commercial'

    nom_commercial = fields.Char(string='Nom Commercial', required=True)
    description = fields.Text(string='Description')
    
    # Relations
    titre_rncp_ids = fields.One2many('limayrac.titre.rncp', 'formation_id', string='Titres RNCP')
    besoin_ids = fields.One2many('limayrac.besoin', 'formation_id', string='Besoins')
    responsable_ids = fields.One2many('res.partner', 'formation_responsable_id', string='Responsables')
    
    # Compteurs
    responsable_count = fields.Integer(string='Nombre de responsables', compute='_compute_counts')
    
    @api.depends('responsable_ids')
    def _compute_counts(self):
        for record in self:
            record.responsable_count = len(record.responsable_ids)
