import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('gapminder.csv')

data_time_range = data[(data['year'] >= 1957) & (data['year'] <= 2007)]

ireland_data_time = data_time_range[data_time_range['country'] == 'Ireland']

plt.figure(figsize=(8, 6))

# Using shape encoding for continent 
sns.lineplot(x='year', y='lifeExp', style='continent', markers=True, dashes=False, data=data_time_range, ci=None)

plt.plot(ireland_data_time['year'], ireland_data_time['lifeExp'], color='red', linewidth=3, label='Ireland')

plt.title('Life Expectancy Over Time (1957-2007) - Continent Encoded by Shape', fontsize=16)
plt.xlabel('Year', fontsize=14, color='darkgreen')
plt.ylabel('Life Expectancy', fontsize=14, color='purple')

plt.legend()

plt.show()
