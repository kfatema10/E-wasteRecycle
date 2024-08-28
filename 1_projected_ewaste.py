import matplotlib.pyplot as plt
import numpy as np

# Data (example)
years_real = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
e_waste_real = np.array([44.4, 46.4, 48.2, 50.0, 51.8, 53.6, 55.5, 57.4, 59.4, 61.0])
    # Real data for a single region in MMT

years_projected = np.array([2024, 2025, 2026, 2027, 2028, 2029, 2030])
e_waste_projected = np.array([63.3, 65.3, 67.2, 69.2, 71.1, 72.9, 74.7])
    # Projected data for a single region in MMT

# Font dictionaries
font_dict_title = {
    'family': 'Times New Roman',
    'size': 16,
    'weight': 'bold',
    'style': 'normal',
    'variant': 'normal',
    'stretch': 'normal',
    'color': 'black',
    'alpha': 1.0  # Fully opaque
}

font_dict_label = {
    'family': 'Times New Roman',
    'size': 14,
    'weight': 'bold',
    'style': 'normal',
    'variant': 'normal',
    'stretch': 'normal',
    'color': 'black',
    'alpha': 1.0  # Fully opaque
}

# Create figure and axis
plt.figure(figsize=(10, 6),dpi=300)

# Plot real data bars (up to 2023)
plt.bar(years_real, e_waste_real, color='dimgray', alpha=0.6, label='Real Data')

# Plot projected data bars (from 2024)
plt.bar(years_projected, e_waste_projected, color='lightgray', alpha=0.6, label='Projected Data')

# Label each bar with its value
for year, waste in zip(years_real, e_waste_real):
    plt.text(year, waste + 1, f'{waste:.1f}', ha='center', va='bottom',
             fontname='Times New Roman', fontsize=10)
for year, waste in zip(years_projected, e_waste_projected):
    plt.text(year, waste + 1, f'{waste:.1f}', ha='center', va='bottom',
             fontname='Times New Roman', fontsize=10)

# Title and labels
plt.title('Global Electronic Waste Generation', fontdict=font_dict_title)
plt.xlabel('Year', fontdict=font_dict_label)
plt.ylabel('E-Waste Generated (MMT)', fontdict=font_dict_label)

# Set x-axis ticks to show every year
plt.xticks(np.concatenate((years_real, years_projected)), rotation=30,
           fontname='Times New Roman', fontsize=10)

# Set y-axis ticks font to Times New Roman
plt.yticks(np.arange(0, 81, 10), fontname='Times New Roman', fontsize=10)

# Fine-tune tick parameters
plt.gca().tick_params(axis='x', which='major', labelsize=12, width=0.5, length=5, color='black')
plt.gca().tick_params(axis='y', which='major', labelsize=12, width=0.5, length=5, color='black')

# Legend with adjusted font properties
plt.legend(prop={'family': 'Times New Roman', 'size': 10})

# Display plot
plt.tight_layout()
plt.show()

