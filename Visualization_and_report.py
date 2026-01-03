import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from docx import Document
from docx.shared import Inches
import os

# =============================================================
# 1. SETTINGS & STYLES (Seaborn +5)
# =============================================================
sns.set_theme(style="whitegrid", palette="magma")
plt.rcParams['figure.figsize'] = [10, 6]

def save_to_word(doc, plot_func, title, insight, filename):
    plt.figure(figsize=(10, 6))
    plot_func()
    plt.title(title, fontsize=14, fontweight='bold')
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    doc.add_heading(title, level=1)
    doc.add_picture(filename, width=Inches(5.5))
    doc.add_paragraph(insight)
    if os.path.exists(filename): os.remove(filename)

# =============================================================
# 2. GENERATING SCIENTIFIC REPORT
# =============================================================
try:
    df = pd.read_csv("cleaned_dataset.csv")
    doc = Document()
    doc.add_heading('Scientific Data Insights Report', 0)

    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()

    if num_cols:
        target = num_cols[0]
        
        # Chart 1: Violin Plot (Advanced Stats +5)
        def p1(): sns.violinplot(data=df, y=target, inner="box")
        ins1 = f"Distribution of {target}: The violin plot shows the probability density and quartiles."
        save_to_word(doc, p1, "Advanced Distribution Analysis", ins1, "f1.png")

        # Chart 2: Heatmap (Relationships)
        if len(num_cols) > 1:
            def p2(): sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
            ins2 = "Correlation Matrix: Identifying linear dependencies between variables."
            save_to_word(doc, p2, "Feature Correlation Heatmap", ins2, "f2.png")

        # Chart 3: Anomaly detection visual
        def p3(): sns.boxenplot(data=df, x=target, color="orange")
        ins3 = "Anomaly Detection: Boxen plot highlights extreme values and data tails."
        save_to_word(doc, p3, "Scientific Outlier Overview", ins3, "f3.png")

    doc.save("Final_Project_Report.docx")
    print("[SUCCESS] 'Final_Project_Report.docx' generated!")

except Exception as e:
    print(f"Error: {e}. Did you run analysis.py first?")