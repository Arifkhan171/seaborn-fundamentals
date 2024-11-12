# Seaborn Violin Plot - Distribution Shape Per Category
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv").head(150)

sns.violinplot(
    x=df.island,
    y=df.bill_length_mm,
    hue=df.sex,
    linewidth=3,
    palette="Dark2",
    saturation=0.8,
    split=True,      # mirror halves by hue
    inner="point"    # show individual data points inside
)

plt.title("Bill Length Distribution by Island and Sex", fontsize=15)
plt.xlabel("Island")
plt.ylabel("Bill Length (mm)")
plt.tight_layout()
plt.show()
