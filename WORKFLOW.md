# Guide Workflow - CRM Limayrac

Ce guide explique les processus métier typiques dans le CRM Limayrac.

## Table des matières

1. [Processus de candidature](#processus-de-candidature)
2. [Gestion des partenariats entreprises](#gestion-des-partenariats-entreprises)
3. [Suivi des contrats](#suivi-des-contrats)
4. [Diplômation et passage en alumni](#diplomation-et-passage-en-alumni)
5. [Gestion des besoins entreprises](#gestion-des-besoins-entreprises)

---

## Processus de candidature

### 1. Réception d'une candidature

**Menu** : Limayrac → Contacts → Personnes

1. Créer un nouveau contact
2. Renseigner les informations personnelles :
   - Nom, prénom
   - Email, téléphone
   - Adresse
3. Cocher **"Candidat"** dans l'onglet "Rôles Limayrac"

### 2. Création d'un vœu

**Menu** : Limayrac → Candidatures → Vœux

1. Cliquer sur "Créer"
2. Sélectionner le candidat
3. Choisir la formation souhaitée
4. La date de candidature est pré-remplie (aujourd'hui)
5. État : "Nouveau" par défaut

### 3. Traitement du vœu

1. Ouvrir le vœu
2. Ajouter des notes si nécessaire
3. Passer l'état en "En cours d'examen"
4. Après décision :
   - **Accepter** : Cliquer sur "Accepter"
     → Ouvre automatiquement un formulaire de cursus
   - **Refuser** : Cliquer sur "Refuser"
   - **Annuler** : Si le candidat se désiste

### 4. Création du cursus (après acceptation)

**Automatique après acceptation du vœu, ou manuel :**

**Menu** : Limayrac → Candidatures → Cursus

1. Le formulaire s'ouvre avec l'apprenant et la formation pré-remplis
2. Renseigner :
   - Date de début (ex: 01/09/2026)
   - Date de fin (optionnel, si connue)
3. Enregistrer

**Résultat** : Le candidat devient automatiquement "Apprenant"

---

## Gestion des partenariats entreprises

### 1. Création d'une structure entreprise

**Menu** : Limayrac → Contacts → Structures

1. Créer un nouveau contact
2. Type : "Entreprise"
3. Renseigner :
   - Nom
   - SIRET (14 chiffres)
     → Le système extrait automatiquement le SIREN et crée/lie le groupe
   - Raison sociale
   - Code NAF
   - Adresse
   - Site web
4. Onglet "Informations Limayrac" :
   - Cocher les statuts appropriés :
     - **Partenaire** : Entreprise partenaire régulière
     - **Prospect** : Entreprise prospectée
     - **Taxe d'apprentissage** : Verse la taxe d'apprentissage
     - **Liste noire** : À éviter

### 2. Création de services

Dans la fiche structure, onglet "Informations Limayrac" :

1. Section "Services"
2. Ajouter une ligne
3. Renseigner :
   - Type de service (ex: "Département Informatique")
   - Actif : Oui
4. Enregistrer

### 3. Ajout de contacts dans l'entreprise

**Menu** : Limayrac → Contacts → Personnes

1. Créer une personne
2. Dans "Société" : Sélectionner la structure
3. Renseigner le poste
4. Sélectionner le service (si applicable)
5. Cocher les rôles :
   - **Tuteur** : Peut être tuteur entreprise
   - **Intervenant** : Peut être tuteur école ou intervenir

---

## Suivi des contrats

### 1. Création d'un contrat

**Menu** : Limayrac → Contrats → Contrats

**Prérequis** : L'apprenant doit avoir un cursus actif

1. Créer un contrat
2. Renseigner :
   - **Type de contrat** :
     - Contrat d'apprentissage
     - Contrat de professionnalisation
     - Convention de stage
   - **Type d'activité** : Description du poste
   - **Dates** : Début et fin
   - **Apprenant** : Sélectionner l'apprenant
     → Le cursus actif se charge automatiquement
   - **Service** : Sélectionner le service dans l'entreprise
     → La structure se remplit automatiquement
   - **Tuteurs** :
     - Tuteur entreprise 1 (obligatoire)
     - Tuteur entreprise 2 (optionnel, si 2 tuteurs simultanés)
     - Tuteur école
   - **Notation** : 1 à 5 étoiles
   - **Commentaire** : Remarques, suivi

3. Enregistrer

**État automatique** :
- Avant la date de début : "Brouillon"
- À partir de la date de début : "En cours"
- Après la date de fin : "Terminé"

### 2. Suivi du contrat

1. Ouvrir le contrat
2. Utiliser le **Chatter** (en bas) pour :
   - Ajouter des notes
   - Programmer des activités (rappels, rendez-vous)
   - Suivre l'historique des modifications
3. Mettre à jour la notation selon l'évolution
4. Si rupture anticipée : Bouton "Rompre le contrat"

### 3. Visualisation

- **Vue Liste** : Vue d'ensemble de tous les contrats
- **Vue Kanban** : Vue carte pour suivi rapide
- **Filtres** :
  - Par état (brouillon, en cours, terminé, rompu)
  - Par type (apprentissage, professionnalisation, stage)
  - Année en cours

---

## Diplômation et passage en alumni

### Processus de diplômation

**Menu** : Limayrac → Candidatures → Cursus

1. Ouvrir le cursus de l'apprenant
2. Vérifier :
   - La formation est terminée
   - L'apprenant a obtenu son diplôme
3. Cliquer sur **"Diplômer"**

**Résultat** :
- Le cursus est marqué comme "Diplômé"
- L'apprenant reçoit automatiquement le statut **"Alumni"**
- L'état du cursus passe en "Terminé"

### Suivi des alumni

**Menu** : Limayrac → Contacts → Personnes

**Filtre** : Alumni

- Liste de tous les anciens diplômés
- Possibilité de garder le contact
- Invitations aux événements

---

## Gestion des responsables de formation

### Désigner un responsable de formation

**Menu** : Limayrac → Contacts → Personnes ou depuis la fiche formation

#### Méthode 1 : Depuis la personne

1. Ouvrir ou créer une personne
2. Dans le champ "Formation (Responsable)" : Sélectionner la formation
3. Enregistrer

**Résultat** : La personne est maintenant responsable de cette formation

#### Méthode 2 : Depuis la formation

1. Menu : Limayrac → Formations → Formations
2. Ouvrir la formation
3. Onglet "Responsables"
4. Ajouter une ligne
5. Sélectionner ou créer la personne
6. Renseigner le poste (ex: "Responsable pédagogique")

**Note** : Une formation peut avoir plusieurs responsables (responsable, co-responsable, responsable adjoint, etc.)

### Voir toutes les formations et leurs responsables

**Menu** : Limayrac → Formations → Formations

Chaque formation affiche un compteur "Responsables" en haut à droite.
Cliquer sur le bouton pour voir la liste des responsables.

### Filtrer les responsables de formation

**Menu** : Limayrac → Contacts → Personnes

**Filtre** : "Responsables de formation"

Affiche la liste de toutes les personnes responsables d'au moins une formation.

---

## Gestion des besoins entreprises

### 1. Enregistrement d'un besoin

**Menu** : Limayrac → Formations → Besoins

**Contexte** : Une entreprise partenaire exprime un besoin en alternant/stagiaire

1. Créer un besoin
2. Renseigner :
   - **Titre** : Court descriptif (ex: "Recherche alternant développeur")
   - **Structure** : L'entreprise
   - **Formation** : Formation concernée
   - **Description** : Détails du poste, compétences requises, etc.
   - **Date** : Date de la demande
3. État : "Nouveau" par défaut

### 2. Traitement du besoin

1. Ouvrir le besoin
2. Mettre l'état en **"En cours"** quand vous commencez le traitement
3. Chercher un candidat correspondant :
   - Menu : Limayrac → Candidatures → Vœux
   - Filtre par formation
   - Identifier un candidat accepté
4. Proposer le candidat à l'entreprise
5. Si acceptation :
   - Créer le contrat (voir section [Suivi des contrats](#suivi-des-contrats))
   - Revenir au besoin
   - État : **"Traité"**
   - Ajouter une note : nom du candidat placé
6. Si refus ou non trouvé :
   - État : **"Annulé"** avec explications

### 3. Suivi statistique

**Menu** : Limayrac → Formations → Formations

Sur chaque formation, vous voyez :
- Nombre de besoins enregistrés
- Nombre de vœux reçus
- Nombre de cursus actifs
- Nombre de responsables

Cela permet d'identifier :
- Les formations les plus demandées par les entreprises
- L'adéquation offre/demande

---

## Tableaux de bord et statistiques

### Indicateurs clés

#### Par formation

**Menu** : Limayrac → Formations → Formations

Pour chaque formation :
- **Vœux** : Nombre de candidatures reçues
- **Cursus actifs** : Nombre d'apprenants actuellement en formation
- **Besoins** : Nombre de demandes entreprises

#### Vue d'ensemble

Utilisez les **groupes** dans les recherches :

**Menu** : Limayrac → Candidatures → Cursus
- Grouper par : Formation → Voir la répartition
- Grouper par : État → Voir en cours / terminés

**Menu** : Limayrac → Contrats → Contrats
- Grouper par : Formation → Contrats par formation
- Grouper par : Structure → Entreprises partenaires actives
- Grouper par : Année → Évolution historique

---

## Cas d'usage spécifiques

### Changement de tuteur entreprise en cours de contrat

**Contexte** : Le tuteur change en cours de contrat

1. Ouvrir le contrat
2. Déplacer le tuteur actuel de "Tuteur 1" vers "Tuteur 2"
3. Mettre le nouveau tuteur en "Tuteur 1"
4. **Résultat** : Vous conservez l'historique (2 tuteurs simultanés)
5. Le **Chatter** enregistre automatiquement la modification

### Apprenant avec plusieurs cursus successifs

**Exemple** : BTS puis Bachelor

1. Premier cursus : BTS (2024-2026)
   - Créer le cursus BTS
   - Créer le(s) contrat(s) d'apprentissage
   - En 2026 : Diplômer
2. Second cursus : Bachelor (2026-2027)
   - Créer un nouveau cursus Bachelor
   - La personne reste "Apprenant" et "Alumni"
   - Créer nouveau(x) contrat(s)

### Entreprise avec plusieurs établissements

**Exemple** : Entreprise avec siège à Paris et filiale à Toulouse

1. Créer la première structure (siège, Paris)
   - SIRET : 82345678900015 (SIREN : 823456789)
   - → Le groupe est créé automatiquement
2. Créer la seconde structure (filiale, Toulouse)
   - SIRET : 82345678900023 (même SIREN : 823456789)
   - → Automatiquement liée au même groupe

**Menu** : Limayrac → Contacts → Groupes
- Voir le groupe avec ses 2 structures

---

## Bonnes pratiques

### ✅ À faire

- Mettre à jour régulièrement les notations des contrats
- Utiliser le chatter pour tracer toutes les actions importantes
- Diplômer les apprenants dès l'obtention du diplôme
- Marquer les besoins comme "Traité" une fois le placement effectué
- Vérifier les SIRET lors de la création des structures

### ❌ À éviter

- Ne pas créer plusieurs fois la même personne (vérifier d'abord)
- Ne pas oublier de cocher les statuts (candidat, apprenant, tuteur)
- Ne pas créer de contrat sans cursus associé
- Ne pas laisser les vœux en état "nouveau" trop longtemps

---

## Raccourcis clavier et astuces

### Recherche rapide

- **Ctrl + K** : Recherche globale Odoo
- Taper le nom d'une personne, entreprise, formation

### Filtres sauvegardés

Dans chaque vue, vous pouvez :
1. Configurer vos filtres préférés
2. "Favoris" → "Enregistrer la recherche actuelle"
3. Donner un nom
4. Accessible ensuite en un clic

### Exports

Dans toutes les vues liste :
1. Sélectionner les lignes (ou tout sélectionner)
2. "Action" → "Exporter"
3. Choisir les champs
4. Format : Excel ou CSV

---

## Support et questions

Pour toute question sur l'utilisation :
1. Consulter ce guide
2. Consulter le [README.md](README.md) pour les aspects techniques
3. Contacter l'équipe technique Limayrac

---

**Dernière mise à jour** : Février 2026
