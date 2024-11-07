# Seaborn Line Plot - Trends Over Continuous Data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv").head(200)

sns.lineplot(
    x="bill_length_mm",
    y="flipper_length_mm",
    data=df,
    hue="sex",
    style="sex",
    palette="Accent",
    markers=["o", ">"]
)

plt.title("Bill Length vs Flipper Length Trend by Sex", fontsize=15)
plt.xlabel("Bill Length (mm)")
plt.ylabel("Flipper Length (mm)")
plt.grid()
plt.tight_layout()
plt.show()
