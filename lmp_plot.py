import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib

df = pd.read_csv('Pokemon.csv', delimiter=',')
sns.lmplot(x='year', y='income', data=df)
plt.show()