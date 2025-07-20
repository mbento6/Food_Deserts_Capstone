# Capstone Summary: Food Deserts & Chronic Disease

## A. Project Overview

### Research Question
How does limited access to grocery stores relate to the prevalence of obesity, diabetes, and cardiovascular disease in communities across the United States?

### Scope
This project focused on analyzing the relationship between food access and chronic illness across U.S. states. While the original intent was to work at the county level, dataset compatibility and granularity led to a decision to aggregate metrics to the state level. The goal was to uncover trends that could inform public health decisions.

### Solution Overview
Using data from the USDA Food Access Research Atlas and the CDC’s Chronic Disease Indicators, I built a cleaned and merged dataset. Python (via PyCharm) was used to wrangle, analyze, and visualize the data. Analytical methods included correlation analysis and summary statistics. Visual outputs were generated using Seaborn and Matplotlib and organized to support storytelling.

---

## B. Project Execution

### Project Plan vs. Execution
Initially, I planned to align data at the county level using FIPS codes, but the CDC dataset’s state-level granularity required shifting to a state-level analysis.

### Planning Methodology
I followed the CRISP-DM methodology, moving from business understanding through evaluation and deployment. I remained flexible when real-world data limitations impacted the planned workflow.

### Timeline & Milestones
- Days 1–2: Data sourcing and cleaning
- Day 3: Exploratory data analysis
- Day 4–5: Correlation and visualization
- Day 6: Report drafting
- Day 7: Final polishing, README, and Panopto prep

---

## C. Methodology

### Data Selection & Collection
I pulled food access data from the USDA (2010 census tract level) and chronic disease data from the CDC’s BRFSS dataset (latest years available). Because the data differed in granularity, I aggregated the USDA data to the state level to match the CDC’s format.

#### Obstacles Encountered
- Mismatched geographic levels between datasets
- Missing or overly verbose column names required renaming and simplification

#### Governance Issues
There were no privacy or security issues as all data was publicly available. Still, I took care not to overstate conclusions from correlation-based analysis.

### Dataset Pros & Cons
**Advantages:**
- Authoritative, well-documented public sources
- Consistent variable formats

**Limitations:**
- The USDA dataset is based on 2010 data, which may not reflect current food access
- State-level aggregation may obscure local disparities

---

## D. Data Extraction & Preparation
I used Python with Pandas for loading, cleaning, transforming, and joining data. The wrangling process involved:

- Filtering for relevant indicators
- Grouping by state and calculating summary stats
- Renaming inconsistent columns
- Saving results to CSV for easy reuse

These processes were appropriate because they allowed flexible transformation, and Python’s ecosystem is ideal for reproducible, script-based workflows.

---

## E. Data Analysis

### Methods Used
- Descriptive statistics
- Pearson correlation coefficient (r)

### Tool Advantages & Limitations
Initially, I planned to build visuals in Tableau to take advantage of its drag-and-drop interface and interactivity. However, I found Python to be the better fit for this project because it allowed for complete control over the data pipeline, from wrangling to visual output. This also helped maintain consistency and reproducibility without switching tools midstream.

**Advantages:** Python's libraries are highly customizable and reproducible. Seaborn made it easy to build visually compelling plots.

**Limitations:** Seaborn doesn’t support fully interactive visuals. Also, while correlation is useful, it doesn’t confirm causation.

### Step-by-Step Process
1. Loaded and cleaned both datasets
2. Aggregated USDA food access indicators by state
3. Merged datasets on `State`
4. Calculated Pearson correlations between food access and:
   - Obesity (r = 0.569, p < 0.001)
   - Diabetes (r = 0.524, p = 0.0001)
   - Blood pressure (r = 0.378, p = 0.0068)
5. Created scatter plots and bar charts to visualize high- and low-risk states

---

## F. Results

### F1. Output Evaluation
The merged dataset and visuals were accurate, complete, and reproducible. The correlation coefficients were statistically significant, supporting the hypothesis.

### F2. Practical Significance
Findings confirm that states with higher percentages of food deserts also show higher chronic disease rates. This insight can guide public health policy, such as where to invest in mobile markets or grocery infrastructure.

### F3. Overall Success
While county-level detail was sacrificed, the state-level approach revealed clear, interpretable trends. The project succeeded in generating usable insights with clean data and actionable outputs.

---

## G. Key Takeaways

### G1. Conclusions
There is a statistically significant positive relationship between limited food access and rates of obesity and diabetes. Blood pressure showed a weaker but still meaningful correlation.

### G2. Visual Communication
Charts were built with Seaborn and Matplotlib using consistent color palettes, labels, and annotations to aid interpretability. The heatmap and scatter plots clearly communicate key relationships.

### G3. Recommendations
1. Prioritize public investment in food infrastructure in states with the highest LILA percentages.
2. Use these insights to support grant proposals, mobile market planning, or policy reforms aimed at underserved populations.

---

**Lead Analyst:** Mike Benton  
**Email:** mbento6@wgu.edu  
**GitHub:** [github.com/mbento6/Food_Deserts_Capstone](https://github.com/mbento6/Food_Deserts_Capstone.git)
