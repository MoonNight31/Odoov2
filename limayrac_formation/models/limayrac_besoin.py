# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracBesoin(models.Model):
    _name = 'limayrac.besoin'
    _description = 'Besoin en formation d\'une structure'
    _rec_name = 'titre'
    _order = 'date desc'

    titre = fields.Char(string='Titre', required=True)
    description = fields.Text(string='Description')
    poste = fields.Char(string='Poste')
    date = fields.Date(string='Date', default=fields.Date.today, required=True)
    
    # Relations avec formation via opportunités
    formation_ids = fields.Many2many('limayrac.formation', 'limayrac_opportunite', 'besoin_id', 'formation_id', string='Formations')
    opportunite_ids = fields.One2many('limayrac.opportunite', 'besoin_id', string='Opportunités')
    
    # Relation avec structure
    structure_id = fields.Many2one('res.partner', string='Structure', 
                                   domain=[('is_company', '=', True)],
                                   required=True)
    
    state = fields.Selection([
        ('nouveau', 'Nouveau'),
        ('en_cours', 'En cours'),
        ('traite', 'Traité'),
        ('annule', 'Annulé')
    ], string='État', default='nouveau', required=True)
    
    notes = fields.Text(string='Notes')
