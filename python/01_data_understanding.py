
import pandas as pd

# Dataset load karna
df = pd.read_csv("charging_stations.csv")

# Dataset ka size
print("Dataset Shape:")
print(df.shape)

# First 5 records
print("\nFirst 5 Records:")
print(df.head())

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
df.info()







# ==================================
# STEP 2: DATA QUALITY ANALYSIS
# ==================================

# 1. Missing values count
print("\n--- MISSING VALUES ---")
missing = df.isnull().sum()
print(missing)

# 2. Missing values percentage
print("\n--- MISSING VALUE PERCENTAGE ---")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage.round(2))

# 3. Duplicate records
print("\n--- DUPLICATE RECORDS ---")
print("Total Duplicates:", df.duplicated().sum())

# 4. Unique values in important columns
print("\n--- UNIQUE VALUES ---")

columns = ["operator", "state", "city", "network"]

for col in columns:
    print(col, ":", df[col].nunique())

# 5. Numeric column summary
print("\n--- NUMERIC DATA SUMMARY ---")
print(df.describe())
