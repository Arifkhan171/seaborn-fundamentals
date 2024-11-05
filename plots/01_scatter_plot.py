# Seaborn Scatter Plot - Visualize Relationships Between Variables
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv").head(100)

# Scatter plot with hue and style by sex
sns.scatterplot(
    x=df.bill_length_mm,
    y=df.flipper_length_mm,
    hue=df.sex,
    style=df.sex,
    s=100
)

plt.title("Bill Length vs Flipper Length by Sex", fontsize=15)
plt.xlabel("Bill Length (mm)")
plt.ylabel("Flipper Length (mm)")
plt.legend(title="Sex")
plt.tight_layout()
plt.show()
