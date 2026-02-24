# 🚀 Démarrage Rapide - CRM Limayrac

## ⚡ Installation en 5 minutes

### 1. Copier les modules
```bash
# Windows PowerShell
Copy-Item -Recurse limayrac_* "C:\Program Files\Odoo 14.0\server\odoo\addons\"

# Linux
cp -r limayrac_* /opt/odoo/addons/
```

### 2. Redémarrer Odoo
```bash
# Service Windows
Restart-Service odoo-server-14.0

# Service Linux
sudo systemctl restart odoo
```

### 3. Installer les modules
1. Se connecter à Odoo : http://localhost:8069
2. Applications → Mettre à jour la liste des applications
3. Rechercher "Limayrac"
4. Installer "Limayrac - Contrats" (installe tout)

### 4. Créer les données de test (optionnel)
1. Paramètres → Technique → Python Code
2. Copier/coller le contenu de `demo_data.py`
3. Exécuter

## 📖 Documentation

| Document | À lire pour... |
|----------|----------------|
| [README.md](README.md) | Comprendre le projet |
| [INSTALLATION.md](INSTALLATION.md) | Installer en détail |
| [WORKFLOW.md](WORKFLOW.md) | Utiliser au quotidien |
| [FEATURES.md](FEATURES.md) | Découvrir les fonctionnalités |
| [STRUCTURE.md](STRUCTURE.md) | Architecture technique |
| [INDEX.md](INDEX.md) | Index de tous les fichiers |

## 🎯 Premiers pas

### Scénario 1 : Créer une formation
1. Menu : Limayrac → Formations → Formations
2. Créer
3. Nom commercial : "BTS SIO"
4. Ajouter un titre RNCP dans l'onglet correspondant

### Scénario 2 : Ajouter une entreprise partenaire
1. Menu : Limayrac → Contacts → Structures
2. Créer
3. Type : Entreprise
4. Renseigner SIRET (le groupe sera créé automatiquement)
5. Cocher "Partenaire" dans l'onglet Limayrac
6. Ajouter des services

### Scénario 3 : Traiter une candidature
1. Menu : Limayrac → Contacts → Personnes
2. Créer un candidat (cocher "Candidat")
3. Menu : Limayrac → Candidatures → Vœux
4. Créer un vœu pour ce candidat
5. Accepter le vœu
6. Le cursus se crée automatiquement

### Scénario 4 : Créer un contrat
1. Menu : Limayrac → Contrats → Contrats
2. Créer
3. Sélectionner l'apprenant (le cursus se charge)
4. Sélectionner le service entreprise
5. Choisir les tuteurs
6. Enregistrer

## 🔍 Navigation rapide

### Accès aux modules
```
Odoo → Menu principal "Limayrac" (icône en haut)
```

### Structure des menus
```
Limayrac
  ├── Contacts (Personnes, Structures, Services, Groupes)
  ├── Formations (Formations, Titres RNCP, Besoins)
  ├── Candidatures (Vœux, Cursus)
  └── Contrats (Contrats)
```

## 💡 Astuces

### Recherche rapide
- **Ctrl + K** puis taper un nom
- Recherche dans tous les modules

### Filtres favoris
1. Configurer vos filtres
2. "Favoris" → "Enregistrer"
3. Accessible en 1 clic ensuite

### Export de données
1. Vue liste → Sélectionner
2. Action → Exporter
3. Choisir format Excel/CSV

## 🎓 Workflows principaux

### Workflow Candidature → Diplôme
```
1. Créer contact (Candidat)
2. Créer vœu
3. Accepter vœu → Créer cursus
4. Créer contrat
5. Diplômer → Statut Alumni
```

### Workflow Besoin entreprise
```
1. Entreprise exprime besoin
2. Créer besoin (état: nouveau)
3. Chercher candidat correspondant
4. Proposer et créer contrat
5. Marquer besoin comme traité
```

## ⚠️ Points d'attention

### ✅ À faire
- Vérifier les SIRET (14 chiffres)
- Cocher les statuts (candidat, tuteur, etc.)
- Diplômer les apprenants en fin de cursus
- Traiter les besoins rapidement

### ❌ À éviter
- Ne pas créer de doublons de contacts
- Ne pas oublier de créer le cursus après acceptation
- Ne pas laisser les vœux "nouveau" trop longtemps

## 🆘 Dépannage rapide

### Module non visible après installation
- Vider le cache navigateur (Ctrl+F5)
- Se déconnecter/reconnecter
- Vérifier que le module est bien "Installé"

### Erreur de droits
- Vérifier `security/ir.model.access.csv`
- Se reconnecter
- Vérifier le groupe utilisateur

### Les menus n'apparaissent pas
- Rafraîchir (F5)
- Mode développeur : Paramètres → Activer le mode développeur
- Vérifier les fichiers `views/menus.xml`

## 📊 Indicateurs clés

### À suivre
- Nombre de vœux par formation
- Taux d'acceptation des vœux
- Nombre de cursus actifs
- Nombre de contrats en cours
- Besoins entreprises non traités

### Tableaux de bord
Utiliser les groupements dans les recherches :
- Grouper par Formation
- Grouper par État
- Grouper par Année

## 🔗 Liens utiles

### Documentation Odoo
- [Documentation officielle](https://www.odoo.com/documentation/)
- [Forum communautaire](https://www.odoo.com/forum/)
- [Apps Odoo](https://apps.odoo.com/)

### Modules Limayrac
- Tous les fichiers dans `/limayrac_*/`
- Documentation dans `/README.md` et autres `.md`
- Script démo dans `/demo_data.py`

## 📞 Support

### En cas de problème
1. Consulter [WORKFLOW.md](WORKFLOW.md)
2. Consulter [README.md](README.md)
3. Vérifier les logs : `/var/log/odoo/`
4. Contacter l'équipe technique

## 🎉 Félicitations !

Vous êtes prêt à utiliser le CRM Limayrac !

### Prochaines étapes
1. ✅ Installation terminée
2. ▶️ Créer vos premières formations
3. ▶️ Importer vos contacts existants
4. ▶️ Former les utilisateurs
5. ▶️ Commencer à traiter les candidatures

---

**Besoin d'aide ?** Consultez la [documentation complète](README.md)
