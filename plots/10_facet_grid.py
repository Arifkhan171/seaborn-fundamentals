# Seaborn FacetGrid - Separate Subplots Per Category
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv")

# FacetGrid creates a separate subplot for each category
grid = sns.FacetGrid(df, col="sex", height=5)
grid.map(
    sns.scatterplot,
    "bill_length_mm",
    "flipper_length_mm",
    alpha=0.7
)
grid.add_legend()
grid.set_axis_labels("Bill Length (mm)", "Flipper Length (mm)")
grid.set_titles(col_template="Sex: {col_name}")

plt.suptitle("FacetGrid - Bill vs Flipper by Sex", y=1.03, fontsize=15)
plt.tight_layout()
plt.show()
