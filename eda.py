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
