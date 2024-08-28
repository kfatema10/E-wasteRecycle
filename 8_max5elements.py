import pandas as pd
import matplotlib.pyplot as plt

# Data from the heatmap
data = {
    "Element": ["Ag", "Al", "As", "Au", "Be", "Bi", "Cd", "Cr", "Cu", "Fe", "Hg", "Ni", "Pb", "Pd", "Pt", "Rh", "Sb", "Sn", "Zn"],
    "Routers": [1213.0, 54433.0, 70.0, 199.0, 0.3, 98.3, 0.6, 474.0, 216333.0, 50500.0, 0.4, 4637.0, 3413.0, 19.5, 0.5, 1.5, 2113.0, 35200.0, 8690.0],
    "Mobile Phones": [2640.0, 19068.0, 93.3, 1051.0, 98.7, 39.6, 0.2, 865.0, 342667.0, 6810.0, 0.6, 11600.0, 3747.0, 119.0, 4.3, 5.7, 543.0, 19267.0, 5483.0],
    "Smart Phones": [2773.0, 17800.0, 141.0, 1083.0, 115.0, 60.6, 0.2, 1219.0, 395000.0, 8793.0, 0.3, 15433.0, 260.0, 55.4, 0.8, 8.5, 30.4, 32200.0, 6667.0]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Calculating total concentration for each source
total_concentration = df[['Routers', 'Mobile Phones', 'Smart Phones']].sum()

# Finding top 5 elements by concentration for each source
top_elements_routers = df.nlargest(5, 'Routers')
top_elements_mobile = df.nlargest(5, 'Mobile Phones')
top_elements_smart = df.nlargest(5, 'Smart Phones')

# Calculating the percentage of these top 5 elements
top_elements_routers['Percentage_Routers'] = (top_elements_routers['Routers'] / total_concentration['Routers']) * 100
top_elements_mobile['Percentage_Mobile_Phones'] = (top_elements_mobile['Mobile Phones'] / total_concentration['Mobile Phones']) * 100
top_elements_smart['Percentage_Smart_Phones'] = (top_elements_smart['Smart Phones'] / total_concentration['Smart Phones']) * 100

# Calculate the 'Others' category by subtracting the sum of the top 5 elements' percentages from 100%
others_routers = 100 - top_elements_routers['Percentage_Routers'].sum()
others_mobile = 100 - top_elements_mobile['Percentage_Mobile_Phones'].sum()
others_smart = 100 - top_elements_smart['Percentage_Smart_Phones'].sum()

# Create a DataFrame for 'Others'
others_df_routers = pd.DataFrame({'Element': ['Others'], 'Percentage_Routers': [others_routers]})
others_df_mobile = pd.DataFrame({'Element': ['Others'], 'Percentage_Mobile_Phones': [others_mobile]})
others_df_smart = pd.DataFrame({'Element': ['Others'], 'Percentage_Smart_Phones': [others_smart]})

# Concatenate the top elements DataFrame with the 'Others' DataFrame
top_elements_routers_final = pd.concat([top_elements_routers[['Element', 'Percentage_Routers']], others_df_routers], ignore_index=True)
top_elements_mobile_final = pd.concat([top_elements_mobile[['Element', 'Percentage_Mobile_Phones']], others_df_mobile], ignore_index=True)
top_elements_smart_final = pd.concat([top_elements_smart[['Element', 'Percentage_Smart_Phones']], others_df_smart], ignore_index=True)

# Preparing data for plotting
elements_routers = top_elements_routers_final['Element']
percentages_routers = top_elements_routers_final['Percentage_Routers']

elements_mobile = top_elements_mobile_final['Element']
percentages_mobile = top_elements_mobile_final['Percentage_Mobile_Phones']

elements_smart = top_elements_smart_final['Element']
percentages_smart = top_elements_smart_final['Percentage_Smart_Phones']

# Define colors for elements
colors_routers = ['#964B00', '#C0C0C0', '#5e626b', '#DADBDD', '#202020', '#519DE9']
colors_mobile = ['#964B00', '#DADBDD', '#C0C0C0', '#fce205', '#5e626b', '#519DE9']
colors_smart = ['#964B00', '#DADBDD', '#C0C0C0', '#fce205', '#5e626b', '#519DE9']

# Set font
plt.rcParams["font.family"] = "Times New Roman"

# Creating subplots
fig, ax = plt.subplots(1, 3, figsize=(9, 5), sharey=True)

# Plot for Routers
bars_routers = ax[0].bar(elements_routers, percentages_routers, width = 1, color=colors_routers)
ax[0].set_title('Routers', fontdict={'fontsize': 16, 'fontweight': 'bold'})
ax[0].set_ylabel('Percentage (%)', fontdict={'fontsize': 14, 'fontweight': 'bold'})
ax[0].set_xlabel('Elements', fontdict={'fontsize': 14, 'fontweight': 'bold'})
# Adding data labels for Routers
for bar in bars_routers:
    height = bar.get_height()
    ax[0].text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}%', ha='center', va='bottom', fontsize=10)

# Plot for Mobile Phones
bars_mobile = ax[1].bar(elements_mobile, percentages_mobile, color=colors_mobile, width = 1)
ax[1].set_title('Mobile Phones', fontdict={'fontsize': 16, 'fontweight': 'bold'})
ax[1].set_xlabel('Elements', fontdict={'fontsize': 14, 'fontweight': 'bold'})
# Adding data labels for Mobile Phones
for bar in bars_mobile:
    height = bar.get_height()
    ax[1].text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}%', ha='center', va='bottom', fontsize=10)

# Plot for Smart Phones
bars_smart = ax[2].bar(elements_smart, percentages_smart, color=colors_smart, width = 1)
ax[2].set_title('Smart Phones', fontdict={'fontsize': 16, 'fontweight': 'bold'})
ax[2].set_xlabel('Elements', fontdict={'fontsize': 14, 'fontweight': 'bold'})
# Adding data labels for Smart Phones
for bar in bars_smart:
    height = bar.get_height()
    ax[2].text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}%', ha='center', va='bottom', fontsize=10)

# Adjust layout to remove space between columns
plt.tight_layout(pad=2.0)

plt.show()
