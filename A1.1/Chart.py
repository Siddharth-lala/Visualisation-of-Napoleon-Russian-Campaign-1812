import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D

# loading data from 3 modified xlsx files
book1_df = pd.read_excel('/content/Book1.xlsx')  # Book1: lonp, latp, surv, dir
book2_df = pd.read_excel('/content/Book2.xlsx')  # Book2: Lonc, Latc, City
book3_df = pd.read_excel('/content/Book3.xlsx')  # Book3: lont,Temp, Days, mon, day

# Create the plot using subplots(one for the paths, one for temperature during RetreatPoints)
fig, (p1, p2) = plt.subplots(2, 1, figsize=(8.27, 11.69), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# change the background colour of the plots
p1.set_facecolor('lightgray')
p2.set_facecolor('lightgray')

# seperate points to plot using the DIR value (AttackPoints/RetreatPoints)
AttackPoints = book1_df[book1_df['DIR'] == 'A']
RetreatPoints = book1_df[book1_df['DIR'] == 'R']

# scaling the points 
attack_size = AttackPoints['SURV'] / AttackPoints['SURV'].max() * 10  # Scale line width for AttackPoints path
RetreatPoints_size = RetreatPoints['SURV'] / RetreatPoints['SURV'].max() * 10  # Scale line width for RetreatPoints path
attack_marker_size = AttackPoints['SURV'] / AttackPoints['SURV'].max() * 400  # Scale marker size for AttackPoints day markers
RetreatPoints_marker_size = RetreatPoints['SURV'] / RetreatPoints['SURV'].max() * 400  # Scale marker size for RetreatPoints day markers


# Plot the army path for AttackPoints (green)
for i in range(len(AttackPoints) - 1):
    p1.plot([AttackPoints['LONP'].iloc[i], AttackPoints['LONP'].iloc[i + 1]], 
            [AttackPoints['LATP'].iloc[i], AttackPoints['LATP'].iloc[i + 1]], 
            color='green', linewidth=attack_size.iloc[i], label='Attack' if i == 0 else "")
    

# Plot the army path for RetreatPoints (red) 
for i in range(len(RetreatPoints) - 1):
    p1.plot([RetreatPoints['LONP'].iloc[i], RetreatPoints['LONP'].iloc[i + 1]], 
            [RetreatPoints['LATP'].iloc[i], RetreatPoints['LATP'].iloc[i + 1]], 
            color='red', linewidth=RetreatPoints_size.iloc[i] * 0.4, label='Retreat' if i == 0 else "")
    

# Plot cities as scatter points
p1.scatter(book2_df['LONC'], book2_df['LATC'], color='blue', marker='D', label='Cities')

# Add city labels
for i, row in book2_df.iterrows():
    p1.text(row['LONC'], row['LATC'], row['CITY'], fontsize=10, ha='left', va='bottom')

# Setting plot limits and labels
p1.set_xlim([24, 40])
p1.set_ylim([53, 57])
p1.set_title("Napoleon's Russian Campaign of 1812", fontsize=16)
p1.set_xlabel('Longitude')
p1.set_ylabel('Latitude')

# Adding gridlines to the plots
p1.grid(True, which='both', linestyle='--', linewidth=0.5)
p2.grid(True, which='both', linestyle='--', linewidth=0.5)

# Highlight key cities or points
highlight_city = 'Moscou' 
highlight_color = 'orange'
highlight = book2_df[book2_df['CITY'] == highlight_city]
p1.scatter(highlight['LONC'], highlight['LATC'], color=highlight_color, marker='*', s=200, zorder=5)

# Creating a custom legend
legend_elements = [Line2D([0], [0], color='green', lw=2, label='Attack'),
                   Line2D([0], [0], color='red', lw=2, label='Retreat'),
                   Line2D([0], [0], marker='D', color='blue', lw=0, label='Cities')]
p1.legend(handles=legend_elements, loc='upper left')

p2.plot(book3_df['LONT'], book3_df['TEMP'], marker='o', color='orange', linestyle='--')

# added to use only points with non-empty mon and day values
book3_df = book3_df.dropna(subset=['MON', 'DAY'])

# Creating custom label for points 
book3_df['Date_Label'] = book3_df['MON'].astype(str) + ' ' + book3_df['DAY'].astype(str)

# Annotating the temperature points with date labels
for i, row in book3_df.iterrows():
    p2.annotate(row['Date_Label'], (row['LONT'], row['TEMP']), fontsize=8, ha='right')

# Setting labels for the temperature plot
p2.set_xlabel('Longitude')
p2.set_ylabel('Temperature (°R)')
p2.set_title('Temperature During Retreat')


# displaying the plot
plt.tight_layout(pad=2)  # Adjust padding to fit all elements properly
plt.show()
