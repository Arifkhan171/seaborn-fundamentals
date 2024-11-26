# Seaborn Pair Plot - Relationships Between All Numeric Variables
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv").head(150)

# Pair plot shows scatter for all numeric column combinations
sns.pairplot(
    df,
    hue="sex",
    palette="Dark2",
    kind="scatter"   # options: scatter, hist, reg, kde
)

plt.suptitle("Pair Plot - Penguins Dataset", y=1.02, fontsize=15)
plt.tight_layout()
plt.show()
