import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('Pokemon.csv', index_col=0, delimiter=',')
sns.boxplot(data=df)
plt.show()