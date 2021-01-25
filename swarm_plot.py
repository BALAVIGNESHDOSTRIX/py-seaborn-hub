import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

df = pd.read_csv('1000_companies.csv')
# Swarm plot with Pokemon color palette
sns.swarmplot(x='R&D Spend', y='Administration', data=df,
              palette=pkmn_type_colors)
plt.show()