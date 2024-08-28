import matplotlib.pyplot as plt

# Data from the table
countries = ["China", "USA", "India", "Japan", "Brazil", "Others", "Bangladesh"]
e_waste_percent = [19.46, 11.59, 6.67, 4.25, 3.94, 52.74, 1.34]

colors = ['#99ff99','#66b3ff','#ffcc99', '#ff9999',
          '#FBE29F', '#9BBFE0', '#E8A09A']

# Explode the Bangladesh slice
explode = [0, 0, 0, 0, 0, 0, 0.1]  # Only "explode" the last slice

# Create a pie chart
plt.figure(figsize=(10, 8), dpi=300)
plt.pie(e_waste_percent, labels=countries, autopct='%1.1f%%', colors=colors,
        startangle=10, explode=explode,
        textprops={'fontsize': 12, 'family': 'Times New Roman'})

# Add the title with space
plt.title('Bangladesh in global e-waste generation in 2022\n', fontsize=14,
          family='Times New Roman', weight='bold')

# Adjust the layout to add space below the title
plt.subplots_adjust(top=0.8)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Drawing a white circle at the center to create a ring/donut chart
center_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

plt.show()
