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
    voeux_ids = fields.One2many('limayrac.voeux', 'formation_id', string='Vœux')
    cursus_ids = fields.One2many('limayrac.cursus', 'formation_id', string='Cursus')
    besoin_ids = fields.One2many('limayrac.besoin', 'formation_id', string='Besoins')
    responsable_ids = fields.One2many('res.partner', 'formation_responsable_id', string='Responsables')
    
    # Compteurs
    voeux_count = fields.Integer(string='Nombre de vœux', compute='_compute_counts')
    cursus_count = fields.Integer(string='Nombre de cursus', compute='_compute_counts')
    cursus_actif_count = fields.Integer(string='Cursus actifs', compute='_compute_counts')
    besoin_count = fields.Integer(string='Nombre de besoins', compute='_compute_counts')
    responsable_count = fields.Integer(string='Nombre de responsables', compute='_compute_counts')
    
    @api.depends('voeux_ids', 'cursus_ids', 'besoin_ids', 'responsable_ids')
    def _compute_counts(self):
        for record in self:
            record.voeux_count = len(record.voeux_ids)
            record.cursus_count = len(record.cursus_ids)
            record.cursus_actif_count = len(record.cursus_ids.filtered(lambda c: not c.is_diplome and not c.date_fin))
            record.besoin_count = len(record.besoin_ids)
            record.responsable_count = len(record.responsable_ids)
