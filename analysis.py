import pandas as pd
import numpy as np
import statistics as stats

# =============================================================
# 1. DATASET LOADING (Handling Messy Data +5)
# =============================================================
try:
    # sep=None and engine='python' automatically detects commas or semicolons
    df = pd.read_csv("dataset.csv", sep=None, engine='python', on_bad_lines='skip')
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading CSV: {e}")
    exit()

# =============================================================
# 2. DATA CLEANING (Robust Cleaning)
# =============================================================
df = df.drop_duplicates()

# Categorical columns imputation
cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    mode_val = df[col].mode()
    df[col] = df[col].fillna(mode_val[0] if not mode_val.empty else "Unknown")

# Numerical columns imputation
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())
    df[col] = df[col].abs() # Ensure positive values where needed

# =============================================================
# 3. DATA SCIENCE & ANOMALY DETECTION (+15)
# =============================================================
advanced_stats = {}
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    advanced_stats[col] = {
        "Mean": df[col].mean(),
        "Median": df[col].median(),
        "Std_Dev": df[col].std(),
        "IQR": IQR,
        "Anomalies": df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))].shape[0]
    }

advanced_stats_df = pd.DataFrame(advanced_stats).T

# =============================================================
# 4. EXPORT FOR PERSON 2
# =============================================================
df.to_csv("cleaned_dataset.csv", index=False)
advanced_stats_df.to_csv("advanced_statistics.csv")
print("Analysis completed. 'cleaned_dataset.csv' created.")