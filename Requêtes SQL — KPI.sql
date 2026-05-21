---1_prix moyen par quartier
SELECT 
	Neighborhood AS quartier,
	ROUND(AVG(SalePrice),0) AS prix_moyen,
	COUNT(*) AS nb_ventes ,
	ROUND(MIN(SalePrice),0) AS prix_min,
	ROUND(MAX(SalePrice),0) AS prix_max
FROM maisons
GROUP BY Neighborhood
ORDER BY prix_moyen DESC


---2_Distribution par tranche de prix
SELECT 
	TranchesPrix,
	COUNT(*) AS nb_maisons,
	ROUND(AVG(SalePrice),0) AS prix_moyen,
	ROUND(AVG(TotalSF),0) AS surface_moyenne
FROM maisons
GROUP BY TranchesPrix
ORDER BY prix_moyen


---3_Évolution des ventes par année
SELECT 
	YrSold AS annee,
	COUNT(*) AS nb_ventes,
	ROUND(AVG(SalePrice),0) AS prix_moyen_annee
FROM maisons 
GROUP BY YrSold
ORDER BY YrSold


---4_Impact de la qualité sur le prix
SELECT
	OverallQual AS qualite, -- de 1 (mauvais) a 10 (excellent)
	COUNT(*) AS nb_maisons,
	ROUND(AVG(SalePrice),0) AS prix_moyen
FROM maisons
GROUP BY OverallQual
ORDER BY OverallQual DESC


--5_Top 10 maisons les mieux valorisées
SELECT
    TOP 10
	Id,
	Neighborhood,
	SalePrice,
	TotalSF,
	ROUND(SalePrice * 1.0 / TotalSF, 1) AS prix_par_m2
FROM maisons
ORDER BY prix_par_m2 DESC
