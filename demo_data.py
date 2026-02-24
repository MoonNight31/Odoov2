# Script de données de démonstration pour CRM Limayrac
# À exécuter dans la console Python d'Odoo

# Ce script crée des données de test pour tous les modules Limayrac

# ============================================
# 1. FORMATIONS
# ============================================

print("Création des formations...")

formation_bts_sio = env['limayrac.formation'].create({
    'nom_commercial': 'BTS SIO - Services Informatiques aux Organisations',
    'description': 'Formation aux métiers de l\'informatique et du développement'
})

formation_bts_ndrc = env['limayrac.formation'].create({
    'nom_commercial': 'BTS NDRC - Négociation et Digitalisation de la Relation Client',
    'description': 'Formation aux métiers du commerce et de la vente'
})

formation_bachelor_dev = env['limayrac.formation'].create({
    'nom_commercial': 'Bachelor Développeur Full Stack',
    'description': 'Formation avancée en développement web et mobile'
})

# Titres RNCP
env['limayrac.titre.rncp'].create({
    'code_rncp': 'RNCP35340',
    'intitule': 'BTS Services Informatiques aux Organisations',
    'formation_id': formation_bts_sio.id,
    'date_debut': '2020-01-01',
})

env['limayrac.titre.rncp'].create({
    'code_rncp': 'RNCP38368',
    'intitule': 'BTS Négociation et Digitalisation de la Relation Client',
    'formation_id': formation_bts_ndrc.id,
    'date_debut': '2021-01-01',
})

env['limayrac.titre.rncp'].create({
    'code_rncp': 'RNCP36442',
    'intitule': 'Concepteur développeur d\'applications',
    'formation_id': formation_bachelor_dev.id,
    'date_debut': '2022-01-01',
})

print(f"✓ {len([formation_bts_sio, formation_bts_ndrc, formation_bachelor_dev])} formations créées")

# ============================================
# 2. STRUCTURES ET SERVICES
# ============================================

print("Création des structures...")

# Structure 1 : TechCorp
techcorp = env['res.partner'].create({
    'name': 'TechCorp Solutions',
    'is_company': True,
    'siret': '82345678900015',
    'raison_sociale': 'TechCorp Solutions SAS',
    'street': '15 Avenue de l\'Innovation',
    'zip': '31000',
    'city': 'Toulouse',
    'phone': '0561123456',
    'email': 'contact@techcorp.fr',
    'website': 'https://www.techcorp.fr',
    'is_partenaire': True,
    'is_taxe_apprentissage': True,
})

service_techcorp_dev = env['limayrac.service'].create({
    'type_service': 'Département Développement',
    'structure_id': techcorp.id,
})

service_techcorp_infra = env['limayrac.service'].create({
    'type_service': 'Département Infrastructure',
    'structure_id': techcorp.id,
})

# Structure 2 : Digital Partners
digital = env['res.partner'].create({
    'name': 'Digital Partners',
    'is_company': True,
    'siret': '75123456700023',
    'raison_sociale': 'Digital Partners SARL',
    'street': '42 Rue du Numérique',
    'zip': '31200',
    'city': 'Toulouse',
    'phone': '0561987654',
    'email': 'contact@digitalpartners.fr',
    'is_partenaire': True,
    'is_prospect': False,
})

service_digital_web = env['limayrac.service'].create({
    'type_service': 'Pôle Web',
    'structure_id': digital.id,
})

# Structure 3 : Commerce Plus (pour BTS NDRC)
commerce = env['res.partner'].create({
    'name': 'Commerce Plus',
    'is_company': True,
    'siret': '89012345600018',
    'raison_sociale': 'Commerce Plus SA',
    'street': '7 Boulevard du Commerce',
    'zip': '31100',
    'city': 'Toulouse',
    'phone': '0561456789',
    'email': 'rh@commerceplus.fr',
    'is_partenaire': True,
})

service_commerce_vente = env['limayrac.service'].create({
    'type_service': 'Service Commercial',
    'structure_id': commerce.id,
})

print(f"✓ 3 structures et 4 services créés")

# ============================================
# 3. PERSONNES
# ============================================

print("Création des personnes...")

# Intervenants / Tuteurs école
tuteur_ecole_1 = env['res.partner'].create({
    'name': 'Martin Sophie',
    'email': 'sophie.martin@limayrac.fr',
    'phone': '0561111111',
    'is_intervenant': True,
    'poste': 'Formatrice Informatique',
})

tuteur_ecole_2 = env['res.partner'].create({
    'name': 'Bernard Thomas',
    'email': 'thomas.bernard@limayrac.fr',
    'phone': '0561222222',
    'is_intervenant': True,
    'poste': 'Formateur Commerce',
})

# Responsables de formation
responsable_sio = env['res.partner'].create({
    'name': 'Durand Philippe',
    'email': 'philippe.durand@limayrac.fr',
    'phone': '0561333333',
    'poste': 'Responsable BTS SIO',
    'formation_responsable_id': formation_bts_sio.id,
})

responsable_sio_2 = env['res.partner'].create({
    'name': 'Rousseau Céline',
    'email': 'celine.rousseau@limayrac.fr',
    'phone': '0561444444',
    'poste': 'Co-responsable BTS SIO',
    'formation_responsable_id': formation_bts_sio.id,
})

responsable_ndrc = env['res.partner'].create({
    'name': 'Lambert Vincent',
    'email': 'vincent.lambert@limayrac.fr',
    'phone': '0561555555',
    'poste': 'Responsable BTS NDRC',
    'formation_responsable_id': formation_bts_ndrc.id,
})

responsable_bachelor = env['res.partner'].create({
    'name': 'Fontaine Isabelle',
    'email': 'isabelle.fontaine@limayrac.fr',
    'phone': '0561666666',
    'poste': 'Responsable Bachelor',
    'formation_responsable_id': formation_bachelor_dev.id,
})

# Tuteurs entreprise
tuteur_entreprise_1 = env['res.partner'].create({
    'name': 'Dubois Michel',
    'email': 'michel.dubois@techcorp.fr',
    'phone': '0661111111',
    'is_tuteur': True,
    'poste': 'Chef de projet',
    'service_id': service_techcorp_dev.id,
})

tuteur_entreprise_2 = env['res.partner'].create({
    'name': 'Leroy Claire',
    'email': 'claire.leroy@digitalpartners.fr',
    'phone': '0662222222',
    'is_tuteur': True,
    'poste': 'Responsable technique',
    'service_id': service_digital_web.id,
})

tuteur_entreprise_3 = env['res.partner'].create({
    'name': 'Petit Pierre',
    'email': 'pierre.petit@commerceplus.fr',
    'phone': '0663333333',
    'is_tuteur': True,
    'poste': 'Directeur commercial',
    'service_id': service_commerce_vente.id,
})

# Candidats
candidat_1 = env['res.partner'].create({
    'name': 'Dupont Jean',
    'email': 'jean.dupont@example.com',
    'phone': '0601020304',
    'is_candidat': True,
    'street': '12 Rue des Étudiants',
    'zip': '31000',
    'city': 'Toulouse',
})

candidat_2 = env['res.partner'].create({
    'name': 'Moreau Julie',
    'email': 'julie.moreau@example.com',
    'phone': '0602030405',
    'is_candidat': True,
    'street': '8 Avenue des Lycées',
    'zip': '31200',
    'city': 'Toulouse',
})

candidat_3 = env['res.partner'].create({
    'name': 'Renard Lucas',
    'email': 'lucas.renard@example.com',
    'phone': '0603040506',
    'is_candidat': True,
    'street': '25 Rue de la Formation',
    'zip': '31100',
    'city': 'Toulouse',
})

# Alumni
alumni_1 = env['res.partner'].create({
    'name': 'Garcia Marie',
    'email': 'marie.garcia@example.com',
    'phone': '0604050607',
    'is_alumni': True,
    'is_apprenant': False,
    'poste': 'Développeuse Full Stack',
})

print(f"✓ 13 personnes créées (2 intervenants, 4 responsables, 3 tuteurs, 3 candidats, 1 alumni)")

# ============================================
# 4. VOEUX
# ============================================

print("Création des vœux...")

voeux_1 = env['limayrac.voeux'].create({
    'apprenant_id': candidat_1.id,
    'formation_id': formation_bts_sio.id,
    'date_candidature': '2026-01-15',
    'state': 'accepte',
    'notes': 'Dossier complet, bon niveau en informatique',
})

voeux_2 = env['limayrac.voeux'].create({
    'apprenant_id': candidat_2.id,
    'formation_id': formation_bts_ndrc.id,
    'date_candidature': '2026-01-20',
    'state': 'en_cours',
    'notes': 'En attente d\'entretien',
})

voeux_3 = env['limayrac.voeux'].create({
    'apprenant_id': candidat_3.id,
    'formation_id': formation_bachelor_dev.id,
    'date_candidature': '2026-02-01',
    'state': 'nouveau',
})

print(f"✓ 3 vœux créés")

# ============================================
# 5. CURSUS
# ============================================

print("Création des cursus...")

cursus_1 = env['limayrac.cursus'].create({
    'apprenant_id': candidat_1.id,
    'formation_id': formation_bts_sio.id,
    'date_debut': '2026-09-01',
})

cursus_2 = env['limayrac.cursus'].create({
    'apprenant_id': alumni_1.id,
    'formation_id': formation_bts_sio.id,
    'date_debut': '2024-09-01',
    'date_fin': '2026-06-30',
    'is_diplome': True,
})

print(f"✓ 2 cursus créés")

# ============================================
# 6. CONTRATS
# ============================================

print("Création des contrats...")

contrat_1 = env['limayrac.contrat'].create({
    'type_contrat': 'apprentissage',
    'type_activite': 'Développement web',
    'date_debut': '2026-09-01',
    'date_fin': '2028-08-31',
    'apprenant_id': candidat_1.id,
    'cursus_id': cursus_1.id,
    'service_id': service_techcorp_dev.id,
    'tuteur_entreprise_id': tuteur_entreprise_1.id,
    'tuteur_ecole_id': tuteur_ecole_1.id,
    'notation': '4',
    'commentaire': 'Excellent potentiel, motivé',
})

contrat_2 = env['limayrac.contrat'].create({
    'type_contrat': 'apprentissage',
    'type_activite': 'Développement Full Stack',
    'date_debut': '2024-09-01',
    'date_fin': '2026-08-31',
    'apprenant_id': alumni_1.id,
    'cursus_id': cursus_2.id,
    'service_id': service_digital_web.id,
    'tuteur_entreprise_id': tuteur_entreprise_2.id,
    'tuteur_ecole_id': tuteur_ecole_1.id,
    'notation': '5',
    'commentaire': 'Excellent parcours, diplômée avec mention',
})

print(f"✓ 2 contrats créés")

# ============================================
# 7. BESOINS
# ============================================

print("Création des besoins...")

besoin_1 = env['limayrac.besoin'].create({
    'titre': 'Recherche alternant développeur Java',
    'description': 'Nous recherchons un alternant en BTS SIO pour rejoindre notre équipe de développement backend.',
    'date': '2026-02-15',
    'formation_id': formation_bts_sio.id,
    'structure_id': techcorp.id,
    'state': 'en_cours',
})

besoin_2 = env['limayrac.besoin'].create({
    'titre': 'Stage développeur mobile',
    'description': 'Stage de 3 mois dans le développement d\'applications mobiles React Native.',
    'date': '2026-02-20',
    'formation_id': formation_bachelor_dev.id,
    'structure_id': digital.id,
    'state': 'nouveau',
})

besoin_3 = env['limayrac.besoin'].create({
    'titre': 'Alternance commercial digital',
    'description': 'Recherche alternant BTS NDRC pour développer notre présence digitale.',
    'date': '2026-02-10',
    'formation_id': formation_bts_ndrc.id,
    'structure_id': commerce.id,
    'state': 'traite',
    'notes': 'Candidat trouvé et placé',
})

print(f"✓ 3 besoins créés")

# ============================================
# RÉSUMÉ
# ============================================

print("\n" + "="*50)
print("DONNÉES DE DÉMONSTRATION CRÉÉES AVEC SUCCÈS!")
print("="*50)
print("✓ 3 Formations (avec titres RNCP et responsables)")
print("✓ 3 Structures (avec 4 services)")
print("✓ 13 Personnes (intervenants, responsables, tuteurs, candidats, alumni)")
print(f"✓ 3 Vœux")
print(f"✓ 2 Cursus")
print(f"✓ 2 Contrats")
print(f"✓ 3 Besoins")
print("="*50)
print("\nVous pouvez maintenant explorer les modules Limayrac!")
print("\nMenus disponibles:")
print("- Limayrac → Contacts → Personnes / Structures / Services / Groupes")
print("- Limayrac → Formations → Formations / Titres RNCP / Besoins")
print("- Limayrac → Candidatures → Vœux / Cursus")
print("- Limayrac → Contrats → Contrats")
