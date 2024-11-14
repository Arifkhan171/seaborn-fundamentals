# Seaborn Count Plot - Count of Observations Per Category
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv").head(150)

sns.countplot(
    x=df.island,
    hue=df.sex,
    palette="bwr"
)

plt.title("Penguin Count by Island and Sex", fontsize=15)
plt.xlabel("Island")
plt.ylabel("Count")
plt.legend(title="Sex")
plt.tight_layout()
plt.show()
