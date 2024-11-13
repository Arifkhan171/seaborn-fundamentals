# Seaborn Strip Plot - Individual Data Points Per Category
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv").head(150)

sns.stripplot(
    x="island",
    y="flipper_length_mm",
    data=df,
    hue="sex",
    size=7,
    marker="*",
    jitter=True      # spread points to avoid overlap
)

plt.title("Flipper Length by Island (Strip Plot)", fontsize=15)
plt.xlabel("Island")
plt.ylabel("Flipper Length (mm)")
plt.legend(title="Sex")
plt.tight_layout()
plt.show()
