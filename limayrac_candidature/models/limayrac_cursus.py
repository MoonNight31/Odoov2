# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LimayracCursus(models.Model):
    _name = 'limayrac.cursus'
    _description = 'Cursus d\'un apprenant'
    _rec_name = 'apprenant_id'
    _order = 'date_debut desc'

    apprenant_id = fields.Many2one('res.partner', string='Apprenant', 
                                   domain="['|', ('is_apprenant', '=', True), ('is_candidat', '=', True)]",
                                   required=True)
    formation_id = fields.Many2one('limayrac.formation', string='Formation', required=True)
    
    date_debut = fields.Date(string='Date de début', required=True)
    date_fin = fields.Date(string='Date de fin')
    
    is_diplome = fields.Boolean(string='Diplômé', default=False)
    
    # Informations de l'apprenant (dupliquées pour facilité)
    email = fields.Char(related='apprenant_id.email', string='Email', readonly=True)
    phone = fields.Char(related='apprenant_id.phone', string='Téléphone', readonly=True)
    
    # État du cursus
    state = fields.Selection([
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('abandonne', 'Abandonné')
    ], string='État', compute='_compute_state', store=True)
    
    @api.depends('date_debut', 'date_fin', 'is_diplome')
    def _compute_state(self):
        today = fields.Date.today()
        for record in self:
            if record.is_diplome:
                record.state = 'termine'
            elif record.date_fin and record.date_fin < today:
                record.state = 'termine'
            elif record.date_debut and record.date_debut <= today:
                record.state = 'en_cours'
            else:
                record.state = 'en_cours'
    
    @api.constrains('date_debut', 'date_fin')
    def _check_dates(self):
        for record in self:
            if record.date_fin and record.date_debut and record.date_fin < record.date_debut:
                raise ValidationError(_("La date de fin doit être postérieure à la date de début."))
    
    @api.model
    def create(self, vals):
        # Marquer automatiquement la personne comme apprenant
        if vals.get('apprenant_id'):
            apprenant = self.env['res.partner'].browse(vals['apprenant_id'])
            apprenant.write({'is_apprenant': True})
        return super(LimayracCursus, self).create(vals)
    
    def action_diplomer(self):
        """Marquer l'apprenant comme diplômé"""
        self.write({'is_diplome': True})
        # Marquer l'apprenant comme alumni
        self.apprenant_id.write({'is_alumni': True})
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.apprenant_id.name} - {record.formation_id.nom_commercial} ({record.date_debut.year if record.date_debut else ''})"
            result.append((record.id, name))
        return result
