# CRM Limayrac - Modules Odoo

Système de gestion de CRM complet pour l'établissement Limayrac, développé sur Odoo.

## 📋 Vue d'ensemble

Ce projet contient 4 modules Odoo interconnectés pour gérer l'ensemble des activités de l'établissement Limayrac.

**📦 Installation simplifiée** : Installez uniquement le module **"Limayrac - Contrats"** qui installera automatiquement tous les modules nécessaires dans le bon ordre :
1. limayrac_contacts (base)
2. limayrac_formation
3. limayrac_candidature
4. limayrac_contrat

## 🏗️ Architecture

Le projet est basé sur le Modèle Conceptuel de Données (MCD) fourni et s'appuie sur le module `contacts` natif d'Odoo en l'étendant avec des fonctionnalités spécifiques.

### Dépendances entre modules

```
limayrac_contacts (base)
    ↓
limayrac_formation
    ↓
limayrac_candidature
    ↓
limayrac_contrat
```

## 📦 Modules

### 1. limayrac_contacts

**Objectif** : Extension du module `contacts` d'Odoo pour gérer les personnes et structures.

**Modèles** :
- `res.partner` (étendu) : Personnes et structures avec rôles spécifiques
  - Personnes : candidat, apprenant, alumni, intervenant, tuteur, responsable de formation
  - Structures : entreprises avec SIRET, raison sociale, statuts (partenaire, prospect, blacklist, etc.)
- `limayrac.service` : Services au sein des structures
- `limayrac.groupe.structure` : Groupes de structures (SIREN)

**Fonctionnalités** :
- Gestion automatique du lien SIREN/SIRET entre groupes et structures
- Filtres avancés par rôle et statut
- Vue unifiée des personnes et entreprises
- Gestion des responsables de formation (plusieurs responsables par formation)

### 2. limayrac_formation

**Objectif** : Gestion du catalogue de formations.

**Modèles** :
- `limayrac.formation` : Formations proposées
- `limayrac.titre.rncp` : Titres RNCP associés aux formations
- `limayrac.besoin` : Besoins en formation exprimés par les entreprises

**Fonctionnalités** :
- Gestion des responsables de formation (un responsable pour une formation)
- Suivi des besoins entreprises
- Statistiques par formation (vœux, cursus actifs, besoins, responsable
- Statistiques par formation (vœux, cursus actifs, besoins)

### 3. limayrac_candidature

**Objectif** : Gestion du parcours candidat → apprenant → alumni.

**Modèles** :
- `limayrac.voeux` : Candidatures/vœux pour une formation
- `limayrac.cursus` : Cursus d'un apprenant dans une formation

**Fonctionnalités** :
- Workflow de candidature (nouveau → en cours → accepté/refusé)
- Création automatique de cursus après acceptation d'un vœu
- Diplômation et passage automatique en statut alumni
- Suivi des états de cursus (en cours, terminé, abandonné)

### 4. limayrac_contrat

**Objectif** : Gestion des contrats d'alternance/apprentissage.

**Modèles** :
- `limayrac.contrat` : Contrats liant apprenant, cursus, entreprise et tuteurs

**Fonctionnalités** :
- Types de contrats : apprentissage, professionnalisation, stage
- Gestion de 2 tuteurs entreprise simultanés + 1 tuteur école
- Notation et commentaires
- États automatiques (brouillon → en cours → terminé)
- Vue Kanban pour visualisation rapide

## 🚀 Installation

### Prérequis

- Odoo 14.0 ou supérieur
- Python 3.7+
- PostgreSQL 10+

### Étapes d'installation

1. **Copier les modules dans le répertoire addons d'Odoo**

```bash
cd /path/to/odoo/addons
cp -r /path/to/Odoov2/* .
```

2. **Mettre à jour la liste des modules**

Dans Odoo, aller dans :
- Applications → Mettre à jour la liste des applications

3. **Installer le CRM Limayrac**

✅ **Installation simplifiée** : Installer uniquement le module **"Limayrac - Contrats"**

Ce module installera automatiquement tous les modules nécessaires dans le bon ordre :
- limayrac_contacts
- limayrac_formation
- limayrac_candidature
- limayrac_contrat

> ⚠️ **Important** : Ne pas installer les modules séparément, laissez Odoo gérer automatiquement les dépendances.

Pour plus de détails, consultez [INSTALLATION.md](INSTALLATION.md) et [QUICKSTART.md](QUICKSTART.md).

## 📊 Utilisation

### Workflow typique

1. **Création d'une structure entreprise**
   - Menu : Limayrac → Contacts → Structures
   - Renseigner SIRET, raison sociale, etc.
   - Le groupe (SIREN) est créé automatiquement

2. **Création d'un service dans la structure**
   - Depuis la fiche structure, onglet "Informations Limayrac"
   - Ou Menu : Limayrac → Contacts → Services

3. **Création d'une formation**
   - Menu : Limayrac → Formations → Formations
   - Ajouter les titres RNCP associés

4. **Gestion d'une candidature**
   - Menu : Limayrac → Candidatures → Vœux
   - Créer un vœu pour un candidat
   - Actions : Accepter, Refuser, Annuler
   - Après acceptation, créer un cursus

5. **Création d'un cursus**
   - Menu : Limayrac → Candidatures → Cursus
   - Associer l'apprenant à une formation
   - La personne devient automatiquement "Apprenant"

6. **Création d'un contrat**
   - Menu : Limayrac → Contrats → Contrats
   - Sélectionner l'apprenant (charge automatiquement le cursus actif)
   - Associer à un service et désigner les tuteurs
   - Le contrat passe automatiquement "en cours" à la date de début

## 🔧 Personnalisation

### Ajouter des champs personnalisés

Exemple pour ajouter un champ à `res.partner` :

```python
class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    mon_champ = fields.Char(string='Mon champ')
```

### Modifier les vues

Les vues se trouvent dans le dossier `views/` de chaque module.

## 📈 Statistiques et rapports

Chaque module propose des vues statistiques :

- **Formations** : Nombre de vœux, cursus actifs, besoins
- **Cursus** : Bouton smart pour accéder aux contrats
- **Structures** : Nombre de services, personnes associées

## 🔐 Sécurité

Les droits d'accès sont définis dans les fichiers `security/ir.model.access.csv` de chaque module.

Par défaut, tous les utilisateurs (`base.group_user`) ont accès en lecture/écriture/création/suppression.

Pour restreindre les accès, modifier ces fichiers selon vos besoins.

## 🐛 Dépannage

### Le module ne s'installe pas

- Vérifier les dépendances
- Consulter les logs Odoo : `/var/log/odoo/odoo-server.log`
- Vérifier la syntaxe des fichiers Python et XML

### Erreur de droits d'accès

- Vérifier les fichiers `ir.model.access.csv`
- Mettre à jour les droits si nécessaire

### Les relations ne fonctionnent pas

- S'assurer que les modules sont installés dans le bon ordre
- Redémarrer le serveur Odoo après modification

## 📝 Notes techniques

### Relations importantes

- **PERSONNE ↔ SERVICE** : Many2one (une personne appartient à un service)
- **STRUCTURE ↔ GROUPE_STRUCTURE** : Many2one (plusieurs structures dans un groupe)
- **CONTRAT → CURSUS** : Many2one (plusieurs contrats possibles par cursus)
- **CONTRAT → TUTEURS** : Many2one (2 tuteurs entreprise + 1 tuteur école)

### Champs calculés

- `state` dans cursus et contrat : calculé automatiquement selon les dates
- `is_active` dans titre RNCP : calculé selon les dates de validité
- Compteurs (`*_count`) : calculés dynamiquement

### Contraintes

- Dates de début/fin cohérentes (fin > début)
- SIREN unique dans groupe_structure

## 🤝 Contribution

Pour proposer des améliorations :

1. Créer une branche pour votre fonctionnalité
2. Développer et tester
3. Soumettre une pull request

## 📄 License

Développé pour l'établissement Limayrac - Tous droits réservés

---

**Version** : 1.0  
**Date** : Février 2026  
**Auteur** : Limayrac
