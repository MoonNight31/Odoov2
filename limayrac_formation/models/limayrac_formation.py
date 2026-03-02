# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracFormation(models.Model):
    _name = 'limayrac.formation'
    _description = 'Formation Limayrac'
    _rec_name = 'nom_commercial'

    nom_commercial = fields.Char(string='Nom Commercial', required=True)
    description = fields.Text(string='Description')
    
    # Questions pour le jury
    question_1 = fields.Text(string='Question 1')
    question_2 = fields.Text(string='Question 2')
    question_3 = fields.Text(string='Question 3')
    question_4 = fields.Text(string='Question 4')
    question_5 = fields.Text(string='Question 5')
    
    # Relations
    titre_rncp_ids = fields.One2many('limayrac.titre.rncp', 'formation_id', string='Titres RNCP')
    opportunite_ids = fields.One2many('limayrac.opportunite', 'formation_id', string='Opportunités')
    responsable_ids = fields.One2many('res.partner', 'formation_responsable_id', string='Responsables')
    
    # Compteurs
    responsable_count = fields.Integer(string='Nombre de responsables', compute='_compute_counts')
    opportunite_count = fields.Integer(string='Nombre d\'opportunités', compute='_compute_counts')
    
    @api.depends('responsable_ids', 'opportunite_ids')
    def _compute_counts(self):
        for record in self:
            record.responsable_count = len(record.responsable_ids)
            record.opportunite_count = len(record.opportunite_ids)
