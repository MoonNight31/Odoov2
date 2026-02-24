# -*- coding: utf-8 -*-
{
    'name': 'Limayrac - Formations',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestion des formations pour Limayrac',
    'description': """
        Module de gestion des formations pour l'établissement Limayrac.
        
        Fonctionnalités:
        - Gestion des formations
        - Gestion des titres RNCP
        - Gestion des besoins en formation des entreprises
    """,
    'author': 'Limayrac',
    'depends': ['base', 'limayrac_contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/limayrac_formation_views.xml',
        'views/limayrac_titre_rncp_views.xml',
        'views/limayrac_besoin_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
