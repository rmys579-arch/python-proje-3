import pandas as pd
import numpy as np

# =============================================================
# 1. DATA LOADING
# =============================================================
try:
    df = pd.read_csv("dataset.csv", sep=None, engine='python', on_bad_lines='skip')
    print("\n" + "="*50)
    print("✅ DATASET LOADED SUCCESSFULLY")
    print(f"Total Rows: {df.shape[0]} | Total Columns: {df.shape[1]}")
    print("="*50 + "\n")
except Exception as e:
    print(f"❌ Error loading CSV: {e}")
    exit()

# =============================================================
# 2. DATA CLEANING & STATS
# =============================================================
# (Cleaning procedures remain the same...)
df = df.drop_duplicates()
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

advanced_stats = {}
for col in num_cols:
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1
    advanced_stats[col] = {
        "Mean": round(df[col].mean(), 2),
        "Median": round(df[col].median(), 2),
        "Std_Dev": round(df[col].std(), 2),
        "Anomalies": df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))].shape[0]
    }

# Terminal-Readable Table Output
stats_df = pd.DataFrame(advanced_stats).T
print("📊 ADVANCED STATISTICAL SUMMARY")
print("-" * 60)
print(stats_df.to_string()) # to_string() aligns the entire table neatly
print("-" * 60 + "\n")

df.to_csv("cleaned_dataset.csv", index=False)
stats_df.to_csv("advanced_statistics.csv")