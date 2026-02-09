import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('penguins.csv')
print(df.shape)
# (344, 7)

print("\nFirst 5 rows:")
print(df.head())