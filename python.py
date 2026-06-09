import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("healthy_diet.csv")

print(df.info())
print(df.head())
print(df.isnull().sum())
print(df.describe())

for col in df.select_dtypes(include='object').columns:
    print(col)
    print(df[col].unique())

print(df['Gender'].value_counts())
print(df['Diet_Plan'].value_counts())

health_map = {
    'Underweight': 0,
    'Healthy': 1,
    'Overweight': 2,
    'Obese': 3
}

df['Health_Status_Num'] = df['Health_Status'].map(health_map)

df.rename(columns={
    'Daily_Calorie_Consumed': 'Calories_Consumed',
    'Daily_Calorie_Requirement': 'Calories_Required'
}, inplace=True)

corr = df.corr(numeric_only=True)

print(corr)

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(
    x='Calories_Consumed',
    y='BMI',
    hue='Health_Status',
    data=df
)
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x='Diet_Plan', data=df)
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='Health_Status', y='BMI', data=df)
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x='Diet_Plan', y='BMI', data=df)
plt.xticks(rotation=45)
plt.show()

sns.pairplot(df)
plt.show()