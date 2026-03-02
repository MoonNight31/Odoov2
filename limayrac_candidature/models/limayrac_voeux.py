# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracVoeux(models.Model):
    _name = 'limayrac.voeux'
    _description = 'Candidature / Vœux'
    _rec_name = 'apprenant_id'
    _order = 'date_candidature desc'

    # Identifiant
    id_voeux = fields.Char(string='ID Vœux', compute='_compute_id_voeux', store=True)
    
    # Relation avec le candidat (PERSONNE)
    apprenant_id = fields.Many2one('res.partner', string='Candidat', 
                                   domain=[('is_candidat', '=', True)],
                                   required=True)
    
    # Informations principales
    date_candidature = fields.Date(string='Date de candidature', default=fields.Date.today, required=True)
    
    # Statuts
    statut_dossier = fields.Selection([
        ('nouveau', 'Nouveau'),
        ('en_cours', 'En cours d\'examen'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
        ('annule', 'Annulé')
    ], string='Statut du dossier', default='nouveau', required=True)
    
    statut_SRE = fields.Selection([
        ('a_traiter', 'À traiter'),
        ('en_cours', 'En cours'),
        ('valide', 'Validé'),
        ('refuse', 'Refusé')
    ], string='Statut SRE', default='a_traiter')
    
    # Notes et commentaires (TEXTE)
    description_mission = fields.Text(string='Description de la mission')
    Note_RP = fields.Text(string='Note RP (Commentaire)')
    Note_CFP = fields.Text(string='Note CFP (Commentaire)')
    Note_SRE = fields.Text(string='Note SRE (Commentaire)')
    Note_Jury = fields.Text(string='Note Jury (Commentaire)')
    
    # Indicateurs booléens
    is_besoin = fields.Boolean(string='Lié à un besoin', default=False)
    is_kairos = fields.Boolean(string='Kaïros', default=False)
    is_alternant = fields.Boolean(string='Alternant', default=False)
    is_presenceCoaching = fields.Boolean(string='Présence Coaching', default=False)
    
    # Date du jury
    Date_Jury = fields.Date(string='Date du Jury')
    
    # Notes de questions (CHIFFRES)
    Note_Q1 = fields.Float(string='Note Question 1', digits=(3, 2))
    Note_Q2 = fields.Float(string='Note Question 2', digits=(3, 2))
    Note_Q3 = fields.Float(string='Note Question 3', digits=(3, 2))
    Note_Q4 = fields.Float(string='Note Question 4', digits=(3, 2))
    Note_Q5 = fields.Float(string='Note Question 5', digits=(3, 2))
    
    # Moyenne des notes de questions
    Note_Moyenne = fields.Float(string='Note Moyenne', compute='_compute_note_moyenne', store=True)
    
    # Relations avec les jurys (PERSONNE)
    jury1_id = fields.Many2one('res.partner', string='Jury 1', 
                               domain=[('is_intervenant', '=', True)])
    jury2_id = fields.Many2one('res.partner', string='Jury 2', 
                               domain=[('is_intervenant', '=', True)])
    
    # Relation avec la formation
    formation_id = fields.Many2one('limayrac.formation', string='Formation', required=True)
    
    # Relation avec l'entreprise (STRUCTURE)
    entreprise_id = fields.Many2one('res.partner', string='Entreprise', 
                                    domain=[('is_company', '=', True)])
    
    # Relation avec le type d'activité
    activite_id = fields.Many2one('limayrac.type.activite', string='Type d\'activité')
    
    # Informations du candidat (dupliquées pour facilité)
    email = fields.Char(related='apprenant_id.email', string='Email', readonly=True)
    phone = fields.Char(related='apprenant_id.phone', string='Téléphone', readonly=True)
    
    @api.depends('apprenant_id', 'formation_id', 'date_candidature')
    def _compute_id_voeux(self):
        for record in self:
            if record.apprenant_id and record.formation_id:
                year = record.date_candidature.year if record.date_candidature else ''
                record.id_voeux = f"V-{record.formation_id.id}-{record.apprenant_id.id}-{year}"
            else:
                record.id_voeux = "Nouveau"
    
    @api.depends('Note_Q1', 'Note_Q2', 'Note_Q3', 'Note_Q4', 'Note_Q5')
    def _compute_note_moyenne(self):
        for record in self:
            notes = [record.Note_Q1, record.Note_Q2, record.Note_Q3, record.Note_Q4, record.Note_Q5]
            notes_valides = [n for n in notes if n > 0]
            if notes_valides:
                record.Note_Moyenne = sum(notes_valides) / len(notes_valides)
            else:
                record.Note_Moyenne = 0.0
    
    @api.model
    def create(self, vals):
        # Marquer automatiquement la personne comme candidat
        if vals.get('apprenant_id'):
            apprenant = self.env['res.partner'].browse(vals['apprenant_id'])
            apprenant.write({'is_candidat': True})
        return super(LimayracVoeux, self).create(vals)
    
    def action_accepter(self):
        """Accepter le vœu et proposer de créer un cursus"""
        self.write({'statut_dossier': 'accepte'})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'limayrac.cursus',
            'view_mode': 'form',
            'context': {
                'default_apprenant_id': self.apprenant_id.id,
                'default_formation_id': self.formation_id.id,
            },
            'target': 'current',
        }
    
    def action_refuser(self):
        """Refuser le vœu"""
        self.write({'statut_dossier': 'refuse'})
    
    def action_annuler(self):
        """Annuler le vœu"""
        self.write({'statut_dossier': 'annule'})
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.apprenant_id.name} - {record.formation_id.nom_commercial}"
            result.append((record.id, name))
        return result
