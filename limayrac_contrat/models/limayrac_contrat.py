# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LimayracContrat(models.Model):
    _name = 'limayrac.contrat'
    _description = 'Contrat d\'apprentissage/alternance'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'date_debut desc'

    name = fields.Char(string='Référence', compute='_compute_name', store=True)
    
    # Informations principales du contrat
    type_contrat = fields.Selection([
        ('apprentissage', 'Contrat d\'apprentissage'),
        ('professionnalisation', 'Contrat de professionnalisation'),
        ('stage', 'Convention de stage'),
    ], string='Type de contrat', required=True, tracking=True)
    
    type_activite = fields.Char(string='Type d\'activité', tracking=True)
    
    date_debut = fields.Date(string='Date de début', required=True, tracking=True)
    date_fin = fields.Date(string='Date de fin', tracking=True)
    
    # Relations principales
    apprenant_id = fields.Many2one('res.partner', string='Apprenant', 
                                   domain=[('is_apprenant', '=', True)],
                                   required=True)
    cursus_id = fields.Many2one('limayrac.cursus', string='Cursus')
    formation_id = fields.Many2one(related='cursus_id.formation_id', string='Formation', store=True, readonly=True)
    
    service_id = fields.Many2one('limayrac.service', string='Service', required=True)
    structure_id = fields.Many2one(related='service_id.structure_id', string='Structure', store=True, readonly=True)
    
    # Tuteurs (2 tuteurs entreprise + 1 tuteur école)
    tuteur_entreprise_id = fields.Many2one('res.partner', string='Tuteur Entreprise 1', 
                                          domain=[('is_tuteur', '=', True)], tracking=True)
    tuteur_entreprise2_id = fields.Many2one('res.partner', string='Tuteur Entreprise 2', 
                                           domain=[('is_tuteur', '=', True)], tracking=True)
    tuteur_ecole_id = fields.Many2one('res.partner', string='Tuteur École', 
                                     domain=[('is_intervenant', '=', True)], tracking=True)
    
    # Notation et suivi
    notation = fields.Selection([
        ('1', 'Très insatisfaisant'),
        ('2', 'Insatisfaisant'),
        ('3', 'Moyen'),
        ('4', 'Satisfaisant'),
        ('5', 'Excellent'),
    ], string='Notation', tracking=True)
    
    commentaire = fields.Text(string='Commentaire')
    
    # État du contrat
    state = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('rompu', 'Rompu'),
    ], string='État', compute='_compute_state', store=True)
    
    @api.depends('apprenant_id', 'structure_id', 'date_debut')
    def _compute_name(self):
        for record in self:
            if record.apprenant_id and record.structure_id:
                year = record.date_debut.year if record.date_debut else ''
                record.name = f"{record.apprenant_id.name} - {record.structure_id.name} ({year})"
            else:
                record.name = "Nouveau contrat"
    
    @api.depends('date_debut', 'date_fin')
    def _compute_state(self):
        today = fields.Date.today()
        for record in self:
            if not record.date_debut:
                record.state = 'brouillon'
            elif record.date_fin and record.date_fin < today:
                record.state = 'termine'
            elif record.date_debut <= today:
                record.state = 'en_cours'
            else:
                record.state = 'brouillon'
    
    @api.constrains('date_debut', 'date_fin')
    def _check_dates(self):
        for record in self:
            if record.date_fin and record.date_debut and record.date_fin < record.date_debut:
                raise ValidationError(_("La date de fin doit être postérieure à la date de début."))
    
    @api.onchange('apprenant_id')
    def _onchange_apprenant_id(self):
        """Charger automatiquement le cursus actif de l'apprenant"""
        if self.apprenant_id:
            cursus = self.env['limayrac.cursus'].search([
                ('apprenant_id', '=', self.apprenant_id.id),
                ('state', '=', 'en_cours')
            ], limit=1)
            if cursus:
                self.cursus_id = cursus.id
    
    def action_rompre(self):
        """Rompre le contrat"""
        self.write({'state': 'rompu'})
