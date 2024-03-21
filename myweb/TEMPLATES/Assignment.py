
import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation%matplotlib inline
sns.set(color_codes=True)

df = pd.read_csv("https://github.com/YBI-Foundation/Dataset/raw/main/House%20Prices.csv")
# To display the top 5 rows
df.head(5)