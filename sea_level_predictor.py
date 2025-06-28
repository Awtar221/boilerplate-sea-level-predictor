import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create the scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data', alpha=0.6)

    # First line of best fit: all data
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = range(1880, 2051)
    ax.plot(years1, [slope1 * year + intercept1 for year in years1], 'red', label='Best Fit: 1880–2050')

    # Second line of best fit: from year 2000 onward
    recent_df = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    years2 = range(2000, 2051)
    ax.plot(years2, [slope2 * year + intercept2 for year in years2], 'green', label='Best Fit: 2000–2050')

    # Add labels, title, legend
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.savefig('sea_level_plot.png')
    return plt.gca()