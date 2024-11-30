import matplotlib.pyplot as plt
import numpy as np

# Data for extractable copper and potential earnings
parameters_yearly = ["Extractable Cu \n(tons/year)", "Possible earnings from \nrecovered Cu \n(million BDT/year)"]
chankharpool_values_yearly = [23, 25.91]
elephant_road_values_yearly = [8, 9.39]
total_values_yearly = [31, 35.30]

# Set font to Times New Roman
plt.rcParams["font.family"] = "Times New Roman"

# Bar chart for Extractable Cu with iron solution (tons/year) and Potential Earnings (million BDT/year)
x = np.arange(len(parameters_yearly))

fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
bar_width = 0.1

# Bar chart for Chankharpool
bars1 = ax.bar(x - bar_width, chankharpool_values_yearly, bar_width,
               label='Chankharpool', color='#a7e237')

# Bar chart for Elephant Road
bars2 = ax.bar(x, elephant_road_values_yearly, bar_width,
               label='Elephant Road', color='#37bd79')

# Bar chart for Total
bars3 = ax.bar(x + bar_width, total_values_yearly, bar_width,
               label='Total', color='#0457ac')

# Add some text for labels, title, and axes ticks
ax.set_xlabel('Parameters', fontname='Times New Roman', weight='bold', fontsize=12)
ax.set_ylabel('Values', fontname='Times New Roman', weight='bold', fontsize=12)
ax.set_title('Yearly Extractable Copper and Potential Earnings',
             fontname='Times New Roman', weight='bold', fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(parameters_yearly, rotation=00, ha='center',
                   fontname='Times New Roman', weight='regular', fontsize=11)
ax.legend()
ax.set_yticks(np.arange(0, 41, 5))  # Y-ticks up to 40
ax.set_yticklabels(range(0, 45, 5), rotation=00, ha='center',
                   fontname='Times New Roman', weight='regular', fontsize=11)

# Add data labels
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontname='Times New Roman', fontsize=12)

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

plt.tight_layout()
plt.show()
