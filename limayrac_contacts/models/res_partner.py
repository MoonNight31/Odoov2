# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Champs spécifiques pour les personnes
    poste = fields.Char(string='Poste')
    is_alumni = fields.Boolean(string='Alumni', default=False)
    is_candidat = fields.Boolean(string='Candidat', default=False)
    is_apprenant = fields.Boolean(string='Apprenant', default=False)
    is_intervenant = fields.Boolean(string='Intervenant', default=False)
    is_tuteur = fields.Boolean(string='Tuteur', default=False)
    
    # Relation avec le service (pour les personnes)
    service_id = fields.Many2one('limayrac.service', string='Service')
    
    # Responsable de formation
    formation_responsable_id = fields.Many2one('limayrac.formation', string='Formation (Responsable)')
    
    # Champs spécifiques pour les structures (entreprises)
    siret = fields.Char(string='SIRET', size=14)
    raison_sociale = fields.Char(string='Raison Sociale')
    code_naf = fields.Char(string='Code NAF', size=5)
    site_web = fields.Char(string='Site Web')
    is_blacklist = fields.Boolean(string='Liste noire', default=False)
    is_partenaire = fields.Boolean(string='Partenaire', default=False)
    is_taxe_apprentissage = fields.Boolean(string='Taxe d\'apprentissage', default=False)
    is_prospect = fields.Boolean(string='Prospect', default=False)
    
    # Relation avec le groupe de structures
    groupe_structure_id = fields.Many2one('limayrac.groupe.structure', string='Groupe')
    
    # Services liés à cette structure
    service_ids = fields.One2many('limayrac.service', 'structure_id', string='Services')
    
    @api.model
    def create(self, vals):
        # Si c'est une structure et qu'elle a un SIRET, extraire le SIREN
        if vals.get('is_company') and vals.get('siret') and len(vals['siret']) >= 9:
            siren = vals['siret'][:9]
            # Chercher ou créer le groupe structure correspondant
            groupe = self.env['limayrac.groupe.structure'].search([('siren', '=', siren)], limit=1)
            if not groupe:
                groupe = self.env['limayrac.groupe.structure'].create({
                    'siren': siren,
                    'name': vals.get('raison_sociale') or vals.get('name', 'Groupe ' + siren),
                })
            vals['groupe_structure_id'] = groupe.id
        
        return super(ResPartner, self).create(vals)
