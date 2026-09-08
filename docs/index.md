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
    **Auteur(s)**: Hamza Aqel (20111814), Nouh Harfouche ()<!-- Nom de chaque membre (matricule)  -->  
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

Notre objectif est de livrer une application fonctionnelle qui permet de :

- créer, consulter, modifier et supprimer des recettes avec leurs ingrédients et quantités ;
- saisir une recette en langage naturel, puis vérifier et corriger les ingrédients extraits par un modèle de langage avant de les enregistrer ;
- sélectionner plusieurs recettes pour la semaine et obtenir une liste d’achats regroupée par magasin, avec un coût estimé ;
- supprimer un article ou remplacer un produit proposé, puis mettre à jour les informations de la liste ;
- recevoir des suggestions de recettes en fonction des promotions disponibles.

Le parcours principal sera la sélection des recettes jusqu’à l’affichage de la liste d’achats. Par « optimisation », nous entendons chercher à réduire le coût des quantités réellement achetées tout en couvrant les besoins et en respectant les contraintes choisies. Nous ne visons pas nécessairement la meilleure solution mathématique possible. Si certains besoins ne sont pas couverts ou qu’aucune solution conforme n’est trouvée, l’application devra l’indiquer clairement.

### Cas d’utilisation

**Gérer ses recettes.** L’utilisateur conserve ses recettes dans une bibliothèque pour pouvoir les retrouver et les réutiliser lors de futures planifications.

**Créer une recette avec une aide à la saisie.** L’utilisateur écrit, par exemple, « curry de poulet : 500 g de poulet, 400 g de riz et deux oignons ». L’application propose une liste structurée d’ingrédients. L’utilisateur peut la modifier, ajouter ou supprimer des éléments, puis confirmer la sauvegarde. Aucun enregistrement n’est effectué automatiquement à partir du résultat du modèle.

**Planifier les courses.** L’utilisateur choisit les recettes de la semaine. Si deux recettes demandent respectivement deux oignons et un oignon, l’application regroupe ce besoin en trois oignons. Elle compare ensuite les besoins aux produits disponibles et propose une liste par magasin selon les contraintes choisies. L’utilisateur peut ensuite modifier cette liste.

**Trouver des idées de repas.** L’utilisateur consulte des suggestions liées aux promotions. Par exemple, des offres sur le poulet, les poivrons et le riz peuvent orienter les recommandations vers des recettes utilisant ces ingrédients. Une méthode simple de classement sera suffisante pour la première version.

### Architecture et technologies

L’application sera organisée autour d’une interface mobile, d’un backend et d’une base de données.

| Élément | Technologie | Rôle |
|---|---|---|
| Application mobile | React Native, TypeScript et Expo | Afficher les écrans et gérer les interactions sur iOS et Android avec une base de code commune |
| Backend | Python et FastAPI | Fournir l’API et traiter les recettes, les promotions, les contraintes et les listes d’achats |
| Validation | Pydantic | Vérifier la structure des données échangées avec le backend |
| Base de données | PostgreSQL | Conserver les recettes et les autres données nécessaires à l’application |
| Modèle de langage | Fournisseur à sélectionner | Transformer une recette écrite en langage naturel en données structurées |
| Versionnement | Git et GitHub | Suivre les modifications et faciliter le travail en équipe |
| Documentation | Zensical | Présenter le projet et documenter son avancement |

Le mobile communiquera avec FastAPI par une API HTTP utilisant des données JSON. Seul le backend accédera à PostgreSQL et au fournisseur du modèle de langage. Les clés API resteront côté serveur. Les conversions d’unités connues et les calculs de quantités et de prix seront réalisés par le backend, sans dépendre du modèle de langage.

### Méthodologie

Nous développerons le projet progressivement sur environ 15 semaines, à raison d’environ 20 heures par semaine par personne. Nous commencerons par connecter l’application mobile à un backend minimal, puis nous ajouterons la gestion des recettes, la saisie assistée, les promotions et la génération des listes. Les recommandations viendront compléter ce parcours.

Les tâches pourront être réparties entre les deux membres lorsque les modules sont indépendants. Par exemple, la préparation des données de promotions pourra avancer en parallèle de l’intégration du modèle de langage. Nous intégrerons régulièrement les différentes parties et ajouterons des tests au fur et à mesure. Une partie du temps sera réservée à la documentation, aux corrections et à la préparation de la démonstration.

Avant de choisir le fournisseur LLM, nous comparerons plusieurs options sur un petit ensemble commun de recettes. Nous vérifierons les ingrédients extraits, les quantités, les unités, le format des réponses, le temps de réponse et le coût des appels.

Nous examinerons aussi les sources de promotions et leur disponibilité pour la période visée. Un jeu de données de secours sera prévu pour permettre les tests et la démonstration si la collecte automatique n’est pas fiable. Les correspondances entre ingrédients et produits seront développées à partir de cas simples, puis étendues aux formats et aux situations pris en charge.

### Validation et Évaluation

Nous évaluerons l’application à partir de scénarios d’utilisation complets : créer une recette, la retrouver, la modifier, sélectionner les repas d’une semaine, générer une liste et changer un article. Ces parcours seront vérifiés sur iOS et Android, avec une attention aux messages d’erreur et à la clarté des résultats.

Les tests automatisés porteront principalement sur la validation des recettes, la sauvegarde après confirmation, l’agrégation des ingrédients, les conversions d’unités compatibles, les prix et le respect des contraintes. Nous vérifierons aussi les cas où un produit est introuvable, où le budget ne permet pas de couvrir les besoins et où une modification rend la liste incomplète.

Pour évaluer la génération des listes, nous utiliserons de petits jeux de données dont les résultats peuvent être vérifiés manuellement. Nous comparerons le coût et la couverture des besoins à une méthode de référence simple. Cela permettra de vérifier l’utilité de la solution sans affirmer qu’elle fournit toujours un optimum global.

Pour le parsing des recettes, nous mesurerons les réponses structurées valides ainsi que les erreurs ou omissions d’ingrédients, de quantités et d’unités. Les tests courants utiliseront des réponses simulées afin de ne pas dépendre d’appels payants. Enfin, la démonstration finale devra montrer le parcours principal de bout en bout, en précisant les fonctionnalités réalisées et les limites restantes.

## Échéancier

!!! info
    Le suivi complet est disponible dans la page [Suivi de projet](suivi.md).

| Activités                      | Début   |   Fin   | Livrable                            | Statut      |
|--------------------------------|---------|---------|-------------------------------------|-------------|
| Ouverture de projet            | 4 mai   | 15 mai  | Proposition de projet               | ✅ Terminé  |
| Études préliminaires           | 4 mai   | 22 mai  | Document d'analyse                  | 🔄 En cours |
| Présentation + Rapport         | 7 aout  | 14 aout | Présentation + Rapport              | ⏳ À venir  |
