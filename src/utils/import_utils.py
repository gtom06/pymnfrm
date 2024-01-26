import csv
import pandas as pd

# Open the input CSV file and create the output CSV file
with open('data\portfolioFromGSheets.csv', newline='') as csvfile, open('data\portfolio.csv', 'w') as output_file:
    reader = csv.reader(csvfile)
    next(reader)
    
    # Write the header to the output file
    output_file.write('date,daily_invested,contribution_value,counter_value\n')
    
    # Process each row in the input file
    for row in reader:
        try:
            column0 = row[0]
            
            # Convert and round the values in column 1 and column 2
            if row[1] != '' and row[1]!= ' â‚¬ -   ':
                column1 = round(float(row[1].replace(' â‚¬ ', '').replace('.', '').replace(',', '.')), 2)
            else:
                column1 = 0
            
            column2 = round(float(row[2].replace('â‚¬ ', '').replace('.', '').replace(',', '.')), 2)
            
            # Convert and round the value in column 3 if it is not empty
            if row[3] != '':
                column3 = round(float(row[3].replace(' â‚¬ ', '').replace('.', '').replace(',', '.')), 2)
            else:
                column3 = ''
            
            # Write the processed row to the output file
            output_file.write(f'{column0},{column1},{column2},{column3}\n')
        except ValueError as e:
            print('Error: ', e)

# Read the processed CSV file into a pandas DataFrame
df = pd.read_csv('data\portfolio.csv', parse_dates=['date'], dayfirst=True)

# Convert the 'counter_value' column to numeric and interpolate missing values
df['counter_value'] = pd.to_numeric(df['counter_value'], errors='coerce')
df['counter_value'] = df['counter_value'].interpolate()

# Round all values in the DataFrame to 2 decimal places
df = df.round(2)

# Write the updated DataFrame back to the CSV file
df.to_csv('data\portfolio.csv', index=False)

# Calculate the sum of the 'daily_invested' column
sum_column1 = df['daily_invested'].sum()
print('Sum of column[1]:', sum_column1)
