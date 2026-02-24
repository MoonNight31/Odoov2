# Structure du projet CRM Limayrac

```
Odoov2/
│
├── README.md                           # Documentation principale
├── INSTALLATION.md                     # Guide d'installation
├── MCD_final.png                       # Modèle conceptuel de données
│
├── limayrac_contacts/                  # Module 1 : Contacts (base)
│   ├── __init__.py
│   ├── __manifest__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── res_partner.py              # Extension de res.partner
│   │   ├── limayrac_service.py         # Modèle Service
│   │   └── limayrac_groupe_structure.py # Modèle Groupe
│   ├── views/
│   │   ├── res_partner_views.xml       # Vues personnes/structures
│   │   ├── limayrac_service_views.xml
│   │   ├── limayrac_groupe_structure_views.xml
│   │   └── menus.xml
│   └── security/
│       └── ir.model.access.csv
│
├── limayrac_formation/                 # Module 2 : Formations
│   ├── __init__.py
│   ├── __manifest__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── limayrac_formation.py       # Modèle Formation
│   │   ├── limayrac_titre_rncp.py      # Modèle Titre RNCP
│   │   └── limayrac_besoin.py          # Modèle Besoin
│   ├── views/
│   │   ├── limayrac_formation_views.xml
│   │   ├── limayrac_titre_rncp_views.xml
│   │   ├── limayrac_besoin_views.xml
│   │   └── menus.xml
│   └── security/
│       └── ir.model.access.csv
│
├── limayrac_candidature/               # Module 3 : Candidatures
│   ├── __init__.py
│   ├── __manifest__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── limayrac_voeux.py           # Modèle Vœux
│   │   └── limayrac_cursus.py          # Modèle Cursus
│   ├── views/
│   │   ├── limayrac_voeux_views.xml
│   │   ├── limayrac_cursus_views.xml
│   │   └── menus.xml
│   └── security/
│       └── ir.model.access.csv
│
└── limayrac_contrat/                   # Module 4 : Contrats
    ├── __init__.py
    ├── __manifest__.py
    ├── models/
    │   ├── __init__.py
    │   └── limayrac_contrat.py         # Modèle Contrat
    ├── views/
    │   ├── limayrac_contrat_views.xml
    │   └── menus.xml
    └── security/
        └── ir.model.access.csv
```

## Description des fichiers

### Fichiers Python (`.py`)

- `__init__.py` : Fichier d'initialisation Python pour les packages
- `__manifest__.py` : Manifeste du module Odoo (métadonnées, dépendances)
- `models/*.py` : Définitions des modèles de données (tables)

### Fichiers XML (`.xml`)

- `views/*_views.xml` : Définitions des vues (formulaires, listes, recherches)
- `views/menus.xml` : Structure des menus
- `security/ir.model.access.csv` : Droits d'accès aux modèles

## Flux de données

```
┌─────────────────────────────────────────────────────────┐
│                    PERSONNE (res.partner)               │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Candidat → Apprenant → Alumni                    │  │
│  │ Intervenant, Tuteur                              │  │
│  └──────────────────────────────────────────────────┘  │
└───────────┬─────────────────────────────────┬───────────┘
            │                                 │
            ▼                                 ▼
    ┌───────────┐                     ┌──────────────┐
    │   VOEUX   │                     │   SERVICE    │
    └─────┬─────┘                     └──────┬───────┘
          │                                  │
          ▼                                  │
    ┌───────────┐                            │
    │  CURSUS   │                            │
    └─────┬─────┘                            │
          │                                  │
          └──────────┬───────────────────────┘
                     ▼
              ┌──────────────┐
              │   CONTRAT    │
              └──────────────┘
                     │
                     ▼
            ┌─────────────────┐
            │   FORMATION     │
            │   TITRE_RNCP    │
            └─────────────────┘

┌─────────────────────────────────────────────────────────┐
│              STRUCTURE (res.partner)                    │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Entreprises, Organisations                       │  │
│  └──────────────────────────────────────────────────┘  │
└───────────┬─────────────────────────────────────────────┘
            │
            ▼
    ┌──────────────────┐
    │ GROUPE_STRUCTURE │
    │     (SIREN)      │
    └──────────────────┘
```

## Correspondance MCD → Odoo

| Entité MCD         | Modèle Odoo                    | Module              |
|--------------------|--------------------------------|---------------------|
| PERSONNE           | res.partner (étendu)           | limayrac_contacts   |
| STRUCTURE          | res.partner (étendu)           | limayrac_contacts   |
| SERVICE            | limayrac.service               | limayrac_contacts   |
| GROUPE_STRUCTURE   | limayrac.groupe.structure      | limayrac_contacts   |
| FORMATION          | limayrac.formation             | limayrac_formation  |
| TITRE_RNCP         | limayrac.titre.rncp            | limayrac_formation  |
| BESOIN             | limayrac.besoin                | limayrac_formation  |
| VOEUX              | limayrac.voeux                 | limayrac_candidature|
| CURSUS             | limayrac.cursus                | limayrac_candidature|
| CONTRAT            | limayrac.contrat               | limayrac_contrat    |

**Note** : La relation PERSONNE → FORMATION (responsables) est gérée par le champ `formation_responsable_id` dans res.partner.

## Types de relations

- **One2many** : Un vers plusieurs (ex: une structure a plusieurs services)
- **Many2one** : Plusieurs vers un (ex: plusieurs contrats vers un service)
- **Many2many** : Plusieurs vers plusieurs (non utilisé dans ce projet)

## Champs importants

### Champs de relation
- `*_id` : Relation Many2one (ex: `formation_id`, `formation_responsable_id`)
- `*_ids` : Relation One2many ou Many2many (ex: `contrat_ids`, `responsable_ids`)

### Champs calculés
- `*_count` : Compteurs calculés dynamiquement
- `state` : État calculé automatiquement
- `is_active` : Statut actif calculé

### Champs système
- `create_date` : Date de création (automatique)
- `write_date` : Date de modification (automatique)
- `date_created` : Date de création custom (manuel)
- `date_updated` : Date de mise à jour custom (manuel)
