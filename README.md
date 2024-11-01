# Seaborn Fundamentals

A complete, structured practice repository covering Seaborn statistical data visualization — from basic plots to advanced multi-plot grids using the real Penguins dataset.

---

## 📌 About This Repository

This repository covers all essential Seaborn plot types with a real-world dataset. Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive statistical graphics — essential for Exploratory Data Analysis (EDA) in Machine Learning.

All plots use the **Penguins dataset** — a real biological dataset containing measurements of 344 penguins across 3 islands.

---

## 📁 Repository Structure

```
seaborn-fundamentals/
│
├── plots/
│   ├── 01_scatter_plot.py      # Scatter plot with hue and style
│   ├── 02_line_plot.py         # Line plot with multiple categories
│   ├── 03_histogram.py         # Distribution with KDE overlay
│   ├── 04_box_plot.py          # Statistical distribution by category
│   ├── 05_violin_plot.py       # Distribution shape with split by sex
│   ├── 06_strip_plot.py        # Individual data points per category
│   ├── 07_count_plot.py        # Count of observations per category
│   ├── 08_heatmap.py           # Matrix heatmap + correlation heatmap
│   ├── 09_pair_plot.py         # All variable relationships in one plot
│   ├── 10_facet_grid.py        # Separate subplot per category
│   └── 11_styling_catplot.py   # Themes, despine, catplot
│
├── data/
│   └── penguins.csv            # Real penguins biological dataset
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Topics Covered

| # | Plot Type | Key Concepts |
|---|-----------|-------------|
| 01 | Scatter Plot | hue, style, size, relationships |
| 02 | Line Plot | trends, hue, style, markers, palette |
| 03 | Histogram | bins, kde, distribution analysis |
| 04 | Box Plot | IQR, outliers, hue, showmeans |
| 05 | Violin Plot | distribution shape, split, inner |
| 06 | Strip Plot | jitter, individual points, categories |
| 07 | Count Plot | category frequency, hue, palette |
| 08 | Heatmap | annot, cmap, correlation matrix |
| 09 | Pair Plot | all variable pairs, hue, kind |
| 10 | FacetGrid | subplots per category, map |
| 11 | Styling & catplot | set_style, set_context, despine, kind |

---

## 📊 Dataset

**Penguins Dataset** — 344 rows, 7 columns

| Column | Description |
|--------|-------------|
| species | Penguin species (Adelie, Chinstrap, Gentoo) |
| island | Island name (Biscoe, Dream, Torgersen) |
| bill_length_mm | Bill length in millimeters |
| bill_depth_mm | Bill depth in millimeters |
| flipper_length_mm | Flipper length in millimeters |
| body_mass_g | Body mass in grams |
| sex | Male or Female |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## 🚀 How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/Arifkhan171/seaborn-fundamentals.git
cd seaborn-fundamentals
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run any plot:**
```bash
python plots/01_scatter_plot.py
python plots/08_heatmap.py
```

---

## 👤 Author

**Arif Khan**
Final Year CS Student | University of Loralai | ML • Deep Learning • Agentic AI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/arif-khan-71a711376)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github)](https://github.com/Arifkhan171)

---

> ⭐ Part of a complete Data Science & AI portfolio — from Seaborn basics to Agentic AI systems.
