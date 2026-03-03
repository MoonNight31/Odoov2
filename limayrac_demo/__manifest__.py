# -*- coding: utf-8 -*-
{
    'name': 'Limayrac - Données de démonstration',
    'version': '1.0.2',
    'category': 'Education',
    'summary': 'Données de démonstration pour tous les modules Limayrac',
    'description': """
        Module contenant toutes les données de démonstration pour les modules Limayrac.
        
        Ce module doit être installé APRÈS tous les autres modules Limayrac.
        Il créera automatiquement :
        - Des structures et contacts d'exemple
        - Des formations et cursus
        - Des candidatures et contrats
    """,
    'author': 'Limayrac',
    'depends': [
        'limayrac_contacts',
        'limayrac_formation',
        'limayrac_candidature',
        'limayrac_contrat',
    ],
    'data': [
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
