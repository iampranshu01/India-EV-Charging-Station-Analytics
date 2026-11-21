
import pandas as pd
from pathlib import Path

# Project folders
data_folder = Path(__file__).resolve().parent
project_folder = data_folder.parent

# Load original dataset
df = pd.read_csv(data_folder / "charging_stations.csv")

print("Original Shape:", df.shape)

# 1. Remove exact duplicate records
df = df.drop_duplicates()

print("After Removing Duplicates:", df.shape)

# 2. Remove columns that are completely empty
empty_columns = df.columns[df.isnull().all()].tolist()

print("Completely Empty Columns:", empty_columns)

df = df.drop(columns=empty_columns)

print("After Removing Empty Columns:", df.shape)

# 3. Save cleaned dataset
output_folder = project_folder / "output"
output_folder.mkdir(exist_ok=True)

output_path = output_folder / "charging_stations_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned Dataset Saved Successfully!")
print("Final Shape:", df.shape)
print("Saved At:", output_path)




# 4. Check missing values after cleaning

print("\nMissing Values After Cleaning:")

missing_values = df.isnull().sum()

missing_percentage = (missing_values / len(df)) * 100

missing_report = pd.DataFrame({
    "Missing Values": missing_values,
    "Missing Percentage": missing_percentage.round(2)
})

missing_report = missing_report.sort_values(
    by="Missing Percentage",
    ascending=False
)

print(missing_report)




# 5. Remove phone column due to excessive missing values

df = df.drop(columns=["phone"])

print("\nPhone Column Removed Successfully!")
print("Updated Dataset Shape:", df.shape)

# 6. Save final cleaned dataset

df.to_csv(output_path, index=False)

print("\nFinal Cleaned Dataset Saved!")





# 7. Check invalid and suspicious values

print("\n--- DATA QUALITY CHECK ---")

# Check missing latitude and longitude
print("Missing Latitude:", df["lat"].isnull().sum())
print("Missing Longitude:", df["lng"].isnull().sum())

# Check latitude and longitude ranges
print("\nLatitude Range:")
print(df["lat"].min(), "to", df["lat"].max())

print("\nLongitude Range:")
print(df["lng"].min(), "to", df["lng"].max())

# Check negative power values
print("\nNegative Power Values:")
print((df["max_power_kw"] < 0).sum())

# Check zero power values
print("\nZero Power Values:")
print((df["max_power_kw"] == 0).sum())

# Check negative charging points
print("\nNegative Charging Points:")
print((df[["ac_points", "dc_points", "n_points"]] < 0).sum())