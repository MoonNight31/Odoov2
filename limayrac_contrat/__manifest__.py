# -*- coding: utf-8 -*-
{
    'name': 'Limayrac - Contrats',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestion des contrats pour Limayrac',
    'description': """
        Module de gestion des contrats pour l'établissement Limayrac.
        
        Fonctionnalités:
        - Gestion des contrats d'alternance/apprentissage
        - Suivi des tuteurs (entreprise et école)
        - Suivi des notations et commentaires
    """,
    'author': 'Limayrac',
    'depends': ['base', 'mail', 'limayrac_contacts', 'limayrac_formation', 'limayrac_candidature'],
    'data': [
        'security/ir.model.access.csv',
        'views/limayrac_contrat_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
