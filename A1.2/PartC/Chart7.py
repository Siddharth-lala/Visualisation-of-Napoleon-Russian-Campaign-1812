import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D

data = pd.read_csv('gapminder.csv')

# Normalizing the population data to adjust marker size
norm_pop = (data['pop'] - data['pop'].min()) / (data['pop'].max() - data['pop'].min())
scaled_pop = norm_pop * 1000  # Scaling the population for better visibility of marker size

# Set figure size and layout
fig, ax = plt.subplots(figsize=(14, 8))  # Larger figure size for better spacing

# Creating a scatter plot to encode all the attributes
sns.scatterplot(
    x='year', 
    y='lifeExp', 
    size=scaled_pop,  # Population encoded by marker size
    hue='gdpPercap',  # GDP per capita encoded by color intensity
    style='continent',  # Continent encoded by marker shape
    palette='coolwarm',  # Color palette for GDP per capita
    sizes=(50, 2000),  
    data=data,
    alpha=0.7, 
    ax=ax  
)

ax.set_title('Attributes of Life Expectancy, Population, GDP Per Capita, and Continent over Time', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14, fontweight='bold', color='darkblue')
ax.set_ylabel('Life Expectancy', fontsize=14, fontweight='bold', color='darkred')

# Adding colorbar for GDP per Capita
norm = plt.Normalize(data['gdpPercap'].min(), data['gdpPercap'].max())
sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, label='GDP per Capita')

# Creating the legend for continents
continent_legend_handles = [
    Line2D([0], [0], marker='o', color='w', label='Africa', markerfacecolor='gray', markersize=10, linestyle=''),
    Line2D([0], [0], marker='s', color='w', label='Americas', markerfacecolor='gray', markersize=10, linestyle=''),
    Line2D([0], [0], marker='D', color='w', label='Asia', markerfacecolor='gray', markersize=10, linestyle=''),
    Line2D([0], [0], marker='^', color='w', label='Europe', markerfacecolor='gray', markersize=10, linestyle=''),
    Line2D([0], [0], marker='X', color='w', label='Oceania', markerfacecolor='gray', markersize=10, linestyle='')
]


first_legend = ax.legend(handles=continent_legend_handles, title='Continent', loc='upper left', fontsize=10)
ax.add_artist(first_legend)  # Add the first legend back after the second one

# Adding a size legend for population
legend_sizes = [50, 500, 1000, 2000] 
legend_labels = ['Small Pop', 'Medium Pop', 'Large Pop', 'Very Large Pop']
size_handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', markersize=np.sqrt(size), 
                       label=label, linestyle='') for size, label in zip(legend_sizes, legend_labels)]

ax.legend(handles=size_handles, title='Population (Marker Size)', loc='lower right')


plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()  
plt.show()
