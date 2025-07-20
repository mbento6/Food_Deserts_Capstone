import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import os

# Set up file paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_path = os.path.join(project_root, "data", "processed", "merged_summary.csv")
output_dir = os.path.join(project_root, "outputs", "figures")
os.makedirs(output_dir, exist_ok=True)

# Load the merged data
df = pd.read_csv(data_path)

# Choose key variables
food_access_col = "percent_lila_1and10"
outcomes = [
    "Obesity among adults",
    "Diabetes among adults",
    "High blood pressure among adults"  # proxy for cardiovascular risk
]

# Scatter plots with correlation
for outcome in outcomes:
    x = df[food_access_col]
    y = df[outcome]

    # Drop NaNs
    valid = df[[food_access_col, outcome]].dropna()
    r, p = pearsonr(valid[food_access_col], valid[outcome])

    plt.figure(figsize=(8, 6))
    sns.regplot(data=valid, x=food_access_col, y=outcome, scatter_kws={"s": 60}, line_kws={"color": "red"})
    plt.title(f"{outcome} vs. Food Access\nr = {r:.2f}, p = {p:.4f}")
    plt.xlabel("% Census Tracts with Limited Access (LILA 1&10)")
    plt.ylabel(outcome)
    plt.grid(True)
    plt.tight_layout()

    filename = f"{outcome.lower()}_vs_food_access.png".replace(" ", "_")
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

# Correlation heatmap
selected_cols = [food_access_col] + outcomes
corr = df[selected_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
plt.close()

# Bar charts for top/bottom 10 states
for outcome in outcomes:
    # Top 10
    top10 = df.sort_values(outcome, ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top10, x=outcome, y="State", palette="Reds_r")
    plt.title(f"Top 10 States by {outcome}")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"top10_{outcome.lower().replace(' ', '_')}.png"))
    plt.close()

    # Bottom 10
    bottom10 = df.sort_values(outcome, ascending=True).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=bottom10, x=outcome, y="State", palette="Greens")
    plt.title(f"Bottom 10 States by {outcome}")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"bottom10_{outcome.lower().replace(' ', '_')}.png"))
    plt.close()


print("✅ Visualizations saved to:", output_dir)
