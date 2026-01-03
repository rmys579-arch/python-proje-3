# Data Analysis & Automated Scientific Reporting

## 1. Project Objective (Projenin Amacı)
The primary objective of this project is to transform raw, "messy" data into a structured, clean dataset and generate professional insights through automated reporting. This project demonstrates a full data science pipeline, including:
- **Data Integrity:** Cleaning and preprocessing inconsistent real-world data.
- **Statistical Depth:** Identifying anomalies and performing advanced descriptive statistics.
- **Automated Communication:** Converting complex analytical results into a readable and visual Word report (.docx) for decision-makers.

## 2. Technical Requirements
- **Python 3.12+**
- **Libraries:** `pandas`, `seaborn`, `matplotlib`, `python-docx`, `numpy`

## 3. Data Cleaning Process (Step-by-Step)
According to the criteria for "Messy Data," we implemented the following pipeline:

### Step 1: Robust Data Loading
- Handled inconsistent CSV delimiters using `sep=None`.
- Bypassed corrupted rows with `on_bad_lines='skip'` to ensure the script does not crash during execution.

### Step 2: Handling Missing Values
- **Numerical Data:** Null values were filled using the **Median** to prevent bias from extreme outliers.
- **Categorical Data:** Null values were filled using the **Mode**. A fallback mechanism was implemented to assign "Unknown" if no mode could be calculated, resolving potential `ValueError` issues.

### Step 3: Anomaly Detection
- We utilized the **Interquartile Range (IQR)** method. 
- Data points falling below `Q1 - 1.5*IQR` or above `Q3 + 1.5*IQR` were flagged as scientific anomalies for further investigation.

### Step 4: Data Transformation
- Duplicates were removed to ensure statistical independence.
- Scientific absolute value conversions were applied to ensure logical consistency in numerical features.

## 4. Visualization & Reporting
- **Seaborn Implementation:** Used for high-fidelity charts including Violin plots (distribution), Heatmaps (correlation), and Boxen plots (advanced outliers).
- **Automated Report:** A Python script automatically embeds these charts into a `Final_Project_Report.docx` file with professional "Insights" (interpretations) written for each visual.

## 5. How to Run
1. Ensure `dataset.csv` is in the root folder.
2. Run `python analysis.py` to clean and analyze data.
3. Run `python Visualization_and_report.py` to generate the final Word report.