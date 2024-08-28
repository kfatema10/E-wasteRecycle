import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Font properties
font_props_title = FontProperties(family='Times New Roman', size=18, weight='bold')
font_props_label = FontProperties(family='Times New Roman', size=14,)

# Data to plot
labels = ['Ship Breaking Yards', 'CFL and Mercury Bulbs', 'Television, Computers and Mobile', 'Medical Waste']
sizes = [2.5, 0.0090, 0.1820, 0.0019]
colors = ['#ff9999','#66b3ff','#99ff99','#35031f']

explode = [0.1, 0.1, 0.3, 0.5]  # Explode the slices to create gaps

# Create a pie chart
plt.figure(figsize=(10, 6))
wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, startangle=200, counterclock=False,
                                   autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.2, explode=explode)

# Set font properties for labels
for text in texts:
    text.set_fontproperties(font_props_label)
    text.set_color('black')

# Set font properties for annotations
for autotext in autotexts:
    autotext.set_fontproperties(font_props_label)
    autotext.set_color('black')

# Set the title with Times New Roman font
plt.title('Source of e-waste in Bangladesh', fontproperties=font_props_title)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()
