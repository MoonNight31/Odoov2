# Index des fichiers - CRM Limayrac

## Documentation

| Fichier | Description |
|---------|-------------|
| [README.md](README.md) | Documentation principale du projet |
| [INSTALLATION.md](INSTALLATION.md) | Guide d'installation pas à pas |
| [STRUCTURE.md](STRUCTURE.md) | Structure technique du projet |
| [WORKFLOW.md](WORKFLOW.md) | Guide des processus métier |
| [FEATURES.md](FEATURES.md) | Liste des fonctionnalités |
| INDEX.md | Ce fichier - Index de tous les fichiers |
| MCD_final.png | Modèle Conceptuel de Données |
| demo_data.py | Script de création de données de test |

## Module: limayrac_contacts

### Fichiers principaux
- `__init__.py` - Initialisation du module
- `__manifest__.py` - Manifeste et configuration

### Modèles (models/)
- `__init__.py` - Import des modèles
- `res_partner.py` - Extension du contact Odoo (personnes et structures)
- `limayrac_service.py` - Modèle Service
- `limayrac_groupe_structure.py` - Modèle Groupe de structures

### Vues (views/)
- `res_partner_views.xml` - Vues personnes et structures
- `limayrac_service_views.xml` - Vues services
- `limayrac_groupe_structure_views.xml` - Vues groupes
- `menus.xml` - Structure des menus

### Sécurité (security/)
- `ir.model.access.csv` - Droits d'accès

## Module: limayrac_formation

### Fichiers principaux
- `__init__.py` - Initialisation du module
- `__manifest__.py` - Manifeste et configuration

### Modèles (models/)
- `__init__.py` - Import des modèles
- `limayrac_formation.py` - Modèle Formation
- `limayrac_titre_rncp.py` - Modèle Titre RNCP
- `limayrac_besoin.py` - Modèle Besoin

### Vues (views/)
- `limayrac_formation_views.xml` - Vues formations
- `limayrac_titre_rncp_views.xml` - Vues titres RNCP
- `limayrac_besoin_views.xml` - Vues besoins
- `menus.xml` - Structure des menus

### Sécurité (security/)
- `ir.model.access.csv` - Droits d'accès

## Module: limayrac_candidature

### Fichiers principaux
- `__init__.py` - Initialisation du module
- `__manifest__.py` - Manifeste et configuration

### Modèles (models/)
- `__init__.py` - Import des modèles
- `limayrac_voeux.py` - Modèle Vœux/Candidature
- `limayrac_cursus.py` - Modèle Cursus

### Vues (views/)
- `limayrac_voeux_views.xml` - Vues vœux
- `limayrac_cursus_views.xml` - Vues cursus
- `menus.xml` - Structure des menus

### Sécurité (security/)
- `ir.model.access.csv` - Droits d'accès

## Module: limayrac_contrat

### Fichiers principaux
- `__init__.py` - Initialisation du module
- `__manifest__.py` - Manifeste et configuration

### Modèles (models/)
- `__init__.py` - Import des modèles
- `limayrac_contrat.py` - Modèle Contrat

### Vues (views/)
- `limayrac_contrat_views.xml` - Vues contrats (liste, formulaire, kanban)
- `menus.xml` - Structure des menus

### Sécurité (security/)
- `ir.model.access.csv` - Droits d'accès

## Statistiques du projet

### Nombre de fichiers par type

| Type | Nombre |
|------|--------|
| Fichiers Python (.py) | 14 |
| Fichiers XML (.xml) | 14 |
| Fichiers CSV (.csv) | 4 |
| Documentation (.md) | 6 |
| Images (.png) | 1 |
| **TOTAL** | **39** |

### Lignes de code estimées

| Composant | Lignes |
|-----------|--------|
| Python | ~1500 |
| XML | ~1200 |
| Documentation | ~2500 |
| **TOTAL** | **~5200** |

## Dépendances entre modules

```
limayrac_contacts (base)
    ├── depends: base, contacts
    │
    └─── limayrac_formation
            ├── depends: limayrac_contacts
            │
            └─── limayrac_candidature
                    ├── depends: limayrac_formation
                    │
                    └─── limayrac_contrat
                            └── depends: limayrac_candidature, mail
```

## Modèles de données

### limayrac_contacts
1. `res.partner` (étendu) - Personnes et structures
2. `limayrac.service` - Services
3. `limayrac.groupe.structure` - Groupes

### limayrac_formation
4. `limayrac.formation` - Formations
5. `limayrac.titre.rncp` - Titres RNCP
6. `limayrac.besoin` - Besoins

### limayrac_candidature
7. `limayrac.voeux` - Vœux
8. `limayrac.cursus` - Cursus

### limayrac_contrat
9. `limayrac.contrat` - Contrats

**Total : 9 modèles** (10 avec l'extension de res.partner)

## Vues disponibles

| Type de vue | Nombre |
|-------------|--------|
| Formulaire | 9 |
| Liste/Arbre | 9 |
| Recherche | 8 |
| Kanban | 1 |
| **TOTAL** | **27** |

## Menus

### Structure des menus

```
Limayrac (menu principal)
│
├── Contacts
│   ├── Personnes
│   ├── Structures
│   ├── Services
│   └── Groupes
│
├── Formations
│   ├── Formations
│   ├── Titres RNCP
│   └── Besoins
│
├── Candidatures
│   ├── Vœux
│   └── Cursus
│
└── Contrats
    └── Contrats
```

**Total : 11 entrées de menu**

## Champs personnalisés ajoutés

### Sur res.partner (Personnes)
- `poste` - Poste occupé
- `is_alumni` - Statut Alumni
- `is_candidat` - Statut Candidat
- `is_apprenant` - Statut Apprenant
- `is_intervenant` - Statut Intervenant
- `is_tuteur` - Statut Tuteur
- `service_id` - Service rattaché
- `formation_responsable_id` - Formation dont la personne est responsable

### Sur res.partner (Structures)
- `siret` - SIRET
- `raison_sociale` - Raison sociale
- `code_naf` - Code NAF
- `site_web` - Site web
- `is_blacklist` - Liste noire
- `is_partenaire` - Partenaire
- `is_taxe_apprentissage` - Taxe d'apprentissage
- `is_prospect` - Prospect
- `groupe_structure_id` - Groupe
- `service_ids` - Services

## Fonctionnalités avancées

### Automatisations
- ✅ Création automatique du groupe (SIREN) depuis SIRET
- ✅ Marquage automatique comme "apprenant" à la création du cursus
- ✅ Marquage automatique comme "candidat" à la création du vœu
- ✅ Passage automatique en "alumni" à la diplômation
- ✅ Calcul automatique de l'état des contrats selon les dates
- ✅ Calcul automatique de l'état des cursus
- ✅ Calcul automatique de la validité des titres RNCP

### Compteurs dynamiques
- Nombre de vœux par formation
- Nombre de cursus actifs par formation
- Nombre de besoins par formation
- Nombre de contrats par cursus
- Nombre de structures par groupe

### Contraintes de validation
- ✅ Dates de fin > dates de début (cursus et contrats)
- ✅ SIREN unique dans les groupes
- ✅ Champs requis validés

### Traçabilité (Chatter)
- Historique complet des modifications sur les contrats
- Tracking des champs importants
- Possibilité d'ajouter des notes
- Programmation d'activités

## Installation et déploiement

### Prérequis
- Odoo 14.0+
- Python 3.7+
- PostgreSQL 10+

### Installation
1. Copier les modules dans addons/
2. Redémarrer Odoo
3. Mettre à jour la liste des applications
4. Installer les modules

### Configuration
1. Créer les formations
2. Créer les structures partenaires
3. Importer les contacts
4. Optionnel : Exécuter demo_data.py pour données de test

## Support et ressources

### Documentation technique
- [Odoo Developer Documentation](https://www.odoo.com/documentation/)
- [Odoo Community Forum](https://www.odoo.com/forum/)

### Fichiers de référence
- `README.md` - Commencer ici
- `INSTALLATION.md` - Installation
- `WORKFLOW.md` - Utilisation quotidienne
- `FEATURES.md` - Vue d'ensemble des fonctionnalités
- `STRUCTURE.md` - Architecture technique

## Changelog

### Version 1.0 (Février 2026)
- ✅ Création des 4 modules principaux
- ✅ Extension de res.partner
- ✅ Gestion complète du cycle candidat → apprenant → alumni
- ✅ Gestion des contrats avec multi-tuteurs
- ✅ Système de besoins entreprises
- ✅ Documentation complète
- ✅ Script de données de démonstration

## Roadmap (fonctionnalités futures)

### Version 1.1
- [ ] Portail candidat web
- [ ] Envoi automatique d'emails
- [ ] Rapports PDF personnalisés

### Version 1.2
- [ ] Gestion des soutenances
- [ ] Planning des cours
- [ ] Signature électronique

### Version 2.0
- [ ] Tableaux de bord avancés
- [ ] Application mobile
- [ ] API REST publique

## Contacts et support

Pour toute question :
- Consulter la documentation
- Vérifier les logs Odoo
- Contacter l'équipe technique Limayrac

---

**Projet** : CRM Limayrac  
**Version** : 1.0  
**Date** : Février 2026  
**Auteur** : Limayrac  
**Licence** : Propriétaire
