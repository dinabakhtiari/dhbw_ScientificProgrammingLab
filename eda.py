import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('penguins.csv')
print(df.shape)
# (344, 7)

print("\nFirst 5 rows:")
print(df.head())

print("\nData Types and Missing Values:")
print(df.info())
# Total Number of Rows: 344 (RangeIndex: 344 entries).
# There are 2 missing rows in the columns related to bill measurements and body mass (bill_length_mm, bill_depth_mm, flipper_length_mm, and body_mass_g), leaving 342 non-null entries out of a total of 344
# The 'sex' column contains 11 missing rows, with 333 non-null entries out of 344 total.

print("\nSummary Statistics:")
print(df.describe())
# count      342.000000     342.000000         342.000000   342.000000
# mean        43.921930      17.151170         200.915205  4201.754386
# std          5.459584       1.974793          14.061714   801.954536
# min         32.100000      13.100000         172.000000  2700.000000
# 25%         39.225000      15.600000         190.000000  3550.000000
# 50%         44.450000      17.300000         197.000000  4050.000000
# 75%         48.500000      18.700000         213.000000  4750.000000
# max         59.600000      21.500000         231.000000  6300.000000


print("\n--- Missing Values Before Cleaning ---")
print(df.isnull().sum())


# --- Step 2: Data Cleaning ---
# 1. Drop rows where essential measurements are missing
# This removes the 2 rows we found in Step 1 that had no bill or flipper data.
df_clean = df.dropna(subset=['bill_length_mm', 'flipper_length_mm'])

# 2. Fill missing values in the 'sex' column with 'Unknown'
# This handles the 11 missing values without deleting the whole row.
df_clean['sex'] = df_clean['sex'].fillna('Unknown')

# 3. Verify cleaning results 
print("Missing values per column after cleaning:")
print(df_clean.isnull().sum())

# 4. Check the species distribution to ensure data balance
print("\nFinal species counts:")
print(df_clean['species'].value_counts())


# Create a 2x2 subplot grid with a specific size
# figsize=(12, 10) ensures the plots are large enough to read
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# A) Histogram: distribution of bill length by species
sns.histplot(data=df_clean, x='bill_length_mm', hue='species', kde=True, ax=ax[0,0]) 
ax[0,0].set_title('Bill Length by Species')

# B) Boxplot: flipper length distribution across species
sns.boxplot(data=df_clean, x='species', y='flipper_length_mm', ax=ax[0,1]) 
ax[0,1].set_title('Flipper Length by Species')

# C) Scatterplot: relationship between bill length and body mass
sns.scatterplot(data=df_clean, x='bill_length_mm', y='body_mass_g', hue='species', ax=ax[1,0])
ax[1,0].set_title('Bill vs Body Mass')

# D) Countplot: number of species found on each island
sns.countplot(data=df_clean, x='island', hue='species', ax=ax[1,1])
ax[1,1].set_title('Species by Island')

# Adjust the padding between plots
plt.tight_layout()
plt.show()
