# Instructions de Mise à Jour v1.0.3 - Modules Limayrac

**Date :** Mai 2024  
**Version :** 1.0.3  
**Modules concernés :** limayrac_contacts, limayrac_demo

---

## 🎯 Résumé des Modifications

### Nouveautés de la version 1.0.3

1. **Séparation des vues Personnes/Structures** dans l'interface utilisateur
2. **Enrichissement massif des données de démonstration** (x3 plus de données)
3. **Amélioration de l'organisation** des menus et de la navigation

---

## 📦 Module limayrac_contacts (v1.0.3)

### Amélioration de l'Interface Utilisateur

**Problème résolu :** Les personnes et les structures apparaissaient mélangées dans le même menu, rendant la navigation confuse.

**Solution :** Création de deux menus distincts avec filtres automatiques :

#### Menu "Personnes"
- Affiche uniquement les contacts individuels (`is_company = False`)
- Regroupe : candidats, apprenants, alumni, intervenants, tuteurs
- Filtre automatique pour exclure les entreprises

#### Menu "Structures"  
- Affiche uniquement les organisations (`is_company = True`)
- Regroupe : partenaires, prospects, entreprises de taxe d'apprentissage
- Filtre automatique pour exclure les individus

### Fichiers Modifiés

```
limayrac_contacts/
├── views/
│   └── menus.xml ← Actions distinctes ajoutées
└── __manifest__.py ← Version 1.0.3
```

---

## 📊 Module limayrac_demo (v1.0.3)

### Enrichissement Massif des Données

Le module de démonstration a été considérablement enrichi pour offrir un environnement de test plus réaliste.

#### Statistiques des Données Enrichies

| Type de Donnée | Avant (v1.0.2) | Après (v1.0.3) | Augmentation |
|----------------|----------------|----------------|--------------|
| **Structures** | 6 | 14 | +133% |
| **Personnes** | ~20 | ~50 | +150% |
| **Formations** | 5 | 9 | +80% |
| **Cursus** | 7 | 17 | +143% |
| **Contrats** | 6 | 14 | +133% |
| **Opportunités** | 0 | 6 | Nouveau |
| **Besoins Formation** | 0 | 7 | Nouveau |

### Détail des Nouvelles Données

#### 🏢 Structures Ajoutées (8 nouvelles)

1. **Datalytics France** - Data & Analytics (Ramonville)
2. **MediaCo Communication** - Communication digitale (Toulouse)
3. **RetailMax Distribution** - E-commerce & Distribution (Portet-sur-Garonne)
4. **CyberSec Solutions** - Cybersécurité (Labège)
5. **GreenTech Innovations** - Ingénierie environnementale (Balma)
6. **SmartFinance Conseil** - Conseil financier (Toulouse)
7. **FoodDelivery Express** - Livraison restauration (Toulouse)
8. **HealthApp Systems** - Applications santé (Toulouse)

#### 👥 Contacts Ajoutés (30+ nouveaux)

**Candidats (10 nouveaux) :**
- Marie Dubois, Lucas Martinez, Sophie Bernard, Alexandre Petit
- Camille Roux, Thomas Fournier, Julie Giraud, Nathan Moreau
- Anaïs Laurent, Maxime Bonnet

**Apprenants (8 nouveaux) :**
- Élise Durand, Nicolas Lefèvre, Clara Simon, Hugo Michel
- Manon Garcia, Théo Martin, Sarah Lopez, Dylan André

**Alumni (4 nouveaux) :**
- Pauline Richard (Data Analyst)
- Julien Blanc (Responsable Marketing Digital)
- Lisa Henry (DevOps Engineer)
- Kevin Rousseau (Commercial BtoB)

**Intervenants (6 nouveaux) :**
- Vincent Dupont (Base de Données)
- Catherine Faure (E-commerce)
- Marc Garnier (Cybersécurité)
- Isabelle Fabre (Communication)
- Alain Mercier (Systèmes et Virtualisation)
- Nathalie Chevalier (Droit et Entreprise)

**Tuteurs Entreprise (7 nouveaux) :**
- Un tuteur par nouvelle structure avec fonctions réalistes

#### 🎓 Formations Ajoutées (4 nouvelles)

1. **BTS NDRC** - Négociation et Digitalisation Relation Client
2. **Licence Pro Cybersécurité** - Alternance 1 an
3. **Master Data Science et IA** - Alternance 2 ans
4. **Bachelor Webdesign et Développement** - Alternance 1 an

#### 📋 Cursus Ajoutés (10 nouveaux)

Dossiers de candidature avec statuts variés :
- **Admis** : Marie Dubois, Lucas Martinez, Alexandre Petit, Julie Giraud, Maxime Bonnet
- **En cours** : Sophie Bernard, Nathan Moreau
- **En attente** : Thomas Fournier, Anaïs Laurent
- **Refusé** : Camille Roux

#### 📝 Contrats Ajoutés (8 nouveaux)

- Apprentissage : Datalytics, CyberSec, RetailMax, HealthApp
- Professionnalisation : MediaCo, SmartFinance
- Différents statuts : en_cours, signé, projet

#### 💼 Opportunités Ajoutées (6 nouvelles)

1. **Datalytics** - Alternant Data Analyst (2 postes - 1400€)
2. **MediaCo** - Assistant Communication Digitale (900€)
3. **RetailMax** - Développeur Web E-commerce (1200€ - pourvue)
4. **CyberSec** - Analyste SOC Junior (2 postes - 1300€)
5. **HealthApp** - Développeur Full Stack (1250€ - suspendue)
6. **SmartFinance** - Chargé de clientèle junior (1000€)

#### 📚 Besoins Formation Ajoutés (7 nouveaux)

- **Formation continue** : Python avancé, E-commerce, RGPD santé, RSE
- **Recrutement alternants** : Communication, SOC, Conseiller clientèle

### Fichiers Modifiés

```
limayrac_demo/
├── data/
│   ├── demo_data.xml ← Données initiales (inchangées)
│   └── demo_data_enriched.xml ← NOUVEAU (800+ lignes)
└── __manifest__.py ← Version 1.0.3, description enrichie
```

---

## 🚀 Procédure de Mise à Jour 

### Option 1 : Mise à Jour Simple (Recommandée)

Si les modules sont déjà installés :

1. **Téléchargement**
   ```bash
   # Copier les modules vers le serveur
   scp -r limayrac_contacts/ user@172.18.0.27:/chemin/odoo/addons/
   scp -r limayrac_demo/ user@172.18.0.27:/chemin/odoo/addons/
   ```

2. **Redémarrage Odoo**
   ```bash
   ssh user@172.18.0.27
   sudo systemctl restart odoo
   # OU
   docker restart odoo_container
   ```

3. **Mise à jour via Interface**
   - Paramètres → Applications → Mettre à jour la liste des applications
   - Rechercher "limayrac_contacts" → **Mettre à niveau**
   - Rechercher "limayrac_demo" → **Mettre à niveau**

### Option 2 : Réinstallation Complète

Si vous rencontrez des problèmes :

1. **Désinstaller** limayrac_demo
2. **Mettre à jour** limayrac_contacts
3. **Réinstaller** limayrac_demo

⚠️ **Attention** : La réinstallation de limayrac_demo peut créer des doublons si vous aviez déjà des données manuelles.

---

## ✅ Vérifications Post-Installation

### Test 1 : Menus Personnes/Structures

1. Aller dans **Contacts**
2. Vérifier l'existence de deux menus distincts :
   - Menu **"Personnes"** → Doit afficher uniquement individus
   - Menu **"Structures"** → Doit afficher uniquement entreprises

### Test 2 : Données Enrichies

| Vérification | Accès | Nombre Attendu |
|--------------|-------|----------------|
| Structures | Contacts → Structures | 14-15 |
| Personnes | Contacts → Personnes | 45-50 |
| Candidats | Contacts → Personnes (filtre) | 15-20 |
| Formations | Formation → Formations | 8-9 |
| Cursus | Candidature → Cursus | 15-17 |
| Contrats | Contrat → Contrats | 12-14 |
| Opportunités | Formation → Opportunités | 5-6 |

### Test 3 : Cohérence des Données

Vérifier quelques exemples :
- **Datalytics France** (structure) → Service "Data & Analytics" → Tuteur "François Renard"
- **Élise Durand** (apprenante) → Contrat avec Datalytics → Cursus Master Data Science
- **Marie Dubois** (candidate) → Cursus BTS NDRC → Statut "admis"

---

## 🔧 Résolution des Problèmes

### Erreur : "External ID not found"

**Cause :** Ordre d'installation incorrect ou module dépendant non mis à jour

**Solution :**
```bash
# Mettre à jour dans l'ordre :
1. limayrac_contacts
2. limayrac_formation  
3. limayrac_candidature
4. limayrac_contrat
5. limayrac_demo (en dernier)
```

### Erreur : "Duplicate key SIREN"

**Cause :** Données existantes en conflit avec les nouvelles données demo

**Solution 1** (Interface) :
- Identifier les structures en doublon
- Supprimer manuellement les anciennes

**Solution 2** (SQL) :
```sql
-- Voir les doublons
SELECT name, siret, COUNT(*) 
FROM res_partner 
WHERE siret IS NOT NULL 
GROUP BY name, siret 
HAVING COUNT(*) > 1;

-- Supprimer les doublons (attention !)
DELETE FROM res_partner 
WHERE id IN (
    SELECT id FROM res_partner 
    WHERE siret = 'SIRET_EN_DOUBLON' 
    LIMIT 1
);
```

### Les Nouveaux Menus N'Apparaissent Pas

**Solution :**
1. Vider le cache navigateur : `Ctrl+Shift+R`
2. Se déconnecter/reconnecter
3. Vérifier version limayrac_contacts : doit être **1.0.3**
4. Mise à jour forcée :
   ```bash
   # En ligne de commande
   odoo-bin -u limayrac_contacts -d nom_base --stop-after-init
   ```

---

## 📋 Checklist de Mise à Jour

- [ ] Sauvegarde de la base de données effectuée
- [ ] Modules copiés sur le serveur
- [ ] Service Odoo redémarré
- [ ] Liste des applications mise à jour
- [ ] Module limayrac_contacts mis à jour (v1.0.3)
- [ ] Module limayrac_demo mis à jour (v1.0.3)
- [ ] Vérification : Menu "Personnes" existe
- [ ] Vérification : Menu "Structures" existe
- [ ] Vérification : 14+ structures présentes
- [ ] Vérification : 45+ personnes présentes
- [ ] Vérification : 15+ cursus présents
- [ ] Vérification : 12+ contrats présents
- [ ] Test : Navigation fluide entre les menus
- [ ] Test : Filtres fonctionnent correctement

---

## 📞 Support

**En cas de problème :**

1. Consulter les logs Odoo :
   ```bash
   tail -f /var/log/odoo/odoo-server.log
   ```

2. Mode développeur Odoo :
   - Activer : Paramètres → Mode développeur
   - Voir erreurs techniques détaillées

3. Vérifier versions de tous les modules :
   - Applications → Filtrer par "limayrac"
   - Tous doivent être en 1.0.2 ou 1.0.3

---

## 📈 Améliorations Futures Prévues

- **v1.1.0** : Ajout de tableaux de bord et statistiques
- **v1.2.0** : Gestion des paiements et facturation
- **v1.3.0** : Portail candidat en ligne

---

**Dernière modification :** 2024-05-XX  
**Auteur :** Équipe Technique Limayrac
