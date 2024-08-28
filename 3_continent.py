import ax
import matplotlib.pyplot as plt
import numpy as np

# Font dictionaries
font_dict_title = {
    'family': 'Times New Roman',
    'size': 14,
    'weight': 'bold',
    'style': 'normal',
}

font_dict_label = {
    'family': 'Times New Roman',
    'size': 12,
    'style': 'normal',
}

# Data
continents = ['Africa', 'America', 'Asia', 'Europe', 'Oceania']
total_e_waste = [2.9, 13.1, 24.9, 12, 0.7]
e_waste_per_capita = [2.5, 13.3, 5.6, 16.2, 16.1]
recycled_percentage = [0.9, 9.4, 11.7, 42.5, 8.8]

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(10, 7), dpi=300)

# Bar chart for e-waste generation
bar_width = 0.3
bar_positions = np.arange(len(continents))

bars1 = ax1.bar(bar_positions, total_e_waste, bar_width,
                label='Total e-waste (Mt)', color='gray', align='center')
bars2 = ax1.bar(bar_positions + bar_width, e_waste_per_capita, bar_width,
                label='E-waste per capita (kg)', color='lightgray', align='center')

# Attach labels on top of the bars
# for bar1, bar2 in zip(bars1, bars2):
#     ax1.text(bar1.get_x() + bar1.get_width() / 2, bar1.get_height(), f'{bar1.get_height()}',
#             ha='center', va='bottom', fontsize=10, )
#     ax1.text(bar2.get_x() + bar2.get_width() / 2, bar2.get_height(), f'{bar2.get_height()}',
#             ha='center', va='bottom', fontsize=10)

# Attach labels on top of the bars
for bar1, bar2 in zip(bars1, bars2):
    ax1.text(bar1.get_x() + bar1.get_width() / 2, bar1.get_height(), f'{bar1.get_height()}',
            ha='center', va='bottom', fontsize=10, fontname='Times New Roman')
    ax1.text(bar2.get_x() + bar2.get_width() / 2, bar2.get_height(), f'{bar2.get_height()}',
            ha='center', va='bottom', fontsize=10, fontname='Times New Roman')

# Adding a second Y-axis for the recycling percentage
ax2 = ax1.twinx()
line = ax2.plot(bar_positions + bar_width / 2, recycled_percentage,
                label='Recycled e-waste (%)', color='black', marker='o')

# Add data labels for recycled_percentage
for i, txt in enumerate(recycled_percentage):
    ax2.annotate(f'{txt}%', (bar_positions[i] + bar_width / 2, recycled_percentage[i]),
                 textcoords="offset points", xytext=(-15,5), ha='center',
                 fontsize=10, fontname='Times New Roman')

# Labels and Title
ax1.set_xlabel('Continent', fontdict=font_dict_label, weight='bold')
ax1.set_ylabel('E-waste generation (Mt)', fontdict=font_dict_label, weight='bold')
ax2.set_ylabel('Recycled e-waste (%)', fontdict=font_dict_label, weight='bold')
plt.title('E-waste generation by continent', fontdict=font_dict_title)

# Customize ticks
ax1.set_xticks(bar_positions + bar_width / 2,)
ax1.set_xticklabels(continents, fontdict=font_dict_label)

ax1.set_yticks(np.arange(0, 35, 5))
ax1.set_yticklabels(np.arange(0, 35, 5), fontdict={'family': 'Times New Roman', 'size': 12})

ax2.set_yticks(np.arange(0, 60, 10))
ax2.set_yticklabels(np.arange(0, 60, 10), fontdict={'family': 'Times New Roman', 'size': 12})

ax1.tick_params(axis='both', which='major', labelsize=12, )
ax2.tick_params(axis='y', which='major', labelsize=12)

# Set y-ticks limits
ax1.set_ylim(0, 30)
ax2.set_ylim(0, 50)

# Add the legends to the plot
ax1.legend(loc='upper left', prop={'family': 'Times New Roman', 'size': 11})
ax2.legend(loc='upper right', prop={'family': 'Times New Roman', 'size': 11})

plt.tight_layout()
plt.show()
