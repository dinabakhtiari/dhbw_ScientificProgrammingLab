import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('EDA_Project/KC_housing_data.csv')

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# بررسی مقادیر خالی (Missing Values)
print(df.isnull().sum())