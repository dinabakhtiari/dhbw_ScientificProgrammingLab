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