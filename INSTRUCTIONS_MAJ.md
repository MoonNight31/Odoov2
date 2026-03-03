# Instructions de mise à jour des modules Limayrac

## Pour le serveur distant

### ⚠️ NOUVELLE MÉTHODE SIMPLIFIÉE ⚠️

Un nouveau module **`limayrac_demo`** a été créé pour faciliter le chargement des données de démonstration.

### Procédure d'installation avec données de démonstration

1. **Uploader tous les modules** sur votre serveur dans le dossier des addons Odoo :
   - limayrac_contacts
   - limayrac_formation
   - limayrac_candidature
   - limayrac_contrat
   - **limayrac_demo** (nouveau !)

2. **Mettre à jour la liste des applications** :
   - Connectez-vous à Odoo en tant qu'administrateur
   - Allez dans **Applications**
   - Activez le **Mode Développeur** (icône insecte)
   - Cliquez sur **Mettre à jour la liste des applications**

3. **Installer les modules dans l'ordre** :
   ```
   1. limayrac_contacts
   2. limayrac_formation
   3. limayrac_candidature
   4. limayrac_contrat
   5. limayrac_demo (★ IMPORTANT : en dernier !)
   ```

4. **C'est tout !** Les données de démonstration seront automatiquement chargées lors de l'installation de `limayrac_demo`

### Option 2 : Installation sans données de démonstration

Si vous ne voulez **PAS** de données de démonstration, installez simplement les 4 premiers modules et **ne pas installer** `limayrac_demo`.

### Vérification du chargement des données

Après l'installation de `limayrac_demo`, vérifiez que les données sont bien présentes :

- **Contacts** : ~20 personnes et ~6 structures
- **Formations** : 5 formations avec titres RNCP
- **Candidatures** : ~9 vœux et ~7 cursus
- **Contrats** : 6 contrats

### Structure des dépendances

```
limayrac_contacts (base)
    ↓
limayrac_formation (dépend de limayrac_contacts)
    ↓
limayrac_candidature (dépend de limayrac_contacts et limayrac_formation)
    ↓
limayrac_contrat (dépend de tous les modules précédents)
    ↓
limayrac_demo (dépend de tous les modules - OPTIONNEL)
```

## Données incluses

### limayrac_contacts
- 6 structures d'entreprises
- 7 services
- 6 candidats
- 2 apprenants actuels
- 2 alumni
- 4 intervenants/formateurs
- 5 tuteurs entreprise
- 6 types d'activité

### limayrac_formation
- 5 formations (BTS SIO, BTS NDRC, Bachelor, BTS MCO, BTS SAM)
- 4 titres RNCP
- 3 responsables de formation
- 5 besoins d'entreprises
- 5 opportunités

### limayrac_candidature
- 6 vœux (candidatures à différents stades)
- 7 cursus (dont 2 diplômés)

### limayrac_contrat
- 6 contrats (apprentissage, professionnalisation, stage)

## Version actuelle

Version des modules : **1.0.1**

Date de dernière mise à jour : 3 mars 2026
