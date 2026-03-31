📊 AI Usage and Academic Performance Study
📌 Project Overview

This project explores the relationship between AI tool usage and academic performance among college students. The goal is to understand how students interact with AI tools (such as ChatGPT and other learning technologies) and how these interactions influence their motivation, attitudes, and potential academic outcomes.

The study combines Exploratory Data Analysis (EDA), statistical modeling, and literature review to investigate key factors that drive AI adoption in education.

📂 Dataset

The dataset used in this project comes from a publicly available survey dataset (via Mendeley/Pew-style data), containing responses from over 600 students.

It includes variables such as:

Demographics (Gender, University, Education Level)
AI usage type
Perception of AI (PE1–PE20)
Curiosity (CU1–CU4)
Attitudes toward AI (ATU1–ATU5)
Actual usage (AUP1–AUP5)
Motivation to use AI (MIUA1–MIUA5)
🧹 Data Processing

The dataset was cleaned and transformed by:

Handling missing values
Creating composite variables using mean scores:
PE_mean (Perceived Ease)
CU_mean (Curiosity)
ATU_mean (Attitudes Toward AI)
AUP_mean (Actual Usage Patterns)
MIUA_mean (Motivation to Use AI)
📊 Analysis Performed
🔍 Exploratory Data Analysis (EDA)
Summary statistics (mean, median, distribution)
Correlation analysis
Visualizations (heatmaps, scatterplots, histograms)
📈 Statistical Modeling
Multiple Linear Regression
Outcome variable: MIUA_mean
Predictors: PE_mean, CU_mean, ATU_mean, AUP_mean
Key finding:
Attitudes toward AI and actual usage are the strongest predictors of motivation
🧪 Hypothesis Testing
Relationships between AI usage and motivation
Group comparisons (t-tests / ANOVA)
📚 Research Context

This project is supported by peer-reviewed research, including:

Zhu (2026):
AI usage, self-efficacy, and academic performance in business education
Found that AI usage improves academic performance
Academic self-efficacy acts as a mediator
Teacher support strengthens these effects

This aligns with this project’s findings that:

Positive attitudes and engagement with AI tools are key drivers of motivation
Behavioral usage matters more than curiosity alone
🛠️ Tools & Technologies
Python (pandas, statsmodels, matplotlib)
R (tidyverse, corrplot)
VS Code
GitHub for version control
📌 Key Findings
Motivation to use AI is strongly influenced by:
Attitudes toward AI
Actual usage behavior
Perceived ease also plays a role
Curiosity alone is not a strong predictor
Results support existing research on self-efficacy and AI adoption in education
🚀 Future Work
Incorporate academic performance metrics (e.g., GPA)
Explore causal relationships using experimental or longitudinal data
Apply machine learning models for prediction
Investigate moderating variables (e.g., teacher support, field of study)
👩‍💻 Author

Sherry Huang
RPI – IT & Web Science
