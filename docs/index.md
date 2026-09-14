---
title: Vue d'ensemble du projet
---

<style>
    @media screen and (min-width: 76em) {
        .md-sidebar--primary {
            display: none !important;
        }
    }
</style>

# Vue d'ensemble du projet

!!! info "Informations générales"
    **Session**: Automne 2026  
    **Auteur(s)**: Hamza Aqel (20111814), Nouh Harfouche (20262136)<!-- Nom de chaque membre (matricule)  -->  
    **Thème(s)**: Développement, innovation<!-- Thèmes principaux abordés dans le projet  -->  
    **Superviseur(s)**: Louis-Edouard Lafontant<!-- Nom du superviseur (affiliation)  -->  
    **Collaborateur(s):** <!-- Nom de(s) collaborateur(s) et partenaire(s)` -->  

## Description du projet

### Contexte

Préparer les repas de la semaine demande de choisir des recettes, de vérifier les ingrédients nécessaires et de faire une liste de courses. Pour respecter un budget, il faut aussi consulter les promotions et comparer les produits de plusieurs épiceries. Ces étapes demandent du temps, surtout lorsque les recettes et les offres se trouvent à des endroits différents.

Le projet OptiBuy part de ce besoin : faciliter le passage des repas que l’on souhaite cuisiner aux produits que l’on doit acheter. Il s’inscrit dans le développement d’une application mobile utilisable sur iOS et Android.

### Problématique

Comment préparer une liste d’achats qui couvre les ingrédients de plusieurs recettes tout en respectant un budget et des contraintes de déplacement ? Une simple liste ne permet pas de comparer les prix, tandis qu’une promotion ne précise pas si le produit correspond aux besoins d’une recette.

Il faut notamment regrouper les quantités, tenir compte des formats vendus et choisir les magasins à visiter. Le produit le moins cher n’est pas toujours le meilleur choix s’il oblige à se déplacer dans une épicerie supplémentaire. Les offres disponibles peuvent aussi ne pas couvrir tous les ingrédients ou ne pas être encore publiées pour la semaine souhaitée.

### Proposition et objectifs

Nous proposons **OptiBuy**, une application mobile qui utilise les recettes de l’utilisateur et les promotions des épiceries pour préparer une liste d’achats par magasin. L’utilisateur pourra choisir ses repas et préciser ses contraintes, comme son budget, le nombre maximal de magasins, les magasins préférés ou exclus et le rayon géographique.

Le périmètre demandé le **10 septembre 2026** conserve tous les cas initiaux et ajoute comptes/profils, découverte assistée, historique, catalogue hors promotion, estimations et contributions après achat. Ces fonctions font partie du produit demandé ; la validation académique éventuelle reste distincte. Le dépôt contient actuellement la documentation, sans application ni backend implémentés.

### Cas d’utilisation

**Gérer et découvrir des recettes.** Créer, consulter, modifier, supprimer, rechercher et marquer des recettes comme favorites. Quatre façons d’ajouter une recette sont prévues :

- **Saisir manuellement** : renseigner ingrédients, quantités, portions et préparation.
- **Trouver une idée** : décrire son envie, choisir parmi plusieurs plats proposés par l’IA, puis modifier la recette complète obtenue.
- **Cuisiner avec ce que j’ai** : fournir ses ingrédients et éventuellement leurs quantités ; voir les ingrédients présents, manquants et les quantités non vérifiables. Le backend calcule la compatibilité à partir des seules déclarations ; la présence ne prouve pas une quantité suffisante.
- **Importer un texte** : extraire une recette existante en données structurées, puis corriger, ajouter ou supprimer des ingrédients.

L’analyse et la génération ne sauvegardent jamais automatiquement une recette. Une confirmation explicite est nécessaire. Les comptes et profils permettent de conserver des données privées et des préférences ; les autorisations seront contrôlées côté serveur.

**Planifier les courses.** Sauvegarder une semaine, ses repas et portions, consulter les semaines passées et générer une liste modifiable par magasin. L’application regroupe les besoins, tient compte des formats réellement achetés et applique budget, nombre de magasins, préférences/exclusions, rayon, alimentation, produits et formats. Cocher, supprimer ou remplacer un article reste possible ; le backend recalcule prix, couverture et contraintes. La régénération doit conserver les choix manuels ou signaler un conflit, sans les annuler silencieusement.

Les plans et listes conserveront des instantanés des recettes, portions et prix retenus. Modifier ensuite une recette ou un prix ne changera pas les résultats historiques.

**Découvrir des repas économiques.** Conserver [la référence Figma](https://www.figma.com/design/GZnafkmCJzWu1gyl6ZamgP), l’accueil, les cinq onglets **Accueil · Recettes · Calendrier · Promos · Paramètres**, l’organisation du calendrier et l’accès à la liste par magasin. Dans Recettes, placer **Toutes · Favoris · Rapides · Petit budget** en haut. Petit budget proposera des recettes selon les prix/promotions avec une justification compréhensible, sans économies chiffrées faute de référence valable. Français québécois, CAD, accent vert, sobriété et états vide/chargement/erreur seront conservés.

### Promotions, prix et incertitude

L’IA aura trois responsabilités séparées : générer des suggestions/recettes, extraire une recette fournie et extraire les informations de circulaires. Les circulaires passeront par une validation avant intégration, en conservant source, magasins, formats, prix, conditions et dates. Les valeurs illisibles ou ambiguës resteront signalées. Import manuel initial, traitement reproductible, détection des doublons et jeu de secours identifié sont prévus.

Distinguer période des repas, date prévue d’achat, validité des offres et publication/récupération des données. Le cycle visé est jeudi–mercredi ; une vérification mercredi soir peut être prévue, mais ne prouve pas que les offres futures sont publiées. Aucune offre expirée ne sera réutilisée silencieusement.

Le catalogue couvrira aussi les produits hors promotion. Distinguer prix commercial connu et sourcé, prix déclaré lors d’un achat, prix estimé avec fourchette/méthode/provenance et prix inconnu. Les références initiales seront documentées ; les observations comparables pourront alimenter une méthode statistique simple. Le LLM n’inventera pas de prix ; une estimation ne prouve pas le stock en magasin.

Après achat d’un article estimé, la question facultative « Quel prix avez-vous payé ? » permettra de déclarer produit, format, magasin, date, quantité, total et conditions. Taxes/consignes et prix unitaires seront distingués. Validation, doublons, valeurs aberrantes et vieillissement seront traités ; une déclaration seule ne remplacera pas une référence. Les estimations communes ne révéleront ni identité ni historique personnel.

Le parcours planification → liste reste prioritaire. L’optimisation cherchera à réduire le coût des quantités achetées sans garantie d’optimum global. Le résultat séparera couverture complète/partielle, contraintes respectées/non respectées/non vérifiables, prix connus/estimés/inconnus et disponibilité des promotions. Liste partielle, aucune solution trouvée et promotions indisponibles pourront se combiner. Avec des estimations, afficher une fourchette et l’incertitude sur le budget, sans le garantir à partir d’une moyenne. La comparaison proposée utilise la borne haute des paniers calculables après contrôle de couverture et de contraintes ; un prix inconnu ne vaut pas zéro.

### Architecture et technologies

L’application sera organisée autour d’une interface mobile, d’un backend et d’une base de données.

| Élément | Technologie | Rôle |
|---|---|---|
| Application mobile | React Native, TypeScript et Expo | Afficher les écrans et gérer les interactions sur iOS et Android avec une base de code commune |
| Backend | Python et FastAPI | Fournir l’API et traiter les recettes, les promotions, les contraintes et les listes d’achats |
| Validation | Pydantic | Vérifier la structure des données échangées avec le backend |
| Base de données | PostgreSQL | Conserver comptes, recettes, plans/historique, catalogue, prix et listes |
| Modèle de langage | Fournisseur à sélectionner | Générer des recettes et extraire recettes/circulaires, avec validation backend |
| Versionnement | Git et GitHub | Suivre les modifications et faciliter le travail en équipe |
| Documentation | Zensical | Présenter le projet et documenter son avancement |

Le mobile communiquera avec FastAPI par une API HTTP utilisant des données JSON. Seul le backend accédera à PostgreSQL et au fournisseur du modèle de langage. Les clés API resteront côté serveur. Les conversions d’unités connues et les calculs de quantités et de prix seront réalisés par le backend, sans dépendre du modèle de langage.

### Méthodologie

Le plan vise **15 semaines, deux étudiants à 15 h par semaine chacun, soit 450 h théoriques**. Il réserve 300 h au produit, tests et intégration, 45 h aux réunions/suivi/documentation, 45 h aux imprévus et 60 h à la finalisation protégée en semaines 14–15. Ces enveloppes ne garantissent pas que toutes les fonctionnalités tiennent dans la capacité ; l’extension représente un risque de charge élevé.

Le premier jalon demeure mobile → `GET /health` → FastAPI. Comptes et persistance précèdent les recettes privées et les plans ; catalogue et circulaires validées précèdent estimations et génération de listes. Les fournisseurs IA seront comparés sur les trois tâches avant sélection ; la solution standard d’authentification sera choisie et documentée avant intégration. Les algorithmes, schémas et routes restent des propositions jusqu’à validation technique.

Des revues de capacité sont prévues en fin de semaines 2, 6 et 10. Un import manuel, des sources/formats limités et documentés et des méthodes simples réduisent la profondeur technique sans supprimer les cas d’utilisation. Si cela ne suffit pas, une capacité supplémentaire ou un phasage doit être convenu explicitement, avec validation académique si nécessaire.

### Validation et Évaluation

Les tests prévus couvrent isolation entre utilisateurs, recettes sauvegardées seulement après confirmation, erreurs IA, compatibilité sans quantités, extraction et doublons de circulaires, dates des offres, conversions/formats, portions et couverture, estimations/contributions, recalcul et choix manuels, stabilité de l’historique. Les parcours seront vérifiés sur iOS et Android avec états vide/chargement/erreur.

De petits jeux contrôlés permettront de comparer les paniers à une référence calculable manuellement. Les tests courants simuleront les réponses IA ; la démonstration utilisera au besoin un jeu de secours identifié. Aucune évaluation fonctionnelle n’a encore été réalisée dans ce dépôt.

## Échéancier proposé

Les semaines sont relatives au démarrage effectif ; les anciennes dates d’exemple du template ne constituent pas un calendrier validé. Le [suivi](suivi.md) rapporte uniquement le travail effectivement réalisé.

| Période | Livrable prévu | Statut |
| --- | --- | --- |
| S1–2 | Mobile → /health, choix comptes/persistance et exploration des données | À développer |
| S3–4 | Comptes, recettes manuelles, recherche/favoris et calendrier sauvegardé | À développer |
| S5–6 | Modes IA de recettes avec confirmation | À développer |
| S7–8 | Catalogue, circulaires validées et données de secours | À développer |
| S9–10 | Estimations, contributions et première génération backend | À développer |
| S11–12 | Listes mobiles modifiables, régénération et historique | À développer |
| S13 | Petit budget et consolidation des parcours | À développer |
| S14–15 | Tests finaux, corrections, rapport et démonstration — 60 h protégées | À venir |
