# Seaborn Styling and catplot - Themes and Figure-Level Plots
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/penguins.csv")

# --- Styling Options ---
# Available styles: darkgrid, whitegrid, dark, white, ticks
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

sns.barplot(
    x="island",
    y="bill_length_mm",
    data=df,
    palette="muted"
)
sns.despine()  # remove top and right borders

plt.title("Average Bill Length by Island", fontsize=15)
plt.xlabel("Island")
plt.ylabel("Bill Length (mm)")
plt.tight_layout()
plt.show()

# --- catplot - Figure Level Categorical Plot ---
# kind options: strip, swarm, box, boxen, violin, bar, count, point
sns.catplot(
    x="island",
    y="bill_length_mm",
    data=df,
    hue="sex",
    kind="boxen",
    height=5,
    aspect=1.5
)

plt.suptitle("catplot - Bill Length by Island and Sex", y=1.02, fontsize=15)
plt.tight_layout()
plt.show()
