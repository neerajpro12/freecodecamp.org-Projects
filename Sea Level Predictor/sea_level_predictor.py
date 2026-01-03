import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series(range(df['Year'].min(), 2051))
    y_pred1 = slope1 * x_pred1 + intercept1
    plt.plot(x_pred1, y_pred1, 'r', label="Best Fit Line(1880-2050)")
    plt.legend()

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = slope2 * x_pred2 + intercept2
    plt.plot(x_pred2, y_pred2, 'g', label="Best Fit Line(2000-2050)")
    plt.legend()


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()