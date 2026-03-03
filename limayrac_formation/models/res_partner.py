# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    # Responsable de formation
    formation_responsable_id = fields.Many2one('limayrac.formation', string='Formation (Responsable)')
