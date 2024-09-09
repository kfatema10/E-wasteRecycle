"""This code generates a heatmap to visualize the elemental concentration 
(in parts per million, ppm) of various elements found in different sources 
of printed circuit boards (PCBs), including routers, mobile phones, and 
smartphones."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
elements = ['Ag', 'Al', 'As', 'Au', 'Be', 'Bi', 'Cd', 'Cr', 'Cu', 'Fe', 'Hg', 'Ni', 'Pb', 'Pd', 'Pt', 'Rh', 'Sb', 'Sn', 'Zn']
data = {
    'Element': elements,
    'Routers': [1213, 54433, 70, 199, 0.3, 98.3, 0.6, 474, 216333, 50500, 0.4, 4637, 3413, 19.5, 0.5, 1.5, 2113, 35200, 8690],
    'Mobile Phones': [2640, 19068, 93.3, 1051, 98.7, 39.6, 0.2, 865, 342667, 6810, 0.6, 11600, 3747, 119, 4.3, 5.7, 543, 19267, 5483],
    'Smart Phones': [2773, 17800, 141, 1083, 115, 60.6, 0.2, 1219, 395000, 8793, 0.3, 15433, 260, 55.4, 0.8, 8.5, 30.4, 32200, 6667]
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index('Element', inplace=True)

# Set font properties for Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'

# Plot heatmap
plt.figure(figsize=(9, 9), dpi=300)
heatmap = sns.heatmap(df, annot=True, fmt='.1f', cmap='YlGnBu', linewidths=.5,
                      cbar_kws={'label': 'Concentration (ppm)'},
                      annot_kws={'size': 14})  # Increase the size of the annotations here
# heatmap.figure.axes[-1].yaxis.label.set_size(14)  # Set the font size for the colorbar label

# Set the font size and weight for the colorbar label
colorbar = heatmap.figure.axes[-1].yaxis.label
colorbar.set_size(14)
colorbar.set_weight('bold')

# Set the font size for the colorbar tick labels
colorbar_tick_labels = heatmap.figure.axes[-1].get_yticklabels()
for label in colorbar_tick_labels:
    label.set_size(12)
heatmap.figure.axes[-1].tick_params(axis='y', labelsize=12)

plt.title('Elemental Concentration in Different Sources of PCB (ppm)',
          fontdict={'fontsize': 16, 'fontweight': 'bold'})
plt.xlabel('Source', fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.ylabel('Element', fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.xticks(rotation=0, ha='center', fontsize=13)
plt.yticks(rotation=0, fontsize=13)

plt.tight_layout()
plt.show()
