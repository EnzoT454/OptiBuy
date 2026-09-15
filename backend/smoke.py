"""Essai explicite de trois appels réels, sans importer ni sauvegarder de prix."""
from fastapi.testclient import TestClient

from backend.app.main import create_app


def main() -> None:
    with TestClient(create_app(enabled=True)) as api:
        categories = api.get('/sources/epiceries/categories')
        categories.raise_for_status()
        print('Catégories :', categories.json()['data']['count'])
        search = api.get('/sources/epiceries/search', params={'q': 'riz', 'limit': 1})
        search.raise_for_status()
        results = search.json()['data']['results']
        if not results:
            raise RuntimeError('Recherche vide : choisir un autre terme avant de valider le parcours.')
        product = api.get('/sources/epiceries/products/' + results[0]['id'])
        product.raise_for_status()
        offers = product.json()['offers']
        if not offers:
            raise RuntimeError('Détail sans observation : normalisation non vérifiée en direct.')
        print('Produit :', results[0]['id'], '— observations :', len(offers))
        print('Avertissements :', offers[0]['quality']['warnings'])
        print('Parcours réel réussi ; exactitude des prix en magasin non vérifiée.')


if __name__ == '__main__':
    main()
