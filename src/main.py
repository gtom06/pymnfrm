from portfolioReader import plot_data, readcsv
def main():
    # Read the CSV file
    df = readcsv()
    # Call the plot_data function
    plot_data(df)
if __name__ == "__main__":
    main()
