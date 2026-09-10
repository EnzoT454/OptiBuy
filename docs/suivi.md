---
title: Suivi du projet
---

<style>
    @media screen and (min-width: 76em) {
        .md-sidebar--primary {
            display: none !important;
        }
    }
</style>

# Suivi de projet

## 10 septembre 2026 — Mise à jour du cadrage

### Objectifs de la période

Intégrer le périmètre produit demandé dans la documentation, en conservant le parcours planification → liste, les quatre cas initiaux et la référence Figma. Aucune implémentation ni installation de dépendance n’était demandée.

### Travail réalisé

- Lecture du README, des pages documentaires et des cinq documents locaux de `tools/` ; constat de l’absence de backend/mobile/base implémentés.
- Cadrage des quatre modes d’ajout, comptes/profils, historique des plans et listes, trois usages IA, catalogue hors promotion, prix estimés et contributions après achat.
- Proposition de règles déterministes de compatibilité, conventions de prix, estimations, dates, révisions historiques et régénération conservant les choix manuels.
- Proposition des ajustements du modèle et des routes, avec distinction entre exigences produit acceptées et détails techniques à valider.
- Révision des 15 semaines : 300 h produit/tests/intégration, 45 h réunions/documentation, 45 h de marge et 60 h de finalisation, soit 450 h équipe.
- Remplacement des dates et réalisations fictives du template dans ce suivi et l’échéancier ; harmonisation de la capacité à 15 h par personne et par semaine.

### Décisions et limites

Les ajouts font partie du produit demandé, sans attester d’une validation académique. La solution d’authentification standard et les fournisseurs IA restent à choisir avant intégration ; les méthodes statistiques et contrats sont proposés, pas évalués. La référence Figma est conservée selon la demande, sans modification ni vérification visuelle des écrans dans cette révision.

Le périmètre présente un risque élevé de dépassement des 300 h produit disponibles. Des revues sont prévues en fin S2, S6 et S10. Import manuel, sources et formats délimités et méthodes simples sont les premiers compromis de profondeur à examiner ; toute réduction de fonctionnalités doit être convenue explicitement.

Les documents `tools/` sont présents localement mais ignorés par Git. Le site généré `site/` n’est pas modifié manuellement. Aucune fonctionnalité applicative ni aucun test fonctionnel n’a été réalisé lors de cette mise à jour documentaire.

### Vérification documentaire

Les liens locaux, les blocs de code et les totaux du planning ont été vérifiés dans les dix documents ; `git diff --check` ne signale pas d’erreur sur les fichiers suivis. Les anciennes formulations rendant comptes ou persistance optionnels ont été retirées. Zensical n’est pas installé dans l’environnement Python vérifié : la construction du site n’a pas été exécutée et aucune dépendance n’a été installée.

### Prochaines étapes

Réaliser le premier jalon mobile → `GET /health` → FastAPI avec chargement et erreur réseau, puis choisir l’authentification standard et l’accès PostgreSQL avant la persistance privée. Faire confirmer le cadrage académique si nécessaire et estimer les tâches à partir de ce premier jalon.
