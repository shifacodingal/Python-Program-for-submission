import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("penguins_size.csv")
sns.get_dataset_names()

df = sns.load_dataset('penguins')
df.head(10)
df.shape
df.tail()
df.isnull().sum()
df.describe()
df.describe()
df.dtypes