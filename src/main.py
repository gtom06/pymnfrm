import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Read the CSV file
    df = pd.read_csv('data\portfolio.csv')
    
    # Extract the 'contribution_value' and 'counter_value' columns
    contribution_value = df['contribution_value']
    counter_value = df['counter_value']
    
    # Plot the data
    plt.plot(contribution_value, label='Contribution Value')
    plt.plot(counter_value, label='Counter Value')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Contribution Value vs Counter Value')
    plt.legend()
    
    # Set custom x-axis ticks and labels
    x_ticks = np.arange(0, len(df), 50)
    x_labels = df['date'].iloc[x_ticks]
    plt.xticks(x_ticks, x_labels, rotation=90)
    
    # Enable grid lines
    plt.grid(True)
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
