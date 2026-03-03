# Instructions de mise à jour des modules Limayrac

## Pour le serveur distant

### Option 1 : Mise à jour via l'interface Odoo

1. Connectez-vous à Odoo en tant qu'administrateur
2. Allez dans **Applications**
3. En haut à droite, activez le **Mode Développeur** (icône insecte)
4. Cliquez sur **Mettre à jour la liste des applications**
5. Mettez à jour les modules **UN PAR UN** dans cet ordre :

   ```
   1. limayrac_contacts
   2. limayrac_formation
   3. limayrac_candidature
   4. limayrac_contrat
   ```

   ⚠️ **IMPORTANT** : Attendez que chaque mise à jour soit complètement terminée avant de passer à la suivante !

### Option 2 : Mise à jour via ligne de commande SSH

Connectez-vous au serveur et exécutez :

```bash
# Se connecter au conteneur Odoo (si Docker)
docker exec -it nom_conteneur_odoo bash

# Ou directement sur le serveur, exécuter :
odoo-bin -d nom_base_donnees \
  -u limayrac_contacts,limayrac_formation,limayrac_candidature,limayrac_contrat \
  --stop-after-init
```

### Vérification du chargement des données

Après la mise à jour, vérifiez que les données sont bien présentes :

- **Contacts** : Doit contenir ~20 personnes et ~6 structures
- **Formations** : Doit contenir 5 formations
- **Candidatures** : Doit contenir ~9 vœux et ~7 cursus
- **Contrats** : Doit contenir 6 contrats

### En cas d'erreur "External ID not found"

Si vous obtenez une erreur indiquant qu'un ID externe n'est pas trouvé, c'est que les modules n'ont pas été mis à jour dans le bon ordre. Procédure de récupération :

1. Supprimez tous les enregistrements créés manuellement dans les modules
2. Désinstallez les modules dans l'ordre inverse :
   - limayrac_contrat
   - limayrac_candidature
   - limayrac_formation
   - limayrac_contacts
3. Réinstallez-les dans l'ordre correct (voir ci-dessus)

### Structure des dépendances

```
limayrac_contacts (base)
    ↓
limayrac_formation (dépend de limayrac_contacts)
    ↓
limayrac_candidature (dépend de limayrac_contacts et limayrac_formation)
    ↓
limayrac_contrat (dépend de tous les modules précédents)
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
