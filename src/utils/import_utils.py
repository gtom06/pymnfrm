import csv
import pandas as pd

INPUT_FILE_PATH = 'data/portfolioFromGSheets.csv'
OUTPUT_FILE_PATH = 'data/portfolio.csv'

def process_row(row):
    try:
        column0 = row[0]
        # Convert and round the values in column 1 and column 2
        if row[1] != '' and row[1]!= ' € -   ':
            column1 = round(float(row[1].replace('€', '').replace('.', '').replace(',', '.')), 2)
        else:
            column1 = 0
        
        column2 = round(float(row[2].replace('€ ', '').replace('.', '').replace(',', '.')), 2)
        
        # Convert and round the value in column 3 if it is not empty
        if row[3] != '':
            column3 = round(float(row[3].replace(' € ', '').replace('.', '').replace(',', '.')), 2)
        else:
            column3 = ''
        
        return column0, column1, column2, column3
    except ValueError:
        return None

def process_csv(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as csvfile, open(output_file, 'w') as output_file:
        reader = csv.reader(csvfile)
        next(reader)
        
        # Write the header to the output file
        output_file.write('date,daily_invested,contribution_value,counter_value\n')
        
        # Process each row in the input file
        for row in reader:
            processed_row = process_row(row)
            if processed_row:
                column0, column1, column2, column3 = processed_row
                # Write the processed row to the output file
                output_file.write(f'{column0},{column1},{column2},{column3}\n')

def read_csv_to_dataframe(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'], dayfirst=True)
    
    # Convert the 'counter_value' column to numeric and interpolate missing values
    df['counter_value'] = pd.to_numeric(df['counter_value'], errors='coerce')
    df['counter_value'] = df['counter_value'].interpolate()
    
    # Round all values in the DataFrame to 2 decimal places
    df = df.round(2)
    
    return df

def write_dataframe_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

def calculate_sum(df, column_name):
    return df[column_name].sum()

def execute(inputfile, outputfile):
    # Process the CSV file
    process_csv(inputfile, outputfile)

    # Read the processed CSV file into a pandas DataFrame
    df = read_csv_to_dataframe(OUTPUT_FILE_PATH)

    # Write the updated DataFrame back to the CSV file
    write_dataframe_to_csv(df, OUTPUT_FILE_PATH)

    # Calculate the sum of the 'daily_invested' column
    sum_column1 = calculate_sum(df, 'daily_invested')
    print('Sum of column[1]:', sum_column1)
