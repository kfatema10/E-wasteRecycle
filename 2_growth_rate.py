import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

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

# Defining the years for the growth rates
growth_years = np.array(range(2015, 2031))

# Annual growth rates calculated previously
annual_growth_rates = np.array([4.50, 3.88, 3.73, 3.60, 3.47, 3.54, 3.42, 3.48,
                                2.69, 3.77, 3.16, 2.91, 2.98, 2.75, 2.53, 2.47])

# Fit a polynomial of degree 3 (cubic) to the data
coefficients = np.polyfit(growth_years, annual_growth_rates, 3)
polynomial = np.poly1d(coefficients)

# Generate x values for the trendline
trendline_years = np.linspace(2015, 2030, 100)
trendline_values = polynomial(trendline_years)

# Calculate the R^2 value
predicted_growth_rates = polynomial(growth_years)
r_squared = r2_score(annual_growth_rates, predicted_growth_rates)

# Plotting the growth rates
plt.figure(figsize=(10, 6))
plt.plot(growth_years, annual_growth_rates, 'ko', label='Annual Growth Rates')
plt.plot(trendline_years, trendline_values, 'b-', label='Trendline (Cubic)')

# Adding titles and labels
plt.title('Annual Growth Rate of Global Electronic Waste Generation',
          fontdict=font_dict_title)
plt.xlabel('Year', fontdict=font_dict_label)
plt.ylabel('Annual Growth Rate (%)', fontdict=font_dict_label)

# Setting xticks and yticks
plt.xticks(np.arange(min(growth_years), max(growth_years)+1, 1),
           fontname='Times New Roman')
plt.yticks(np.arange(2.5, 4.6, 0.5), fontname='Times New Roman')

# Adding legend
plt.legend(loc='lower left')

# Adding grid
plt.grid(True)

# Show equation and R^2 value on the plot
coeff_text = [
    f"{coefficients[0]:.3g}",
    f"{coefficients[1]:.3g}",
    f"{coefficients[2]:.6g}",
    f"{coefficients[3]:.3g}"
]

equation_text = (r'$y = {}x^3 + {}x^2 + {}x + {}$' + '\n' + r'$R^2 = {:.4f}$').format(
    coeff_text[0], coeff_text[1], coeff_text[2], coeff_text[3], r_squared
)

# Display the equation and R^2 value on the top right corner of the plot
plt.text(2018, max(annual_growth_rates) * 1, equation_text,
         fontdict = font_dict_label, color='black', ha='left', va='top')

# Display the plot
plt.show()
