# -*- coding: utf-8 -*-
{
    'name': 'Limayrac - Contacts',
    'version': '1.0',
    'category': 'CRM',
    'summary': 'Gestion des personnes et structures pour Limayrac',
    'description': """
        Module de gestion des contacts pour l'établissement Limayrac.
        
        Fonctionnalités:
        - Gestion des personnes (candidats, apprenants, intervenants, tuteurs, alumni)
        - Gestion des structures (entreprises, organisations)
        - Gestion des groupes de structures
        - Gestion des services
    """,
    'author': 'Limayrac',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/limayrac_service_views.xml',
        'views/limayrac_groupe_structure_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
