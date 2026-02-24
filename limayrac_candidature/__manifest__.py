# -*- coding: utf-8 -*-
{
    'name': 'Limayrac - Candidatures',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestion des candidatures et cursus pour Limayrac',
    'description': """
        Module de gestion des candidatures pour l'établissement Limayrac.
        
        Fonctionnalités:
        - Gestion des vœux (candidatures)
        - Gestion des cursus (apprenants inscrits)
        - Suivi du parcours des apprenants
    """,
    'author': 'Limayrac',
    'depends': ['base', 'limayrac_contacts', 'limayrac_formation'],
    'data': [
        'security/ir.model.access.csv',
        'views/limayrac_voeux_views.xml',
        'views/limayrac_cursus_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
