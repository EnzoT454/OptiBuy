# Exemples publics épiceries.ca

Extraits des réponses récupérées pendant l’analyse du projet, conservés comme
fixtures pour des tests sans réseau. Source : https://epiceries.ca/api ;
documentation : https://epiceries.ca/developers.

- `categories.json` : liste des catégories.
- `rice-maxi.json` : page de recherche.
- `storeproduct-example.json` : sous-objet `product` de la résolution du code
  Maxi `20021564_EA`, enveloppé dans `{ok, data}` pour tester le détail.
- `detail-carrots-superc.json` : conflit réel entre le résumé à 1,98 $ et
  l’observation Super C à 3,99 $, plus ancienne.

Les dates internes appartiennent au fournisseur. Ces exemples ne constituent
ni un catalogue actuel, ni une preuve du prix en magasin. Les tests de cas
limites modifient une copie en mémoire et n’altèrent pas les fixtures.
