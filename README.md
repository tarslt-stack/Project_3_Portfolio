# Que coûte une maison à Ames, Iowa ?

J'ai voulu comprendre ce qui fait varier le prix d'une maison. Pour ça,j'ai pris un dataset Kaggle de 1 460 ventes immobilières et j'ai fait toute la chaîne d'analyse :
nettoyage avec Python,questions posées en SQL, et préparation des données pour Power BI.

## Ce que j'ai utilisé
Python (pandas, matplotlib, seaborn), SQL Server et Power BI.

##  Comment j'ai procédé
1. **J'ai d'abord regardé les données** : valeurs manquantes, distribution des prix, variables les plus liées au prix, différences entre quartiers.
2. **Je les ai nettoyées** : les trous sont comblés par la médiane (chiffres) ou « Inconnu » (texte). J'ai aussi créé trois colonnes utiles : la surface totale, l'âge de la maison et une tranche de prix (Budget, Moyen, Premium, Luxe).
3. **Je les ai envoyées dans SQL Server** pour pouvoir les interroger.
4. **J'ai posé 5 questions aux données** :
   - Quels sont les quartiers les plus chers ?
   - Comment les maisons se répartissent-elles par tranche de prix ?
   - Comment les ventes évoluent-elles d'une année à l'autre ?
   - La qualité de la maison influence-t-elle vraiment le prix ?
   - Quelles maisons offrent le prix le plus élevé par rapport à leur surface ?

##  Pour tester le projet
1. Installer les bibliothèques : `pip install pandas numpy matplotlib seaborn openpyxl sqlalchemy pyodbc`
2. Télécharger [train.csv sur Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) et le mettre dans le dossier `data/`
3. Lancer les scripts Python dans l'ordre, puis les requêtes SQL

