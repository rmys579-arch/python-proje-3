import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as stats

# ==============================
# 1. DATASET LOADING (Messy Downloaded Data)
# ==============================

# Example: downloaded CSV file with missing values and inconsistent data
df = pd.read_csv("dataset.csv")

print("Initial Dataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# ==============================
# 2. DATA CLEANING (Downloaded messy data +5)
# ==============================

# Drop duplicate rows
df = df.drop_duplicates()

# Handle missing values
# Numerical columns -> fill with median
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# Categorical columns -> fill with mode
categorical_columns = df.select_dtypes(include=["object"]).columns

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Fix negative values if they should not exist
for col in numeric_columns:
    df[col] = df[col].apply(lambda x: abs(x))

print("\nCleaned Dataset Info:")
print(df.info())

# ==============================
# 3. SIMPLE AGGREGATIONS (Baseline)
# ==============================

summary_stats = df[numeric_columns].agg(
    ["mean", "min", "max", "sum"]
)

print("\nSummary Statistics:")
print(summary_stats)

# ==============================
# 4. ADVANCED STATISTICAL ANALYSIS (+5)
# ==============================

advanced_stats = {}

for col in numeric_columns:
    advanced_stats[col] = {
        "mean": stats.mean(df[col]),
        "median": stats.median(df[col]),
        "std_dev": stats.stdev(df[col]),
        "Q1": df[col].quantile(0.25),
        "Q3": df[col].quantile(0.75),
        "IQR": df[col].quantile(0.75) - df[col].quantile(0.25)
    }

advanced_stats_df = pd.DataFrame(advanced_stats).T
print("\nAdvanced Statistical Analysis:")
print(advanced_stats_df)

# ==============================
# 5. ANOMALY DETECTION (Data Science +15)
# ==============================

anomalies = {}

for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    anomaly_rows = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    anomalies[col] = anomaly_rows.shape[0]

print("\nAnomaly Detection Results:")
for key, value in anomalies.items():
    print(f"{key}: {value} potential anomalies detected")

# ==============================
# 6. BASIC VISUALIZATION (Matplotlib baseline)
# ==============================

# Boxplot for anomaly visualization
plt.figure()
df[numeric_columns].boxplot()
plt.title("Boxplot for Numerical Features")
plt.xlabel("Features")
plt.ylabel("Values")
plt.tight_layout()
plt.show()

# ==============================
# 7. DATA EXPORT (For P2 & P3 compatibility)
# ==============================

df.to_csv("cleaned_dataset.csv", index=False)
advanced_stats_df.to_csv("advanced_statistics.csv")

print("\nAnalysis completed successfully.")
