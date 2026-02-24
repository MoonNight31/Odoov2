# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracVoeux(models.Model):
    _name = 'limayrac.voeux'
    _description = 'Vœux de candidature'
    _rec_name = 'apprenant_id'
    _order = 'date_candidature desc'

    apprenant_id = fields.Many2one('res.partner', string='Candidat', 
                                   domain=[('is_candidat', '=', True)],
                                   required=True)
    formation_id = fields.Many2one('limayrac.formation', string='Formation', required=True)
    date_candidature = fields.Date(string='Date de candidature', default=fields.Date.today, required=True)
    
    state = fields.Selection([
        ('nouveau', 'Nouveau'),
        ('en_cours', 'En cours d\'examen'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
        ('annule', 'Annulé')
    ], string='État', default='nouveau', required=True)
    
    notes = fields.Text(string='Notes')
    
    # Informations du candidat (dupliquées pour facilité)
    email = fields.Char(related='apprenant_id.email', string='Email', readonly=True)
    phone = fields.Char(related='apprenant_id.phone', string='Téléphone', readonly=True)
    
    @api.model
    def create(self, vals):
        # Marquer automatiquement la personne comme candidat
        if vals.get('apprenant_id'):
            apprenant = self.env['res.partner'].browse(vals['apprenant_id'])
            apprenant.write({'is_candidat': True})
        return super(LimayracVoeux, self).create(vals)
    
    def action_accepter(self):
        """Accepter le vœu et proposer de créer un cursus"""
        self.write({'state': 'accepte'})
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
        self.write({'state': 'refuse'})
    
    def action_annuler(self):
        """Annuler le vœu"""
        self.write({'state': 'annule'})
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.apprenant_id.name} - {record.formation_id.nom_commercial}"
            result.append((record.id, name))
        return result
