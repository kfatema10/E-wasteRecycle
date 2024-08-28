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
plt.figure(figsize=(10, 9))
sns.heatmap(df, annot=True, fmt='.1f', cmap='YlGnBu', linewidths=.5,
            cbar_kws={'label': 'Concentration (ppm)', 'labelsize': 14},
            annot_kws={'size': 14})  # Increase the size of the annotations here
plt.title('Elemental Concentration in Different Sources of PCB (ppm)',
          fontdict={'fontsize': 16, 'fontweight': 'bold'})
plt.xlabel('Source', fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.ylabel('Element', fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.xticks(rotation=0, ha='center', fontsize = 13)
plt.yticks(rotation=0, fontsize = 13)

plt.tight_layout()
plt.show()


# # ----- percent of highest 5 elements
# import pandas as pd
#
# # Data from the heatmap
# data = {
#     "Element": ["Ag", "Al", "As", "Au", "Be", "Bi", "Cd", "Cr", "Cu", "Fe", "Hg", "Ni", "Pb", "Pd", "Pt", "Rh", "Sb", "Sn", "Zn"],
#     "Routers": [1213.0, 54433.0, 70.0, 199.0, 0.3, 98.3, 0.6, 474.0, 216333.0, 50500.0, 0.4, 4637.0, 3413.0, 19.5, 0.5, 1.5, 2113.0, 35200.0, 8690.0],
#     "Mobile Phones": [2640.0, 19068.0, 93.3, 1051.0, 98.7, 39.6, 0.2, 865.0, 342667.0, 6810.0, 0.6, 11600.0, 3747.0, 119.0, 4.3, 5.7, 543.0, 19267.0, 5483.0],
#     "Smart Phones": [2773.0, 17800.0, 141.0, 1083.0, 115.0, 60.6, 0.2, 1219.0, 395000.0, 8793.0, 0.3, 15433.0, 260.0, 55.4, 0.8, 8.5, 30.4, 32200.0, 6667.0]
# }
#
# # Creating DataFrame
# df = pd.DataFrame(data)
# # Calculating total concentration for each source
# total_concentration = df[['Routers', 'Mobile Phones', 'Smart Phones']].sum()
#
# # Finding top 5 elements by concentration for each source
# top_elements_routers = df.nlargest(5, 'Routers')
# top_elements_mobile = df.nlargest(5, 'Mobile Phones')
# top_elements_smart = df.nlargest(5, 'Smart Phones')
#
# # Calculating the percentage of these top 5 elements
# top_elements_routers['Percentage_Routers'] = (top_elements_routers['Routers'] / total_concentration['Routers']) * 100
# top_elements_mobile['Percentage_Mobile_Phones'] = (top_elements_mobile['Mobile Phones'] / total_concentration['Mobile Phones']) * 100
# top_elements_smart['Percentage_Smart_Phones'] = (top_elements_smart['Smart Phones'] / total_concentration['Smart Phones']) * 100
#
# top_elements_routers[['Element', 'Percentage_Routers']], top_elements_mobile[['Element', 'Percentage_Mobile_Phones']], top_elements_smart[['Element', 'Percentage_Smart_Phones']]
#
# print('top_routers: \n', top_elements_routers, '\n')
# print('top_mobile: \n', top_elements_mobile, '\n')
# print('top_smart: \n', top_elements_smart)