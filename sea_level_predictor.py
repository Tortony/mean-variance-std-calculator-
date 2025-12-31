import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5)
    
    # First line of best fit (all data)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create array of years from 1880 to 2050
    years_extended1 = np.arange(1880, 2051)
    # Predict sea levels
    sea_levels_pred1 = intercept1 + slope1 * years_extended1
    
    # Plot first line
    plt.plot(years_extended1, sea_levels_pred1, 'r', label='Best Fit Line 1880-2013')
    
    # Second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create array of years from 2000 to 2050
    years_extended2 = np.arange(2000, 2051)
    # Predict sea levels
    sea_levels_pred2 = intercept2 + slope2 * years_extended2
    
    # Plot second line
    plt.plot(years_extended2, sea_levels_pred2, 'green', label='Best Fit Line 2000-2013')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Test the function
if __name__ == "__main__":
    draw_plot()
    plt.show()
