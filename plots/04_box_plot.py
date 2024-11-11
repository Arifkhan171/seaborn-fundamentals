# Seaborn Box Plot - Statistical Distribution Per Category
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv")

sns.boxplot(
    x="island",
    y="flipper_length_mm",
    data=df,
    hue="sex",
    showmeans=True
)

plt.title("Flipper Length Distribution by Island and Sex", fontsize=15)
plt.xlabel("Island")
plt.ylabel("Flipper Length (mm)")
plt.legend(title="Sex")
plt.tight_layout()
plt.show()
