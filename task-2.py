import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("D:\one drive\Downloads\cleaned_titanic.csv")

# 1. Summary Statistics
print("Summary Statistics:")
print(df.describe(include='all'))

# 2. Histograms for Numeric Features
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']
df[numeric_cols].hist(bins=20, figsize=(12, 8))
plt.suptitle("Histograms of Numeric Features")
plt.tight_layout()
plt.savefig('histograms_numeric_features.png')
plt.show()

# 3. Boxplots for Numeric Features
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(y=df[col])
    plt.title(f"Boxplot of {col}")
    plt.savefig(f'boxplot_{col}.png')
    plt.show()

# 4. Correlation Matrix
plt.figure(figsize=(10, 8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix")
plt.savefig('correlation_matrix.png')
plt.show()

# 5. Pairplot
sns.pairplot(df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']])
plt.savefig('pairplot_selected_features.png')
plt.show()

# 6. Categorical Plots
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.savefig('survival_count.png')
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Class")
plt.savefig('survival_by_class.png')
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.savefig('survival_by_gender.png')
plt.show()
