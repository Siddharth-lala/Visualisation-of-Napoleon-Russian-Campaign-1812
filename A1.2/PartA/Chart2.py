import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D


data = pd.read_csv('gapminder.csv')


data_2002 = data[data['year'] == 2002]

# Normalize the population data for color intensity
norm_pop = (data_2002['pop'] - data_2002['pop'].min()) / (data_2002['pop'].max() - data_2002['pop'].min())

plt.figure(figsize=(12, 8))

markers = {'Africa': 'o', 'Americas': 's', 'Asia': 'D', 'Europe': '^', 'Oceania': 'X'}

palette = sns.color_palette('Blues', as_cmap=True)

for continent, marker in markers.items():
    continent_data = data_2002[data_2002['continent'] == continent]
    plt.scatter(
        continent_data['gdpPercap'], 
        continent_data['lifeExp'], 
        c=norm_pop[continent_data.index],  # Color intensity based on normalized population
        cmap='Blues', 
        marker=marker, 
        s=200, 
        edgecolor='black', 
        alpha=0.8, 
        label=continent
    )

# Adding a color bar for population intensity
cbar = plt.colorbar()
cbar.set_label('Normalized Population (Color Intensity)', fontsize=12)

highlight_countries = ['Ireland']

for country in highlight_countries:
    country_data = data_2002[data_2002['country'] == country]
    plt.scatter(country_data['gdpPercap'], country_data['lifeExp'], 
                color='red', s=300, edgecolor='black', label=country)
    
    plt.text(country_data['gdpPercap']+200, country_data['lifeExp'], country, fontsize=10, weight='bold')

top_3_population = data_2002.nlargest(3, 'pop')

for idx, row in top_3_population.iterrows():
    plt.text(row['gdpPercap'] + 200, row['lifeExp'], row['country'], fontsize=15, weight='bold')

plt.title('GDP Per Capita vs Life Expectancy (2002) - Population Encoded by Color Intensity', fontsize=16, fontweight='bold')
plt.xlabel('GDP per Capita (in USD)', fontsize=16, fontweight='bold', color='darkred', fontstyle='italic', labelpad=15)
plt.ylabel('Life Expectancy (years)', fontsize=16, fontweight='bold', color='purple', rotation=90, labelpad=25)

plt.xlim(0, 50000) 

income_levels = [1000, 12000, 30000, 60000]  
for income in income_levels:
    plt.axvline(x=income, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)  

plt.text(1000, 38, 'Level 1', fontsize=10, alpha=0.8, rotation=90, verticalalignment='bottom')
plt.text(12000, 38, 'Level 2', fontsize=10, alpha=0.8, rotation=90, verticalalignment='bottom')
plt.text(30000, 38, 'Level 3', fontsize=10, alpha=0.8, rotation=90, verticalalignment='bottom')

legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Africa', markerfacecolor='blue', markersize=12),
    Line2D([0], [0], marker='s', color='w', label='Americas', markerfacecolor='blue', markersize=12),
    Line2D([0], [0], marker='D', color='w', label='Asia', markerfacecolor='blue', markersize=12),
    Line2D([0], [0], marker='^', color='w', label='Europe', markerfacecolor='blue', markersize=12),
    Line2D([0], [0], marker='X', color='w', label='Oceania', markerfacecolor='blue', markersize=12),
    Line2D([0], [0], marker='o', color='w', label='Ireland', markerfacecolor='red', markersize=12, markeredgecolor='black')
]

plt.legend(handles=legend_elements, title='Legend', title_fontsize='13', loc='lower right', fontsize=10)

plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.show()
