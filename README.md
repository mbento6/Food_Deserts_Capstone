# Food Deserts & Chronic Disease: Capstone Project

## Business Question

**How does limited access to grocery stores relate to the prevalence of obesity, diabetes, and cardiovascular disease in communities across the United States?**

This capstone explores the intersection of food access and chronic disease. The goal is to uncover whether communities classified as food deserts, those with low-income populations and limited access to healthy grocery options, show higher prevalence rates of chronic conditions.

---

## Datasets Used

### 1. **USDA Food Access Research Atlas**

* Level: Census Tract
* Key Fields: `LILATracts_1And10`, `PovertyRate`, `MedianFamilyIncome`, `State`, `County`
* Describes population-level access to healthy food based on income, vehicle access, and distance from stores
* https://www.ers.usda.gov/data-products/food-access-research-atlas/

### 2. **CDC Chronic Disease Indicators (BRFSS)**

* Level: State
* Key Fields: `Obesity among adults`, `Diabetes among adults`, `High blood pressure among adults`
* Captures the prevalence of chronic diseases and behaviors across U.S. states
* https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators/hksd-2xuw (Manually paste it into your browser)

---

## Data Wrangling

* Extracted and filtered relevant columns from both datasets
* Summarized food access indicators to the state level
* Filtered CDC data to include only the latest available values, and renamed columns for clarity
* Merged both datasets on the `State` column to enable side-by-side analysis

Resulting dataset saved to:

```
data/processed/merged_summary.csv
```

---

## Visualizations

Visualizations generated in `scripts/visualize.py` and saved to `outputs/figures/`:

1. **Scatter Plots (with r & p values)**

   * Obesity vs. % LILA Tracts
   * Diabetes vs. % LILA Tracts
   * Blood Pressure vs. % LILA Tracts

2. **Bar Charts**

   * Top 10 and Bottom 10 states by Obesity, Diabetes, Blood Pressure

3. **Correlation Heatmap**

   * Visual overview of relationships between food access and disease metrics

---

## Project Structure

```
Food_Deserts_Capstone/
├── data/
│   ├── raw/
│   │   ├── Food_Access_Raw.csv
│   │   └── Chronic_Diseases_Raw.csv
│   ├── processed/
│   │   └── merged_summary.csv
│
├── notebooks/
│   ├── 01_data_wrangling.ipynb
│   └── 02_analysis_visuals.ipynb
│
├── scripts/
│   ├── visualize.py
│   └── summarize.py
│
├── outputs/
│   ├── figures/
│   │   ├── correlation_heatmap.png
│   │   ├── obesity_vs_food_access.png
│   │   ├── diabetes_vs_food_access.png
│   │   ├── diabetes_among_adults_vs_food_access.png
│   │   ├── high_vs_food_access.png
│   │   ├── high_blood_pressure_among_adults_vs_food_access.png
│   │   ├── top10_diabetes_among_adults.png
│   │   ├── top10_high_blood_pressure_among_adults.png
│   │   ├── top10_obesity_among_adults.png
│   │   ├── bottom10_high_blood_pressure_among_adults.png
│   │   ├── bottom10_obesity_among_adults.png
│   │   └── bottom10_diabetes_among_adults.png
│   └── summary_tables/
│       └── correlation_summary.csv
│
├── reports/
│   └── capstone_summary.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Key Findings

* A positive correlation exists between limited grocery access and adult obesity rates (r = ...)
* Diabetes and blood pressure rates also show moderate correlations with food desert status
* States with the highest % of LILA-designated tracts often have above-average chronic disease prevalence

---

## Tools & Libraries

* **Python**: `pandas`, `seaborn`, `matplotlib`, `scipy`
* **PyCharm** for scripting
* **Jupyter Notebook** for EDA (optional)

---

## How to Run

1. Run `wrangle.py` to process and merge datasets
2. Run `visualize.py` to generate charts in `outputs/figures`

```bash
python scripts/visualize.py
```

---

## Status

Complete ,  ready for presentation, review, and submission

---

## Credits

* USDA Economic Research Service
* CDC BRFSS Chronic Disease Indicators

---

## Contact

Lead Analyst: Mike Benton
Email: mbento6@wgu.edu
GitHub: [github.com/mbento6/Food\_Deserts\_Capstone](https://github.com/mbento6/Food_Deserts_Capstone.git)
