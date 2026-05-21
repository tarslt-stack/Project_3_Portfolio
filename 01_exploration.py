# pip install pandas numpy matplotlib seaborn openpyxl

# 1 Chargement et aperçu
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from pkg_resources import Distribution
import seaborn as sns 
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv('.........') #path to csv fil "train.csv"

print('Dimensions :', df.shape) # (1460, 81)
print(df.head())
print(df.describe())


#2 Valeurs manquantes 
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)
print(missing)
plt.figure(figsize=(10, 5))
missing.plot(kind='bar', color='#7F77DD')
plt.title('Valeurs manquantes par colonne')
plt.tight_layout()
plt.savefig('outputs/missing_values.png')


#3 distribution du prix de vente
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
sns.histplot(df['SalePrice'], kde=True, color='#1D9E75')
plt.title('Distribution du prix')
plt.subplot(1, 2, 2)
sns.histplot(np.log1p(df['SalePrice']), kde=True, color='#BA7517')
plt.title('Distribution log(prix)')
plt.tight_layout()
plt.savefig('outputs/distribution_prix.png')

#4 Corrélation avec le prix 
corr = df.select_dtypes(include='number').corr()['SalePrice']
top10 = corr.abs().sort_values(ascending=False)[1:11]
top10.plot(kind='barh', color='#534AB7')
plt.title('Top 10 variables correlees au prix')
plt.tight_layout()
plt.savefig('outputs/correlations.png')

# 5 Prix par quartier
prix_quartier = df.groupby('Neighborhood')['SalePrice'] \
.mean().sort_values(ascending=False)
prix_quartier.plot(kind='bar', figsize=(12, 6), color='#1D9E75')
plt.title('Prix moyen par quartier')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('outputs/prix_quartier.png')
