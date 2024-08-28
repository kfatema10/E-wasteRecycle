import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ["China", "USA", "India", "Japan", "Brazil", "Others", "Bangladesh"]
global_e_waste_percent = [19.46, 11.59, 6.67, 4.25, 3.94, 52.74, 1.34]
population_percent = [17.76, 4.19, 17.82, 1.57, 2.70, 53.80, 2.15]
e_waste_per_person = [8.55, 21.59, 2.92, 21.10, 11.36, 7.65, 4.85]

# Specified colors
colors = ['#ffb3ba', '#ffd2b3', '#fff68f',
          '#baffb3', '#bae1ff', '#2acaea',
          '#ba1eff']

# Setting font to Times New Roman
plt.rcParams["font.family"] = "Times New Roman"

# Creating subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 8))

# Width of each bar
bar_width = 1.0

# Plotting Global E-Waste Percent
axs[0].bar(countries, global_e_waste_percent, width=bar_width, color=colors)
axs[0].set_title('Global e-waste generation', fontsize=16, weight='bold')
axs[0].set_xlabel('Countries', fontsize=16)
axs[0].set_ylabel('Global share in total e-waste generation (%)', fontsize=16)
axs[0].set_xticklabels(countries, rotation=45, ha='right', fontsize=12)
axs[0].set_yticks(np.arange(0, 60, 5))  # Y-ticks from 0 to 55 with 5 increment

# Adding data labels
for i in range(len(countries)):
    axs[0].text(i, global_e_waste_percent[i] + 1, f'{global_e_waste_percent[i]:.2f}', ha='center', fontsize=12)

# Plotting Population Percent
axs[1].bar(countries, population_percent, width=bar_width, color=colors)
axs[1].set_title('Global share in population', fontsize=18, weight='bold')
axs[1].set_xlabel('Countries', fontsize=16)
axs[1].set_ylabel('Population (%)', fontsize=16)
axs[1].set_xticklabels(countries, rotation=45, ha='right', fontsize=12)
axs[1].set_yticks(np.arange(0, 60, 5))  # Y-ticks from 0 to 55 with 5 increment

# Adding data labels
for i in range(len(countries)):
    axs[1].text(i, population_percent[i] + 1, f'{population_percent[i]:.2f}', ha='center', fontsize=12)

# Plotting E-Waste per Person
axs[2].bar(countries, e_waste_per_person, width=bar_width, color=colors)
axs[2].set_title('E-waste generation per person', fontsize=18, weight='bold')
axs[2].set_xlabel('Countries', fontsize=16)
axs[2].set_ylabel('E-waste generation per person (kg)', fontsize=16)
axs[2].set_xticklabels(countries, rotation=45, ha='right', fontsize=12)
axs[2].set_yticks(np.arange(0, 30, 5))  # Y-ticks from 0 to 25 with 5 increment

# Adding data labels
for i in range(len(countries)):
    axs[2].text(i, e_waste_per_person[i] + 0.5, f'{e_waste_per_person[i]:.2f}', ha='center', fontsize=12)

# Adjust layout
plt.tight_layout()
plt.show()
