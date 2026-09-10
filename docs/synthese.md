---
title: Synthèse
---

<style>
    @media screen and (min-width: 76em) {
        .md-sidebar--primary {
            display: none !important;
        }
    }
</style>


# Synthèse

État documentaire au **10 septembre 2026**. Cette page distingue les choix de cadrage des réalisations ; elle sera complétée avec les résultats effectifs et ne remplace pas le rapport final.

## 1. Études préliminaires

Le besoin central est de passer de recettes et repas hebdomadaires à une liste d’achats modifiable par magasin, sous contraintes. Le cadrage a été élargi aux comptes, aux quatre modes d’ajout, à l’historique, aux circulaires structurées et aux prix hors promotion avec contributions facultatives.

L’architecture cible conserve React Native/TypeScript/Expo, FastAPI/Pydantic et PostgreSQL. Trois responsabilités IA sont séparées : génération de recettes, extraction de recettes fournies et extraction de circulaires. La confirmation utilisateur précède toute sauvegarde de recette générée ou analysée ; les calculs restent déterministes côté backend.

Les principaux risques identifiés sont la correspondance ingrédients/produits/formats, la disponibilité et la qualité des offres, l’incertitude des prix, l’isolation des comptes et la stabilité historique. Des règles et contrats sont proposés dans le cadrage local, mais aucune comparaison de fournisseurs, calibration statistique ou étude utilisateur n’est encore rapportée comme réalisée.

## 2. Réalisation

Le dépôt contient le site documentaire Zensical et les documents de cadrage. La révision du 10 septembre harmonise objectifs, architecture, contrats candidats, décisions, tâches et suivi. La référence Figma et les cinq onglets sont conservés dans les exigences ; aucun écran n’est implémenté par cette révision.

Le backend, le mobile, PostgreSQL, l’authentification et les intégrations IA restent à développer. Le premier jalon prévu est mobile → `GET /health` → FastAPI.

## 3. Évaluation

Aucun résultat de test applicatif ou gain économique mesuré n’est disponible. La validation future couvrira les parcours iOS/Android, l’isolation entre comptes, la confirmation avant sauvegarde, les erreurs IA, les dates et doublons de circulaires, les conversions et formats, les estimations/contributions, la couverture et les contraintes, le recalcul et la conservation de l’historique.

Les paniers seront comparés sur des cas contrôlés à une référence vérifiable manuellement. La compatibilité distinguera présence d’un ingrédient et quantité suffisante. Les estimations conserveront provenance et fourchette sans garantir stock ou budget. Les tests courants utiliseront des réponses IA simulées et un catalogue de secours identifié.

## 4. Bilan provisoire

Le cadrage demandé est documenté ; la réalisation du produit reste à faire. Les 450 h théoriques comprennent 300 h produit/tests/intégration, 45 h réunions/documentation, 45 h de marge et 60 h de finalisation protégée. La charge est élevée et devra être réestimée aux jalons, sans reclasser les ajouts en bonus.

Restent notamment à choisir la solution standard d’authentification, les fournisseurs IA, les sources du catalogue/circulaires/recettes et les conventions techniques détaillées. Les règles proposées de prix, historique et optimisation doivent être validées avant codage. Une validation académique éventuelle du périmètre élargi reste distincte de la demande produit.
