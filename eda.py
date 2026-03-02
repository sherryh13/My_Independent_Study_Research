# eda.py - Full EDA with Hypothesis Testing
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import os
from scipy import stats

# -------------------------------
# Step 0: Create results folder
# -------------------------------
if not os.path.exists("../results"):
    os.makedirs("../results")

# -------------------------------
# Step 1: Load Excel dataset
# -------------------------------
df = pd.read_excel("../Data/ai_adoption_students.xlsx")
print("Original shape:", df.shape)

# Drop rows with missing values and make a copy
df_clean = df.dropna().copy()
print("Clean shape:", df_clean.shape)

# -------------------------------
# Step 2: Compute construct averages
# -------------------------------
df_clean.loc[:, "PE_mean"] = df_clean[[f"PE{i}" for i in range(1,21)]].mean(axis=1)
df_clean.loc[:, "CU_mean"] = df_clean[[f"CU{i}" for i in range(1,5)]].mean(axis=1)
df_clean.loc[:, "ATU_mean"] = df_clean[[f"ATU{i}" for i in range(1,6)]].mean(axis=1)
df_clean.loc[:, "AUP_mean"] = df_clean[[f"AUP{i}" for i in range(1,6)]].mean(axis=1)
df_clean.loc[:, "MIUA_mean"] = df_clean[[f"MIUA{i}" for i in range(1,6)]].mean(axis=1)

print(df_clean[["PE_mean","CU_mean","ATU_mean","AUP_mean","MIUA_mean"]].head())

# -------------------------------
# Step 3: Correlation matrix
# -------------------------------
corr = df_clean[["PE_mean","CU_mean","ATU_mean","AUP_mean","MIUA_mean"]].corr()
print("\nCorrelation Matrix:\n", corr)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix of AI Motivation Constructs")
plt.tight_layout()
plt.savefig("../results/correlation_heatmap.png")
plt.close()

# -------------------------------
# Step 4: Regression analysis
# -------------------------------
X = df_clean[["PE_mean","CU_mean","ATU_mean","AUP_mean"]]
y = df_clean["MIUA_mean"]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print("\nRegression Summary:\n")
print(model.summary())
with open("../results/regression_summary.txt", "w") as f:
    f.write(model.summary().as_text())

# -------------------------------
# Step 5: Scatter plots
# -------------------------------
for var in ["PE_mean","CU_mean","ATU_mean","AUP_mean"]:
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=df_clean[var], y=df_clean["MIUA_mean"])
    sns.regplot(x=df_clean[var], y=df_clean["MIUA_mean"], scatter=False, color="red")
    plt.title(f"MIUA_mean vs {var}")
    plt.xlabel(var)
    plt.ylabel("MIUA_mean")
    plt.tight_layout()
    plt.savefig(f"../results/MIUA_vs_{var}.png")
    plt.close()

# -------------------------------
# Step 6: Demographics summary
# -------------------------------
demographics = ["Gender", "Level of Education", "Fields of Study"]
for col in demographics:
    counts = df_clean[col].value_counts()
    counts.to_csv(f"../results/{col}_counts.csv")
    print(f"\n{col} counts saved to results/{col}_counts.csv")

# -------------------------------
# Step 7: Hypothesis Testing
# -------------------------------

# T-test example: Gender (2 groups)
if df_clean["Gender"].nunique() == 2:
    group1 = df_clean[df_clean["Gender"] == df_clean["Gender"].unique()[0]]["MIUA_mean"]
    group2 = df_clean[df_clean["Gender"] == df_clean["Gender"].unique()[1]]["MIUA_mean"]
    t_stat, p_val = stats.ttest_ind(group1, group2)
    print(f"\nT-test Gender MIUA_mean: t={t_stat:.3f}, p={p_val:.3f}")
    with open("../results/t_test_gender.csv", "w") as f:
        f.write(f"Group1: {df_clean['Gender'].unique()[0]}, Group2: {df_clean['Gender'].unique()[1]}\n")
        f.write(f"t-statistic,p-value\n{t_stat},{p_val}\n")

# ANOVA example: Level of Education (3+ groups)
anova_results = []
if df_clean["Level of Education"].nunique() > 2:
    levels = df_clean["Level of Education"].unique()
    samples = [df_clean[df_clean["Level of Education"]==lvl]["MIUA_mean"] for lvl in levels]
    f_stat, p_val = stats.f_oneway(*samples)
    print(f"\nANOVA Level of Education MIUA_mean: F={f_stat:.3f}, p={p_val:.3f}")
    with open("../results/anova_education.csv", "w") as f:
        f.write("F-statistic,p-value\n")
        f.write(f"{f_stat},{p_val}\n")

# You can add more hypothesis tests here (e.g., Fields of Study, AI Type)