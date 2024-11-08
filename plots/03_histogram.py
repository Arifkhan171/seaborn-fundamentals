# Seaborn Histogram - Distribution of a Single Variable
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv").head(150)

sns.histplot(
    df.bill_length_mm,
    bins=[32, 34, 36, 38, 40, 42, 44, 46, 48],
    kde=True,        # overlay a smooth density curve
    color="steelblue"
)

plt.title("Distribution of Bill Length", fontsize=15)
plt.xlabel("Bill Length (mm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
