# Solution au problème de chargement des données

## Problème initial

L'erreur `External ID not found: limayrac_candidature.cursus_moreau` se produisait car :
- Le module `limayrac_contrat` essayait de charger ses données
- Ces données référençaient `limayrac_candidature.cursus_moreau`
- Mais `limayrac_candidature` n'avait pas encore chargé ses données

## Solution mise en place

### Module limayrac_demo

Un nouveau module **`limayrac_demo`** a été créé pour centraliser toutes les données de démonstration.

**Avantages :**
✅ Toutes les données sont dans un seul fichier, chargées dans le bon ordre
✅ Plus de problèmes de références inter-modules
✅ Installation simple et fiable
✅ Module optionnel - on peut l'installer ou non selon les besoins
✅ Les modules principaux restent propres sans données de test

### Structure du module

```
limayrac_demo/
├── __init__.py (vide)
├── __manifest__.py (manifeste du module)
├── README.md (documentation)
└── data/
    └── demo_data.xml (toutes les données consolidées)
```

### Changements dans les autres modules

Les fichiers `demo/demo_data.xml` sont restés dans chaque module mais dans la section `demo:` des manifests.

Cela permet :
- De garder les données "proche" de leur module source
- D'installer le module `limayrac_demo` comme source unique de vérité
- De ne pas dupliquer le code (les fichiers originaux sont conservés comme référence)

## Installation sur le serveur distant

### Étape 1 : Upload des modules

Uploadez **tous les dossiers** suivants sur votre serveur :
- limayrac_contacts
- limayrac_formation
- limayrac_candidature
- limayrac_contrat
- **limayrac_demo** ← NOUVEAU !

### Étape 2 : Installer dans l'ordre

Via l'interface Odoo :

1. Applications → Mode Développeur → Mettre à jour liste
2. Installer dans l'ordre :
   - limayrac_contacts
   - limayrac_formation
   - limayrac_candidature
   - limayrac_contrat
   - **limayrac_demo** (en dernier !)

### Étape 3 : Vérifier

Après installation de `limayrac_demo`, vous devriez avoir :
- ~20 personnes (candidats, apprenants, alumni, intervenants, tuteurs)
- ~6 structures d'entreprises
- 5 formations
- 6 vœux / 7 cursus
- 6 contrats

## Fichiers modifiés

1. **Nouveaux fichiers créés :**
   - `limayrac_demo/__init__.py`
   - `limayrac_demo/__manifest__.py`
   - `limayrac_demo/README.md`
   - `limayrac_demo/data/demo_data.xml`

2. **Fichiers modifiés :**
   - Tous les `__manifest__.py` (version 1.0.1, section demo remise)
   - `limayrac_contrat/models/limayrac_contrat.py` (domaine apprenant_id)
   - `limayrac_candidature/models/limayrac_cursus.py` (domaine apprenant_id)
   - `limayrac_formation/models/__init__.py` (ordre d'import)
   - `INSTRUCTIONS_MAJ.md` (nouvelle procédure)

## Avantages de cette solution

✅ **Fiable** : Un seul point de chargement, plus de problèmes d'ordre
✅ **Flexible** : Module optionnel, on peut choisir d'avoir ou non les données
✅ **Maintenable** : Toutes les données de démo au même endroit
✅ **Compatible serveur distant** : Aucun script à exécuter, juste installer le module
✅ **Propre** : Les modules principaux ne sont pas pollués par les données de test

## En cas de problème

Si vous avez encore des erreurs :

1. Désinstallez `limayrac_demo`
2. Vérifiez que les 4 modules principaux sont bien installés
3. Réinstallez `limayrac_demo`

Si ça ne fonctionne toujours pas, vérifiez les logs Odoo pour voir l'erreur exacte.
