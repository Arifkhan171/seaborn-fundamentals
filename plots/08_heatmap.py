# Seaborn Heatmap - Visualize Matrix Data and Correlations
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# --- Basic Heatmap with Numeric Matrix ---
data = np.linspace(1, 10, 20).reshape(4, 5)
label_style = {"fontsize": 14, "color": "black"}

sns.heatmap(
    data,
    annot=True,
    annot_kws=label_style,
    linewidth=2,
    linecolor="white",
    cmap="Blues"
)

plt.title("Heatmap - Numeric Matrix", fontsize=15)
plt.tight_layout()
plt.show()

# --- Correlation Heatmap from Real Dataset ---
df = pd.read_csv("../data/penguins.csv")
numeric_df = df.select_dtypes(include=np.number)
correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidth=0.5
)

plt.title("Correlation Heatmap - Penguins Dataset", fontsize=15)
plt.tight_layout()
plt.show()
