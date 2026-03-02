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
    
    # Type de contrat souhaité (détermine le workflow)
    type_contrat_souhaite = fields.Selection([
        ('stage', 'Stage'),
        ('alternance', 'Alternance (Apprentissage/Pro)')
    ], string='Type de contrat souhaité', required=True, default='alternance', tracking=True)
    
    # Workflow - États basés sur le processus de candidature
    state = fields.Selection([
        ('nouveau', 'Portail candidature'),
        ('cfp_validation', 'CFP - Validation importation'),
        ('rp_evaluation', 'RP - Évaluation dossier'),
        ('cfp_rdv_jury', 'CFP - Date RDV Jury'),
        ('rp_passage_jury', 'RP - Passage Jury'),
        # Branche Alternance
        ('sre_mission', 'SRE - Entretien + Mission (Alternance)'),
        ('rp_validation_mission_alternance', 'RP - Validation mission (Alternance)'),
        ('sre_validation_contrat', 'SRE - Validation contrat (Alternance)'),
        # Branche Stage
        ('rp_validation_mission_stage', 'RP - Validation mission (Stage)'),
        # Fin
        ('accepte', 'Accepté - Contrat/Convention généré'),
        ('refuse', 'Refusé'),
        ('annule', 'Annulé')
    ], string='État', default='nouveau', required=True, tracking=True)
    
    # Date de RDV Jury
    date_rdv_jury = fields.Datetime(string='Date RDV Jury')
    
    # Notes et commentaires (TEXTE)
    description_mission = fields.Text(string='Description de la mission')
    note_rp = fields.Text(string='Note RP (Commentaire)')
    note_cfp = fields.Text(string='Note CFP (Commentaire)')
    note_sre = fields.Text(string='Note SRE (Commentaire)')
    note_jury = fields.Text(string='Note Jury (Commentaire)')
    
    # Indicateurs booléens
    is_besoin = fields.Boolean(string='Lié à un besoin', default=False)
    is_kairos = fields.Boolean(string='Kaïros', default=False)
    is_alternant = fields.Boolean(string='Alternant', default=False)
    is_presence_coaching = fields.Boolean(string='Présence Coaching', default=False)
    
    # Date du jury
    date_jury = fields.Date(string='Date du Jury')
    
    # Notes de questions (CHIFFRES)
    note_q1 = fields.Float(string='Note Question 1', digits=(3, 2))
    note_q2 = fields.Float(string='Note Question 2', digits=(3, 2))
    note_q3 = fields.Float(string='Note Question 3', digits=(3, 2))
    note_q4 = fields.Float(string='Note Question 4', digits=(3, 2))
    note_q5 = fields.Float(string='Note Question 5', digits=(3, 2))
    
    # Moyenne des notes de questions
    note_moyenne = fields.Float(string='Note Moyenne', compute='_compute_note_moyenne', store=True)
    
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
    
    @api.depends('note_q1', 'note_q2', 'note_q3', 'note_q4', 'note_q5')
    def _compute_note_moyenne(self):
        for record in self:
            notes = [record.note_q1, record.note_q2, record.note_q3, record.note_q4, record.note_q5]
            notes_valides = [n for n in notes if n > 0]
            if notes_valides:
                record.note_moyenne = sum(notes_valides) / len(notes_valides)
            else:
                record.note_moyenne = 0.0
    
    @api.model
    def create(self, vals):
        # Marquer automatiquement la personne comme candidat
        if vals.get('apprenant_id'):
            apprenant = self.env['res.partner'].browse(vals['apprenant_id'])
            apprenant.write({'is_candidat': True})
        return super(LimayracVoeux, self).create(vals)
    
    # ========== Actions du Workflow ==========
    
    def action_cfp_valider_importation(self):
        """CFP: Valider l'importation du dossier"""
        self.write({'state': 'rp_evaluation'})
    
    def action_rp_evaluer_dossier(self):
        """RP: Évaluer le dossier et envoyer au CFP pour RDV jury"""
        self.write({'state': 'cfp_rdv_jury'})
    
    def action_cfp_fixer_rdv_jury(self):
        """CFP: Fixer la date du RDV jury"""
        # La date doit être remplie avant de passer à l'étape suivante
        if not self.date_rdv_jury:
            from odoo.exceptions import ValidationError
            raise ValidationError("Veuillez définir la date du RDV jury avant de continuer.")
        self.write({'state': 'rp_passage_jury'})
    
    def action_rp_passage_jury(self):
        """RP: Passage du jury - orientation selon le type de contrat"""
        # Si c'est un stage, on va directement à la validation mission stage
        if self.type_contrat_souhaite == 'stage':
            self.write({'state': 'rp_validation_mission_stage'})
        else:  # alternance
            self.write({'state': 'sre_mission'})
    
    # ========== Parcours ALTERNANCE ==========
    
    def action_sre_entretien_mission(self):
        """SRE: Entretien + coaching + renseignement mission (Alternance)"""
        self.write({'state': 'rp_validation_mission_alternance'})
    
    def action_rp_valider_mission_alternance(self):
        """RP: Validation de la mission (Alternance)"""
        self.write({'state': 'sre_validation_contrat'})
    
    def action_sre_valider_contrat(self):
        """SRE: Validation signature contrat et génération du contrat/CERFA (Alternance)"""
        self.write({'state': 'accepte'})
        # Proposer de créer un contrat d'alternance
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'limayrac.contrat',
            'view_mode': 'form',
            'context': {
                'default_apprenant_id': self.apprenant_id.id,
                'default_service_id': self.entreprise_id.service_ids[0].id if self.entreprise_id and self.entreprise_id.service_ids else False,
                'default_type_contrat': 'apprentissage',
                'default_description_mission': self.description_mission,
            },
            'target': 'current',
        }
    
    # ========== Parcours STAGE ==========
    
    def action_rp_valider_mission_stage(self):
        """RP: Validation mission et génération convention de stage (Stage)"""
        self.write({'state': 'accepte'})
        # Proposer de créer une convention de stage
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'limayrac.contrat',
            'view_mode': 'form',
            'context': {
                'default_apprenant_id': self.apprenant_id.id,
                'default_service_id': self.entreprise_id.service_ids[0].id if self.entreprise_id and self.entreprise_id.service_ids else False,
                'default_type_contrat': 'stage',
                'default_description_mission': self.description_mission,
            },
            'target': 'current',
        }
    
    def action_refuser_dossier(self):
        """Refuser le dossier (peut être fait à plusieurs étapes)"""
        self.write({'state': 'refuse'})
    
    def action_annuler(self):
        """Annuler la candidature"""
        self.write({'state': 'annule'})
    
    def action_reinitialiser(self):
        """Réinitialiser au début du workflow"""
        self.write({'state': 'nouveau'})
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.apprenant_id.name} - {record.formation_id.nom_commercial}"
            result.append((record.id, name))
        return result
