import pandas as pd

# Load your cleaned dataset
df = pd.read_csv("charging_stations_cleaned.csv")

print("Dataset Loaded:", df.shape)

# Create MySQL-ready dataset
mysql_df = df.copy()

mysql_df.to_csv(
    "charging_stations_mysql_ready.csv",
    index=False,
    na_rep="\\N",
    encoding="utf-8"
)

print("\nMySQL Ready CSV Created Successfully!")
print("Total Rows:", len(mysql_df))
print("Total Columns:", len(mysql_df.columns))
print("Total Missing Values:", mysql_df.isnull().sum().sum())