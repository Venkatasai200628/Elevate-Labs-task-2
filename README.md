# Elevate-Labs-task-2
Overview
This project is part of an AI & ML internship and focuses on performing Exploratory Data Analysis (EDA) on the cleaned Titanic dataset. The goal is to uncover insights, identify patterns, and visualize relationships between features that might influence survival outcomes.

Objectives
Understand data distributions and statistical summaries.
Visualize relationships between variables.
Detect patterns and potential anomalies.
Draw initial inferences useful for predictive modeling.

Tools & Libraries
Python
Pandas
Matplotlib
Seaborn

Dataset
File Used: cleaned_titanic.csv
This is a preprocessed version of the original Titanic dataset with missing values handled, categorical variables encoded, and outliers removed.

EDA Steps
1. Summary Statistics
Used .describe() to display central tendencies and spread of the features.
2. Histograms
Plotted histograms for numeric features (Age, Fare, SibSp, Parch) to understand distribution and skewness.
3. Boxplots
Used boxplots to visualize spread and detect any residual outliers in numeric features.
4. Correlation Matrix
Generated a heatmap to understand relationships and multicollinearity among numerical variables.
5. Pairplot
Plotted pairwise relationships between key features like Survived, Pclass, Sex, Age, and Fare.
6. Categorical Feature Analysis
Countplot of overall survival.
Survival distribution based on Gender and Passenger Class.

Visual Outputs
The following plots were saved:
histograms_numeric_features.png
boxplot_Age.png, boxplot_Fare.png, etc.
correlation_matrix.png
pairplot_selected_features.png
survival_count.png
survival_by_class.png
survival_by_gender.png

Key Takeaways
Higher survival rates were observed for females and first-class passengers.
Fare and Pclass showed moderate correlation.
Most passengers had siblings/spouses or parents/children accompanying them.

Conclusion
This EDA step provided valuable insights into the Titanic dataset and helped in preparing the ground for building predictive models.
