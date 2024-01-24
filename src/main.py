import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data\portfolio.csv')

    # Extract the 'contribution_value' and 'counter_value' columns
    contribution_value = df['contribution_value']
    counter_value = df['counter_value']

    # Plot the data
    plt.plot(contribution_value, label='Contribution Value')
    plt.plot(counter_value, label='Counter Value')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Contribution Value vs Counter Value')

    # Add legend
    plt.legend()

    # Set x-axis ticks
    x_ticks = np.arange(0, len(df), 50)
    x_labels = df['date'].iloc[x_ticks]
    plt.xticks(x_ticks, x_labels, rotation=90)

    # Add grid
    plt.grid(True)

    # Show the plot
    plt.show()

    # Get the clicked point
    clicked_point = plt.ginput(1)

    # Print the value of the clicked point
    if clicked_point:
        x, y = clicked_point[0]
        print(f"Clicked point: x={x}, y={y}")

if __name__ == "__main__":
    main()
