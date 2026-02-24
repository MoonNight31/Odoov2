# Fonctionnalités du CRM Limayrac

## Vue d'ensemble des modules

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          CRM LIMAYRAC - ODOO                            │
│                    Système de Gestion Intégré                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ MODULE 1: LIMAYRAC_CONTACTS                                             │
│ ════════════════════════════════════════════════════════════════════    │
│                                                                          │
│ PERSONNES                           STRUCTURES                          │
│ ┌──────────────────┐               ┌──────────────────┐                │
│ │ • Candidats      │               │ • Entreprises    │                │
│ │ • Apprenants     │               │ • SIRET/SIREN    │                │
│ │ • Alumni         │               │ • Partenaires    │                │
│ │ • Intervenants   │               │ • Prospects      │                │
│ │ • Tuteurs        │               │ • Services       │                ││  │ • Responsables   │               │                  │                ││ └──────────────────┘               └──────────────────┘                │
│                                                                          │
│ GROUPES DE STRUCTURES                                                   │
│ ┌────────────────────────────────────────────────────┐                 │
│ │ • Holdings / Groupes (SIREN)                       │                 │
│ │ • Gestion multi-établissements                     │                 │
│ └────────────────────────────────────────────────────┘                 │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ MODULE 2: LIMAYRAC_FORMATION                                            │
│ ════════════════════════════════════════════════════════════════════    │
│                                                                          │
│ CATALOGUE                    TITRES RNCP              BESOINS           │
│ ┌────────────┐              ┌────────────┐          ┌────────────┐     │
│ │ • BTS      │              │ • Codes    │          │ • Demandes │     │
│ │ • Bachelor │              │ • Validité │          │ • Entreprise│    │
│ │ • Licence  │              │ • Niveaux  │          │ • Suivi    │     │
│ └────────────┘              └────────────┘          └────────────┘     │
│                                                                          │
│ STATISTIQUES PAR FORMATION                                              │
│ ┌────────────────────────────────────────────────────┐                 │
│ │ • Nombre de vœux                                   │                 │
│ │ • Cursus actifs                                    │                 │
│ │ • Besoins entreprises                              │                 │
│ └────────────────────────────────────────────────────┘                 │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ MODULE 3: LIMAYRAC_CANDIDATURE                                          │
│ ════════════════════════════════════════════════════════════════════    │
│                                                                          │
│ VŒUX (Candidatures)                    CURSUS                           │
│ ┌──────────────────────┐             ┌──────────────────────┐          │
│ │ Workflow:            │             │ États:               │          │
│ │ 1. Nouveau           │             │ • En cours           │          │
│ │ 2. En cours d'examen │────────────▶│ • Terminé            │          │
│ │ 3. Accepté ─────────┐│             │ • Abandonné          │          │
│ │ 4. Refusé           ││             │                      │          │
│ │ 5. Annulé           ││             │ Actions:             │          │
│ └──────────────────────┘│             │ • Diplômer           │          │
│                         │             │   → Statut Alumni    │          │
│                         │             └──────────────────────┘          │
│                         │                                               │
│                         └──────────▶ Création automatique               │
│                                      de cursus après acceptation        │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ MODULE 4: LIMAYRAC_CONTRAT                                              │
│ ════════════════════════════════════════════════════════════════════    │
│                                                                          │
│ TYPES DE CONTRATS                                                       │
│ ┌─────────────────────────────────────────────────────┐                │
│ │ • Contrat d'apprentissage                           │                │
│ │ • Contrat de professionnalisation                   │                │
│ │ • Convention de stage                               │                │
│ └─────────────────────────────────────────────────────┘                │
│                                                                          │
│ ACTEURS                                                                 │
│ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                  │
│ │  Apprenant   │  │  Entreprise  │  │   Tuteurs    │                  │
│ │              │  │              │  │              │                  │
│ │ • Cursus     │  │ • Structure  │  │ • Tuteur 1   │                  │
│ │ • Formation  │  │ • Service    │  │ • Tuteur 2   │                  │
│ │              │  │              │  │ • École      │                  │
│ └──────────────┘  └──────────────┘  └──────────────┘                  │
│                                                                          │
│ SUIVI                                                                   │
│ ┌─────────────────────────────────────────────────────┐                │
│ │ • États automatiques (brouillon/en cours/terminé)   │                │
│ │ • Notation (1-5 étoiles)                            │                │
│ │ • Commentaires et suivi                             │                │
│ │ • Chatter (historique + activités)                  │                │
│ │ • Possibilité de rupture                            │                │
│ └─────────────────────────────────────────────────────┘                │
└─────────────────────────────────────────────────────────────────────────┘
```

## Parcours type d'un apprenant

```
   CANDIDATURE              FORMATION                DIPLÔME
       │                        │                        │
       ▼                        ▼                        ▼
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   CANDIDAT  │         │  APPRENANT  │         │   ALUMNI    │
│             │         │             │         │             │
│  Statut:    │         │  Statut:    │         │  Statut:    │
│  Candidat   │         │  Apprenant  │         │  Alumni     │
│             │         │             │         │             │
│  Action:    │         │  Documents: │         │  Réseau:    │
│  • Vœux     │────────▶│  • Cursus   │────────▶│  • Contact  │
│             │ Accept. │  • Contrat  │ Diplôme │  • Événem.  │
└─────────────┘         └─────────────┘         └─────────────┘
```

## Flux de données principal

```
ENTREPRISE exprime un BESOIN
         │
         ▼
Recherche de CANDIDATS
         │
         ▼
CANDIDAT fait un VŒUX
         │
         ▼ (Acceptation)
Création d'un CURSUS
         │
         ▼
ENTREPRISE propose un CONTRAT
         │
         ▼
APPRENANT signe le CONTRAT
         │
         ▼ (Fin de formation)
DIPLÔMATION → ALUMNI
```

## Fonctionnalités clés par module

### limayrac_contacts

| Fonctionnalité | Description |
|----------------|-------------|
| **Multi-rôles** | Une personne peut avoir plusieurs rôles simultanés |
| **Responsables** | Gestion des responsables de formation (plusieurs par formation) |
| **SIREN/SIRET** | Extraction et liaison automatique groupe/structure |
| **Filtres avancés** | Filtrage par rôle, statut, partenariat |
| **Services** | Gestion des départements dans les structures |
| **Groupe** | Gestion des holdings avec plusieurs établissements |

### limayrac_formation

| Fonctionnalité | Description |
|----------------|-------------|
| **Catalogue** | Gestion complète du catalogue de formations |
| **Responsables** | Affectation des responsables de formation |
| **Besoins** | Workflow de gestion des besoins entreprises |
| **Statistiques** | Indicateurs (vœux, cursus, besoins, responsablerises |
| **Statistiques** | Indicateurs (vœux, cursus, besoins) par formation |
| **Matching** | Aide au rapprochement offre/demande |

### limayrac_candidature

| Fonctionnalité | Description |
|----------------|-------------|
| **Workflow vœux** | Process complet de candidature |
| **Auto-création** | Cursus créé automatiquement après acceptation |
| **États** | Suivi de l'état des cursus (en cours, terminé, etc.) |
| **Diplômation** | Passage automatique en alumni |
| **Historique** | Traçabilité complète du parcours |

### limayrac_contrat

| Fonctionnalité | Description |
|----------------|-------------|
| **Multi-tuteurs** | 2 tuteurs entreprise + 1 tuteur école |
| **États auto** | Calcul automatique de l'état selon les dates |
| **Notation** | Système de notation 1-5 étoiles |
| **Chatter** | Suivi collaboratif avec historique |
| **Rupture** | Gestion des ruptures de contrat |
| **Vue Kanban** | Visualisation carte pour suivi rapide |

## Tableaux de bord disponibles

### Vue candidatures

- Vœux par formation
- Vœux par période
- Taux d'acceptation
- Délai de traitement

### Vue formations

- Cursus actifs par formation
- Taux de diplômation
- Besoins vs candidats
- Évolution historique

### Vue contrats

- Contrats en cours par formation
- Contrats par entreprise
- Notations moyennes
- Taux de rupture

### Vue entreprises

- Top entreprises partenaires (nb contrats)
- Besoins non satisfaits
- Services actifs
- Géographie des partenariats

## Intégrations et extensions possibles

### Extensions suggérées

- **Mail** : Envoi automatique d'emails aux candidats
- **Calendrier** : Gestion des soutenances, entretiens
- **Documents** : GED pour les documents administratifs
- **Reporting** : Tableaux de bord avancés
- **Website** : Portail candidat en ligne
- **Sign** : Signature électronique des contrats

### API et exports

- Export Excel/CSV de toutes les données
- Import massif de contacts/candidats
- API REST pour intégration externe
- Synchronisation avec autres systèmes

## Sécurité et droits d'accès

### Groupes possibles (à créer selon besoins)

- **Administrateur CRM** : Tous droits
- **Gestionnaire formations** : Formations, vœux, cursus
- **Gestionnaire entreprises** : Structures, services, besoins
- **Gestionnaire contrats** : Contrats, suivi
- **Consultation** : Lecture seule

### Données sensibles

- Données personnelles candidats : RGPD
- Informations entreprises : Confidentialité
- Notations : Accès restreint
- Historique : Traçabilité complète

## Performance et volumétrie

### Capacités estimées

- **Contacts** : 10 000+ personnes/structures
- **Formations** : 50+ formations actives
- **Cursus** : 500+ cursus actifs
- **Contrats** : 500+ contrats actifs
- **Historique** : Conservation illimitée

### Optimisations

- Index sur champs fréquemment recherchés
- Archivage des anciens cursus/contrats
- Vues matérialisées pour statistiques
- Cache sur compteurs

## Support et maintenance

### Mises à jour recommandées

- **Mensuel** : Vérification des données
- **Trimestriel** : Nettoyage et archivage
- **Annuel** : Révision des formations/titres RNCP

### Sauvegardes

- Base de données : Quotidienne
- Documents : Quotidienne
- Configuration : Après chaque modification

---

**Documentation complète** : Voir [README.md](README.md), [INSTALLATION.md](INSTALLATION.md), [WORKFLOW.md](WORKFLOW.md), [STRUCTURE.md](STRUCTURE.md)
