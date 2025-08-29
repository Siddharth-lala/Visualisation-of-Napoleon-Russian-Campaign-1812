import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.lines import Line2D

# Loading dataset
data = pd.read_csv('gapminder.csv')

# Filtering dataset for year 2002
data_2002 = data[data['year'] == 2002]

# Defining custom Custom_markers for the 5 continents
Custom_markers = {'Africa': 'o', 'Americas': 's', 'Asia': 'D', 'Europe': '^', 'Oceania': 'X'}

# zooming in for better visibility
plt.figure(figsize=(12,8))  

# selecting a fixed color palette
palette = sns.color_palette('deep', 5)  # Seaborn's default deep palette
continent_palette = dict(zip(['Africa', 'Americas', 'Asia', 'Europe', 'Oceania'], palette))

# Creating the scatter plot encoding population by size
sns.scatterplot(
    x='gdpPercap', 
    y='lifeExp', 
    size='pop', 
    sizes=(50, 1000),  
    hue='continent', 
    style='continent',  # Different marker shapes for each continent
    markers=Custom_markers,
    palette=continent_palette,  
    data=data_2002,
    legend=False,  #disable auto legend
    alpha=0.8  # transparency for better visibility
)

# Highlighting Ireland
Mark_IRL = ['Ireland']

for country in Mark_IRL:
    country_data = data_2002[data_2002['country'] == country]
    plt.scatter(country_data['gdpPercap'], country_data['lifeExp'], 
                color='red', s=300, edgecolor='black', label=country)
    
    # Annotate key countries
    plt.text(country_data['gdpPercap']+200, country_data['lifeExp'], country, fontsize=10, weight='bold')

# Finding the top 3 countries with the largest populations
top_3_population = data_2002.nlargest(3, 'pop')

# Highlighting the top 3 countries by population with bold Custom_markers and annotations 
for idx, row in top_3_population.iterrows():
    plt.scatter(row['gdpPercap'], row['lifeExp'], color='orange', s=700, edgecolor='black', label=row['country'])
    plt.text(row['gdpPercap'] + 200, row['lifeExp'], row['country'], fontsize=10, weight='bold')

# labelling
plt.title('GDP Per Capita vs Life Expectancy (2002) - Population Encoded by Size', fontsize=16, fontweight='bold')
plt.xlabel('GDP per Capita (in USD)', fontsize=16, fontweight='bold', color='darkred', fontstyle='italic', labelpad=15)
plt.ylabel('Life Expectancy (years)', fontsize=16, fontweight='bold', color='purple', rotation=90, labelpad=25)


plt.xlim(0, 50000) 

# Adding vertical lines to divide the graph into 4 income levels (custom income range)
income_levels = [1000, 12000, 30000]  
for income in income_levels:
    plt.axvline(x=income, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)  # Light gray vertical lines

plt.text(1000, 38, 'Level 1', fontsize=10, alpha=0.8, rotation=90, verticalalignment='bottom')
plt.text(12000, 38, 'Level 2', fontsize=10, alpha=0.8, rotation=90, verticalalignment='bottom')
plt.text(30000, 38, 'Level 3', fontsize=10, alpha=0.8, rotation=90, verticalalignment='bottom')

# Creating a manual legend for continents, Ireland, and top 3 countries by population 
legend_items = [
    Line2D([0], [0], marker='o', color='w', label='Africa', markerfacecolor=continent_palette['Africa'], markersize=12),
    Line2D([0], [0], marker='s', color='w', label='Americas', markerfacecolor=continent_palette['Americas'], markersize=12),
    Line2D([0], [0], marker='D', color='w', label='Asia', markerfacecolor=continent_palette['Asia'], markersize=12),
    Line2D([0], [0], marker='^', color='w', label='Europe', markerfacecolor=continent_palette['Europe'], markersize=12),
    Line2D([0], [0], marker='X', color='w', label='Oceania', markerfacecolor=continent_palette['Oceania'], markersize=12),
    Line2D([0], [0], marker='o', color='w', label='Ireland', markerfacecolor='red', markersize=12, markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Maximum Population', markerfacecolor='orange', markersize=12, markeredgecolor='black')
]

# Adding the legend 
plt.legend(handles=legend_items, title='Legend', title_fontsize='13', loc='lower right', fontsize=10)


plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.show()
