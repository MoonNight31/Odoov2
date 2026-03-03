# Module limayrac_demo

## Description

Ce module contient toutes les données de démonstration pour les modules Limayrac.

Il permet de charger facilement toutes les données d'exemple dans votre base Odoo.

## Installation

### Prérequis

Tous les modules Limayrac doivent être **installés** avant d'installer ce module :
- limayrac_contacts
- limayrac_formation
- limayrac_candidature
- limayrac_contrat

### Procédure sur serveur distant

1. **Uploader le module** sur votre serveur dans le dossier des addons Odoo

2. **Mettre à jour la liste des applications** :
   - Connectez-vous à Odoo en tant qu'administrateur
   - Allez dans **Applications**
   - Activez le **Mode Développeur** (icône insecte)
   - Cliquez sur **Mettre à jour la liste des applications**

3. **Rechercher et installer** le module `limayrac_demo`:
   - Recherchez "Limayrac - Données de démonstration"
   - Cliquez sur **Installer**

4. Les données seront automatiquement chargées ✅

## Contenu des données

### Contacts (limayrac_contacts)
- 6 structures d'entreprises
- 7 services
- 6 candidats
- 2 apprenants actuels
- 2 alumni diplômés
- 4 intervenants/formateurs
- 5 tuteurs entreprise
- 6 types d'activité

### Formations (limayrac_formation)
- 5 formations (BTS SIO, BTS NDRC, Bachelor, BTS MCO, BTS SAM)
- 4 titres RNCP avec codes officiels
- 3 responsables de formation
- 5 besoins d'entreprises
- 5 opportunités (matching formations/besoins)

### Candidatures (limayrac_candidature)
- 6 vœux à différents stades du workflow
- 7 cursus (dont 2 diplômés pour les alumni)

### Contrats (limayrac_contrat)
- 6 contrats variés :
  - 3 contrats d'apprentissage
  - 2 contrats de professionnalisation
  - 1 convention de stage
- Notations et commentaires
- Périodes différentes

## Désinstallation

Pour supprimer les données de démonstration :

1. Désinstallez le module `limayrac_demo`
2. Les données créées resteront dans la base
3. Pour les supprimer complètement, vous devrez les supprimer manuellement via l'interface Odoo

## Notes techniques

- Toutes les références entre modules ont été consolidées dans ce module unique
- Les IDs externes sont préfixés par `limayrac_demo`
- Le fichier de données est chargé dans la section `data` (pas `demo`) pour garantir le chargement
- Les données ne sont pas marquées `noupdate` - elles seront rechargées à chaque mise à jour du module

## Dépannage

### "External ID not found"

Si vous obtenez cette erreur, vérifiez que :
- Tous les modules Limayrac sont installés
- Vous avez installé `limayrac_demo` **APRÈS** les autres modules

### Les données ne se chargent pas

1. Vérifiez les logs Odoo pour voir les erreurs détaillées
2. Assurez-vous que les modules de base sont à jour (version 1.0.1+)
3. Essayez de désinstaller puis réinstaller `limayrac_demo`

## Version

1.0.1 - Compatible avec Odoo 17
