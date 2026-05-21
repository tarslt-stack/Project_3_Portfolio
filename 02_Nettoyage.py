
# Objectif : préparer un dataset propre pour SQL et Power BI.
# Résultat attendu : un fichier train_propre.csv avec ~12 colonnes et 1460 lignes, sans aucune valeur manquante

#1 Traiter les valeurs manquantes
import pandas as pd
import os 
os.makedirs('data',exist_ok=True)
df = pd.read_csv('C:\\Users\\Fatima\\Desktop\\Portfolio_project_3\\train.csv')
    # Colonnes numeriques : remplacer par la mediane
num_cols = df.select_dtypes(include='number').columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    # Colonnes texte : remplacer par 'Inconnu'
cat_cols = df.select_dtypes(include='object').columns
df[cat_cols] = df[cat_cols].fillna('Inconnu')
print('Manquants restants :', df.isnull().sum().sum())


#2 Créer des nouvelles colonnes utiles
    # Surface totale
df['TotalSF'] = df['GrLivArea'] + df['TotalBsmtSF']
    # Age de la maison au moment de la vente
df['Age'] = df['YrSold'] - df['YearBuilt']
    # Tranche de prix
df['TranchesPrix'] = pd.cut(
df['SalePrice'],
bins=[0, 100000, 200000, 300000, 999999],
labels=['Budget', 'Moyen', 'Premium', 'Luxe']
)


#3 Sélectionner les colonnes pour l'analyse
colonnes = [
'Id', 'Neighborhood', 'SalePrice', 'GrLivArea',
'TotalSF', 'Age', 'OverallQual', 'BedroomAbvGr',
'FullBath', 'GarageCars', 'YrSold', 'TranchesPrix'
]
df_propre = df[colonnes]
    # Export CSV propre
df_propre.to_csv('data/train_propre.csv', index=False)
print('Export termine :', df_propre.shape)
