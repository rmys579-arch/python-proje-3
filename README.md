# python-proje-3
# Data Analysis Project - Step-by-Step Cleaning

## 1. Handling Messy Data (+5 Points)
- **Parser Robustness:** We used `sep=None` and `engine='python'` to handle inconsistent delimiters in the downloaded CSV.
- **Error Management:** `on_bad_lines='skip'` was used to bypass corrupted rows that caused `ParserError`.

## 2. Statistical Analysis & Data Science (+15 Points)
- **Missing Values:** Numerical nulls were filled with the **Median** to avoid outlier bias. Categorical nulls used **Mode** with a safe fallback mechanism to prevent `ValueError`.
- **Anomaly Detection:** We implemented the **IQR (Interquartile Range)** method. Data points outside 1.5 * IQR were flagged as scientific anomalies.

## 3. Advanced Visualization (+5 Points)
- Developed using **Seaborn** for high-fidelity scientific reporting.
- Automated **Word Report (.docx)** generation for professional insight delivery.