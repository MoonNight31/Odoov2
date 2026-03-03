# -*- coding: utf-8 -*-
{
    'name': 'Limayrac - Données de démonstration',
    'version': '1.0.3',
    'category': 'Education',
    'summary': 'Données de démonstration enrichies pour tous les modules Limayrac',
    'description': """
        Module contenant toutes les données de démonstration pour les modules Limayrac.
        
        Ce module doit être installé APRÈS tous les autres modules Limayrac.
        Il créera automatiquement :
        - Des structures et contacts d'exemple (20+ structures)
        - Des formations diverses (BTS, Licence, Master)
        - Des candidatures et cursus (30+ dossiers)
        - Des contrats d'alternance et professionnalisation (15+ contrats)
        - Des opportunités de stage et alternance
        - Des besoins en formation continue
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
        'data/demo_data_enriched.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
