import pandas as pd
from sqlalchemy import create_engine

# connexion SQL Server
engine = create_engine(
    "mssql+pyodbc://localhost\\SQLEXPRESS/immobilier?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

df = pd.read_csv(r"data\train_propre.csv")

# envoyer vers SQL Server
df.to_sql("maisons", engine, if_exists="replace", index=False)

print("Table créée avec succès")