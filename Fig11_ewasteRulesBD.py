import matplotlib.pyplot as plt

# Data for the timeline
years = [2010, 2021, 2024]
events = [
    "Report on \nchild worker\nmortality due to \ne-waste (2010)",
    "Hazardous Waste \n(E-Waste)\nManagement Rules\nenacted (2021)",
    "EPR Guidelines\nannounced (2024)"
]

# Create the timeline plot
plt.figure(figsize=(12, 4))

# Add extra space around the plot
padding = 2
plt.scatter(years, [1] * len(years), color='blue', s=200, label="Key Events")
plt.hlines(y=1, xmin=min(years) - padding, xmax=max(years) + padding, color='gray', linestyle='--')

# Annotate the events
for year, event in zip(years, events):
    plt.text(year, 1.009, event, rotation=0, fontsize=13, ha='center', va='bottom', color='darkblue')

# Adjust x-axis limits for extra space
plt.xlim(min(years) - padding, max(years) + padding)

# Add labels and title
plt.yticks([])  # Remove y-axis ticks
plt.xticks(fontsize=14)
plt.xlabel("Year", fontsize=16)
plt.title("Timeline of E-Waste Regulatory Actions in Bangladesh", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
