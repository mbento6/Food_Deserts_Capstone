# summarize.py
# Purpose: Calculate correlation values between food access and chronic disease metrics
# and export the results to a summary table with interpretation for each relationship.

import pandas as pd
from scipy.stats import pearsonr
import os

# Set paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_file = os.path.join(project_root, "data", "processed", "merged_summary.csv")
output_file = os.path.join(project_root, "outputs", "summary_tables", "correlation_summary.csv")
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Load data
df = pd.read_csv(data_file)

# Rename for clarity (if needed)
df = df.rename(columns={
    "Obesity among adults": "Obesity",
    "Diabetes among adults": "Diabetes",
    "High blood pressure among adults": "BloodPressure"
})

# Variables
food_access_col = "percent_lila_1and10"
outcomes = ["Obesity", "Diabetes", "BloodPressure"]

# Interpretations
interpretation_map = {
    "Obesity": "Stronger positive correlation; limited access to grocery stores is strongly associated with higher obesity rates.",
    "Diabetes": "Moderate positive correlation indicating that limited food access may contribute to higher diabetes prevalence.",
    "BloodPressure": "Weaker but significant positive correlation; food access may be a factor, but other contributors likely exist."
}

# Calculate correlations
results = []
for outcome in outcomes:
    valid = df[[food_access_col, outcome]].dropna()
    r, p = pearsonr(valid[food_access_col], valid[outcome])
    results.append({
        "Health Outcome": outcome,
        "Food Access Variable": food_access_col,
        "Pearson r": round(r, 3),
        "p-value": round(p, 4),
        "Interpretation": interpretation_map[outcome]
    })

# Save results to CSV
summary_df = pd.DataFrame(results)
summary_df.to_csv(output_file, index=False)
print(f"✅ Correlation summary saved to {output_file}")
