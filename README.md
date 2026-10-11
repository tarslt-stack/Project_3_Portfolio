# 🏠 What Does a House Cost in Ames, Iowa?

I wanted to understand what makes house prices vary. To do that, I took a Kaggle dataset of 1,460 real estate sales and built the full analysis pipeline: data cleaning with Python, questions answered with SQL, and data prepared for Power BI.

## 🛠️ What I Used
Python (pandas, matplotlib, seaborn), SQL Server and Power BI.

## 🔄 How I Did It
1. **I started by exploring the data**: missing values, price distribution, variables most correlated with price, differences between neighborhoods.
2. **I cleaned it**: missing values are filled with the median (numeric) or "Inconnu" (text). I also created three useful columns: total area, house age, and a price tier (Budget, Moyen, Premium, Luxe).
3. **I loaded it into SQL Server** so I could query it.
4. **I asked the data 5 questions**:
   - Which neighborhoods are the most expensive?
   - How are houses distributed across price tiers?
   - How do sales evolve from one year to the next?
   - Does a house's quality really affect its price?
   - Which houses have the highest price relative to their size?

## 🚀 How to Run the Project
1. Install the libraries: `pip install pandas numpy matplotlib seaborn openpyxl sqlalchemy pyodbc`
2. Download [train.csv from Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) and put it in the `data/` folder
3. Run the Python scripts in order, then the SQL queries
