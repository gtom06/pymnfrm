import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_data(df):
    # Extract the 'contribution_value' and 'counter_value' columns
    contribution_value = df['contribution_value']
    counter_value = df['counter_value']
    
    # Create a figure object and set the title
    fig = plt.figure("Portfolio Performance")
    fig.suptitle('Contribution Value vs Counter Value')
    
    # Plot the data
    plt.plot(contribution_value, label='Contribution Value', color='red')
    plt.plot(counter_value, label='Counter Value', color='blue')
    
    # Fit a polynomial regression model to the data points for contribution_value
    degree = 64  # Degree of the polynomial (1 for linear regression)
    coeffs = np.polyfit(range(len(df)), contribution_value, degree)
    trend_line_contribution = np.polyval(coeffs, range(len(df)))
    
    # Fit a polynomial regression model to the data points for counter_value
    coeffs = np.polyfit(range(len(df)), counter_value, degree)
    trend_line_counter = np.polyval(coeffs, range(len(df)))
    
    # Plot the trend lines
    plt.plot(trend_line_contribution, label='_nolegend_', linestyle='dotted', color='red')
    plt.plot(trend_line_counter, label='_nolegend_', linestyle='dotted', color='blue')
    
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    
    # Set custom x-axis ticks and labels
    x_ticks = np.arange(0, len(df), 50)
    x_labels = df['date'].iloc[x_ticks]
    plt.xticks(x_ticks, x_labels, rotation=45)
    
    # Enable grid lines
    plt.grid(True)
    
    # Display the plot
    plt.show()

def readcsv(csv_file_path = 'data/portfolio.csv'):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    return df