"""This code generates a donut chart visualizing the composition of 
electronic waste (e-waste) in terms of various material categories."""

import matplotlib.pyplot as plt
import numpy as np

# Data to plot
labels = ['Metals', 'Plastics', 'Metal-plastic mixture', 'Cables', 'Screens (CRT and LCD)', 'PCBs', 'Others', 'Pollutants']
sizes = [60.2, 15.21, 4.97, 1.97, 11.87, 1.71, 1.38, 2.7]
colors = ['#3399FF', '#FF9933', '#CCCCCC', '#FFFF99', '#999999', '#FF6666', '#66FF66', '#FFCC99']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice

# Set font
plt.rcParams["font.family"] = "Times New Roman"

# Plot
plt.figure(figsize=(10, 6))
wedges, texts = plt.pie(
    sizes, explode=explode, colors=colors, shadow=True, startangle=30, pctdistance=0.85
)

# Draw a circle at the center to make it look like a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Adding title
plt.title('Composition of E-waste', fontdict={'fontsize': 16, 'fontweight': 'bold'})

# Annotate with arrow
for i, (wedge, size) in enumerate(zip(wedges, sizes)):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = np.cos(np.radians(angle))
    y = np.sin(np.radians(angle))
    horizontalalignment = {-1: 'right', 1: 'left'}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(angle)
    plt.annotate(f'{labels[i]}: {size:.2f}%', xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                 horizontalalignment=horizontalalignment, arrowprops=dict(arrowstyle='->', connectionstyle=connectionstyle),
                 fontsize=12)

plt.tight_layout()
plt.show()
