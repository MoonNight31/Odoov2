# Guide d'installation rapide - CRM Limayrac

## Installation rapide

### 1. Prérequis
- Odoo 14.0 ou supérieur installé et fonctionnel
- Accès administrateur à Odoo

### 2. Installation des modules

#### Méthode 1 : Via l'interface Odoo (recommandée)

1. **Copier les modules**
   ```bash
   # Linux/Mac
   cp -r limayrac_* /path/to/odoo/addons/
   
   # Windows (PowerShell)
   Copy-Item -Recurse limayrac_* C:\path\to\odoo\addons\
   ```

2. **Redémarrer Odoo**
   ```bash
   # Linux
   sudo systemctl restart odoo
   
   # Ou si lancé manuellement
   ./odoo-bin --addons-path=/path/to/addons
   ```

3. **Activer le mode développeur**
   - Se connecter à Odoo
   - Paramètres → Activer le mode développeur

4. **Mettre à jour la liste des applications**
   - Applications → Mettre à jour la liste des applications

5. **Installer le module principal**
   - Applications → Rechercher "Limayrac"
   - Installer "Limayrac - Contrats" (installera automatiquement les dépendances)

#### Méthode 2 : Via la ligne de commande

```bash
./odoo-bin -d nom_base_de_donnees -i limayrac_contacts,limayrac_formation,limayrac_candidature,limayrac_contrat --stop-after-init
```

### 3. Vérification

Après installation, vous devriez voir dans le menu principal :
- **Limayrac** (menu principal)
  - Contacts
  - Formations
  - Candidatures
  - Contrats

### 4. Configuration initiale

#### Créer les données de base

1. **Créer quelques formations**
   - Menu : Limayrac → Formations → Formations
   - Ajouter au minimum 2-3 formations avec leurs codes RNCP

2. **Créer des structures entreprises**
   - Menu : Limayrac → Contacts → Structures
   - Créer 2-3 entreprises tests avec SIRET

3. **Créer des personnes**
   - Menu : Limayrac → Contacts → Personnes
   - Créer quelques profils : candidats, intervenants, tuteurs

## Données de démonstration (optionnel)

Pour créer des données de test rapidement, vous pouvez utiliser ce script Python dans une console Odoo :

```python
# Créer une formation
formation = env['limayrac.formation'].create({
    'nom_commercial': 'BTS SIO - Services Informatiques aux Organisations'
})

# Créer un titre RNCP
titre = env['limayrac.titre.rncp'].create({
    'code_rncp': 'RNCP35340',
    'intitule': 'BTS Services Informatiques aux Organisations',
    'formation_id': formation.id,
})

# Créer une structure
structure = env['res.partner'].create({
    'name': 'TechCorp Solutions',
    'is_company': True,
    'siret': '12345678900015',
    'raison_sociale': 'TechCorp Solutions SAS',
    'is_partenaire': True,
})

# Créer un service
service = env['limayrac.service'].create({
    'type_service': 'Informatique',
    'structure_id': structure.id,
})

# Créer un candidat
candidat = env['res.partner'].create({
    'name': 'Dupont Jean',
    'email': 'jean.dupont@example.com',
    'phone': '0601020304',
    'is_candidat': True,
})

# Créer un vœu
voeux = env['limayrac.voeux'].create({
    'apprenant_id': candidat.id,
    'formation_id': formation.id,
    'date_candidature': '2026-01-15',
})

print("Données de démonstration créées avec succès!")
```

## Résolution des problèmes courants

### Erreur : "Module not found"
- Vérifier que les dossiers sont bien dans le répertoire addons
- Vérifier les droits d'accès (chmod 755)
- Redémarrer Odoo

### Erreur : "Access denied"
- Vérifier les fichiers `ir.model.access.csv`
- Se déconnecter/reconnecter
- Vider le cache du navigateur

### Les menus n'apparaissent pas
- Vérifier que les modules sont bien installés (pas seulement téléchargés)
- Rafraîchir la page (Ctrl+F5)
- Se déconnecter/reconnecter

### Erreur de dépendances
Installer les modules dans cet ordre :
1. limayrac_contacts
2. limayrac_formation
3. limayrac_candidature
4. limayrac_contrat

## Prochaines étapes

Après installation réussie :
1. Lire le [README.md](README.md) complet pour comprendre l'architecture
2. Créer vos formations
3. Importer vos contacts existants
4. Former les utilisateurs au workflow

## Support

En cas de problème persistant :
1. Consulter les logs Odoo
2. Vérifier la documentation Odoo officielle
3. Contacter l'équipe technique Limayrac
