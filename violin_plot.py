import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib
# alternative to boxplot
df = pd.read_csv('Pokemon.csv', delimiter=',')
sns.violinplot(x="year", y="income", data=df)
plt.show()
