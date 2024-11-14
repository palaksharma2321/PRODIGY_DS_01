# -*- coding: utf-8 -*-
"""ProdigyInfotechDS01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11BIoewLWWBcl3eCBvuYqlyTN2_uRAV5U
"""

from google.colab import drive
drive.mount('/drive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv("/drive/MyDrive/ProdigyInfotech/task1.csv", delimiter=',', on_bad_lines='skip')
except pd.errors.ParserError as e:
    print(f"Error reading CSV with delimiter ',': {e}")
    try:
        df = pd.read_csv("/drive/MyDrive/ProdigyInfotech/task1.csv", delimiter='\t', on_bad_lines='skip')
        print("Successfully read CSV using delimiter '\\t'")
    except pd.errors.ParserError as e:
        print(f"Error reading CSV with delimiter '\\t': {e}")
        print("Please check your CSV file for other potential delimiters or data issues.")

df.head(5)

df.tail(5)

df.columns

df.info()

df.duplicated().sum()

df.isna().sum()

print(df['Country Name'].unique())
print("\n Total no of unique countries:",df['Country Name'].nunique())

total_population_data = df[df['Indicator Code'] == 'SP.POP.TOTL']
total_population_sorted = total_population_data.sort_values(by="2023", ascending=False)
total_top_ten_countries = total_population_sorted.head(10)
print("Top ten countries of total population\n")
print(total_top_ten_countries[['Country Code']])

plt.figure(figsize=(15, 6))
plt.subplot(2,2,1)
sns.barplot(x="2023", y="Country Code", data=total_top_ten_countries, palette="coolwarm")
plt.title("Top Ten Countries of Total Population (2023)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()

total_population_sorted1 = total_population_data.sort_values(by="2023", ascending=True)
total_bottom_ten_countries = total_population_sorted1.head(10)
print("Bottom ten countries of total population\n")
print(total_bottom_ten_countries[['Country Code']])

plt.figure(figsize=(15, 6))
plt.subplot(2,2,1)
sns.barplot(x="2022", y="Country Code", data=total_bottom_ten_countries, palette="viridis")
plt.title("Bottom Ten Countries of Total Population (2023)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()