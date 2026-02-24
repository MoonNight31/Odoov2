# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LimayracGroupeStructure(models.Model):
    _name = 'limayrac.groupe.structure'
    _description = 'Groupe de structures (holding, groupe d\'entreprises)'
    _rec_name = 'name'

    name = fields.Char(string='Nom du Groupe', required=True)
    siren = fields.Char(string='SIREN', size=9, required=True, unique=True)
    siege_social = fields.Char(string='Siège Social')
    
    date_created = fields.Datetime(string='Date de création', default=fields.Datetime.now, readonly=True)
    date_updated = fields.Datetime(string='Date de mise à jour', readonly=True)
    
    # Structures (établissements) liés à ce groupe
    structure_ids = fields.One2many('res.partner', 'groupe_structure_id', string='Structures/Établissements')
    
    structure_count = fields.Integer(string='Nombre de structures', compute='_compute_structure_count')
    
    @api.depends('structure_ids')
    def _compute_structure_count(self):
        for record in self:
            record.structure_count = len(record.structure_ids)
    
    @api.model
    def create(self, vals):
        vals['date_created'] = fields.Datetime.now()
        return super(LimayracGroupeStructure, self).create(vals)
    
    def write(self, vals):
        vals['date_updated'] = fields.Datetime.now()
        return super(LimayracGroupeStructure, self).write(vals)
    
    _sql_constraints = [
        ('siren_unique', 'unique(siren)', 'Le SIREN doit être unique!')
    ]
