import pandas as pd
from pathlib import Path

# Project paths
project_folder = Path(__file__).resolve().parent.parent
data_path = project_folder / "output" / "charging_stations_cleaned.csv"

# Load cleaned dataset
df = pd.read_csv(data_path)

print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

# 1. Top 10 states by charging stations
top_states = df["state"].value_counts().head(10)

print("\nTop 10 States by Charging Stations:")
print(top_states)

# 2. Top 10 operators
top_operators = df["operator"].value_counts().head(10)

print("\nTop 10 Charging Station Operators:")
print(top_operators)

# 3. Top 10 cities
top_cities = df["city"].value_counts().head(10)

print("\nTop 10 Cities by Charging Stations:")
print(top_cities)



# 4. AC vs DC Charging Analysis

print("\n--- AC VS DC ANALYSIS ---")

total_ac = df["ac_points"].sum()
total_dc = df["dc_points"].sum()

print("Total AC Points:", total_ac)
print("Total DC Points:", total_dc)

# 5. Charging Power Analysis

print("\n--- CHARGING POWER ANALYSIS ---")

print("Average Power (kW):", round(df["max_power_kw"].mean(), 2))
print("Median Power (kW):", df["max_power_kw"].median())
print("Maximum Power (kW):", df["max_power_kw"].max())
print("Minimum Power (kW):", df["max_power_kw"].min())

# 6. Charging Points Summary

print("\n--- CHARGING POINTS SUMMARY ---")

print(df[["ac_points", "dc_points", "n_points"]].describe())








import matplotlib.pyplot as plt

# Create charts folder
charts_folder = project_folder / "output" / "charts"
charts_folder.mkdir(parents=True, exist_ok=True)

# Chart 1: AC vs DC
plt.figure(figsize=(8, 5))

plt.bar(
    ["AC Points", "DC Points"],
    [total_ac, total_dc]
)

plt.title("AC vs DC Charging Points")
plt.xlabel("Charging Type")
plt.ylabel("Total Points")
plt.tight_layout()

plt.savefig(charts_folder / "ac_vs_dc.png")
plt.show()


# Chart 2: Charging Power Distribution
plt.figure(figsize=(8, 5))

plt.hist(
    df["max_power_kw"].dropna(),
    bins=30,
    edgecolor="black"
)

plt.title("Charging Power Distribution")
plt.xlabel("Maximum Power (kW)")
plt.ylabel("Number of Stations")
plt.tight_layout()

plt.savefig(charts_folder / "charging_power_distribution.png")
plt.show()

print("Charts saved successfully!")






# Chart 3: Top 10 States by Charging Stations

top_states = df["state"].value_counts().head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_states.index, top_states.values)

plt.title("Top 10 States by EV Charging Stations")
plt.xlabel("State")
plt.ylabel("Number of Station Records")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(charts_folder / "top_10_states.png")
plt.show()

print("Top 10 States chart saved successfully!")





# Chart 4: Top 10 Charging Operators

top_operators = df["operator"].value_counts().head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_operators.index, top_operators.values)

plt.title("Top 10 EV Charging Operators in India")
plt.xlabel("Charging Operator")
plt.ylabel("Number of Station Records")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(charts_folder / "top_10_operators.png")
plt.show()

print("Top 10 Operators chart saved successfully!")



# Chart 5: Top 10 Cities

top_cities = df["city"].value_counts().head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_cities.index, top_cities.values)

plt.title("Top 10 Cities by EV Charging Stations")
plt.xlabel("City")
plt.ylabel("Number of Station Records")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(charts_folder / "top_10_cities.png")
plt.show()

print("Top 10 Cities chart saved successfully!")


# Chart 6: State-wise AC vs DC Charging Points

state_charging = df.groupby("state")[["ac_points", "dc_points"]].sum()

top_10_states = state_charging.sum(axis=1).sort_values(
    ascending=False
).head(10).index

state_charging = state_charging.loc[top_10_states]

state_charging.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("State-wise AC vs DC Charging Points")
plt.xlabel("State")
plt.ylabel("Total Charging Points")

plt.xticks(rotation=45, ha="right")
plt.legend(["AC Points", "DC Points"])

plt.tight_layout()

plt.savefig(charts_folder / "state_wise_ac_vs_dc.png")
plt.show()

print("State-wise AC vs DC chart saved successfully!")



# Chart 7: Top 10 States - Horizontal Bar Chart

top_10_states = df["state"].value_counts().head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_10_states.index[::-1],
    top_10_states.values[::-1]
)

plt.title("Top 10 States by EV Charging Station Records")
plt.xlabel("Number of Station Records")
plt.ylabel("State")

plt.tight_layout()

plt.savefig(charts_folder / "top_10_states_horizontal.png")
plt.show()

print("Horizontal bar chart saved successfully!")




# Analysis 8: Missing Values Analysis

# Step 1: Calculate missing values percentage
missing_percent = df.isnull().mean() * 100

# Step 2: Keep only columns having missing values
missing_percent = missing_percent[
    missing_percent > 0
]

# Step 3: Sort missing values
missing_percent = missing_percent.sort_values(
    ascending=False
)

# Step 4: Print missing values report
print("\nMissing Values Percentage:")
print(missing_percent.round(2))

# Step 5: Create chart
plt.figure(figsize=(10, 7))

plt.barh(
    missing_percent.index[::-1],
    missing_percent.values[::-1]
)

plt.title("Missing Values Percentage by Column")
plt.xlabel("Missing Values (%)")
plt.ylabel("Columns")

plt.tight_layout()

# Step 6: Save chart
plt.savefig(
    charts_folder / "missing_values_analysis.png"
)

plt.show()

print("Missing Values Analysis Completed!")




# Analysis 9: Outlier Analysis

# Step 1: Select power column and remove missing values
power_data = df["max_power_kw"].dropna()

# Step 2: Calculate Q1 and Q3
Q1 = power_data.quantile(0.25)
Q3 = power_data.quantile(0.75)

# Step 3: Calculate IQR
IQR = Q3 - Q1

# Step 4: Calculate outlier limits
lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

# Step 5: Identify potential outliers
outliers = power_data[
    (power_data < lower_limit) |
    (power_data > upper_limit)
]

# Step 6: Print results
print("\nOUTLIER ANALYSIS")
print("Q1:", round(Q1, 2))
print("Q3:", round(Q3, 2))
print("IQR:", round(IQR, 2))
print("Lower Limit:", round(lower_limit, 2))
print("Upper Limit:", round(upper_limit, 2))
print("Total Outliers:", len(outliers))
print("Outlier Percentage:", round(
    (len(outliers) / len(power_data)) * 100, 2
), "%")

# Step 7: Create boxplot
plt.figure(figsize=(9, 5))

plt.boxplot(power_data)

plt.title("Outlier Analysis - Charging Power")
plt.ylabel("Maximum Power (kW)")

plt.tight_layout()

plt.savefig(charts_folder / "outlier_analysis.png")
plt.show()

print("Outlier Analysis Completed!")






# Analysis 10: Correlation Analysis

# Step 1: Select numerical columns
numeric_data = df[
    ["max_power_kw", "ac_points", "dc_points", "n_points"]
]

# Step 2: Calculate correlation
correlation_matrix = numeric_data.corr()

# Step 3: Print correlation values
print("\nCORRELATION MATRIX:")
print(correlation_matrix.round(2))

# Step 4: Create correlation heatmap
plt.figure(figsize=(9, 6))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.colorbar(label="Correlation Coefficient")

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

# Step 5: Display values inside the chart
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        plt.text(
            j,
            i,
            round(correlation_matrix.iloc[i, j], 2),
            ha="center",
            va="center"
        )

plt.title("Correlation Analysis of EV Charging Data")

plt.tight_layout()

# Step 6: Save chart
plt.savefig(charts_folder / "correlation_analysis.png")
plt.show()

print("Correlation Analysis Completed!")










