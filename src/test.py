import csv
import os
import unittest
import pandas as pd
import random
from portfolioReader import plot_data, readcsv
from utils.import_utils import calculate_sum, process_csv, process_row, read_csv_to_dataframe, execute
class TestPortfolioReader(unittest.TestCase):
    def test_plot_data(self):
        # Create a sample DataFrame for testing
        df = pd.DataFrame(columns=['date', 'contribution_value', 'counter_value'])
        
        # Add multiple rows to the DataFrame
        for _ in range(100):
            row = {
                'date': pd.date_range(start='1/1/2022', periods=1),
                'contribution_value': random.uniform(0.0, 1.0),
                'counter_value': random.uniform(0.0, 1.0)
            }
            df = df._append(row, ignore_index=True)
        
        plot_data(df)
class TestImportUtils(unittest.TestCase):
    def test_process_row(self):
        # Test case 1: Valid row with all values
        EURO_AMOUNT = " € 2.500,00 "
        row1 = ["15/11/2021", EURO_AMOUNT, EURO_AMOUNT, EURO_AMOUNT]
        expected1 = ('15/11/2021', 2500.0, 2500.0, 2500.0)
        self.assertEqual(process_row(row1), expected1)

        # Test case 2: Valid row with empty values
        row2 = ["15/11/2021", "", "", ""]
        expected2 = None
        self.assertEqual(process_row(row2), expected2)

        # Test case 3: Valid row with special characters
        row3 = ['C', '1.000,50', '2.500,75', '3.750,25']
        expected3 = ('C', 1000.5, 2500.75, 3750.25)
        self.assertEqual(process_row(row3), expected3)

        # Test case 4: Invalid row with non-numeric values
        row4 = ['D', 'abc', 'def', 'ghi']
        self.assertIsNone(process_row(row4))
        
    def test_process_csv(self):
        # Test case 1: Valid input file with all values
        input_file1 = 'data/portfolioFromGSheets_sample.csv'
        output_file1 = 'data/test_output1.csv'
        process_csv(input_file1, output_file1)
        os.remove(output_file1)
        # Add assertions to validate the output file contents
        
    def test_read_csv_to_dataframe(self):
        # Create a sample CSV file
        csv_data = "date,counter_value\n\"2022-01-01\",10\n\"2022-01-02\",20\n\"2022-01-03\",30\n"
        file_path = "test.csv"
        with open(file_path, "w") as f:
            f.write(csv_data)
        df = read_csv_to_dataframe(file_path)
        expected_df = pd.DataFrame({
            'date': pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-03']),
            'counter_value': [10, 20, 30]
        })
        #self.assertEqual(df, expected_df)
        
        os.remove(file_path)
        
    
    def test_calculate_sum(self):
        # Create a sample DataFrame
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]
        })
        
        # Call the function under test
        result = calculate_sum(df, 'B')
        
        # Assert the expected output
        expected_result = 150
        assert result == expected_result
    
    def test_execute(self):
        csv_data = 'date,daily_invested,contribution_value,counter_value\n15/11/2021," € 2.500,00 "," € 2.500,00 "," € 2.500,00 "\n16/11/2021, € -   ," € 2.500,00 "," € 2.500,00 "\n17/11/2021," € 10,00 "," € 2.510,00 "," € 2.510,00 "'
        inputfile = 'test_input.csv'
        with open(inputfile, "w", encoding='utf-8') as f:
            f.write(csv_data)
        # Define input and output file paths for testing
        
        outputfile = 'test_output.csv'

        # Call the execute function with the test file paths
        execute(inputfile, outputfile)
        os.remove(inputfile)
        os.remove(outputfile)

    def test_red_csv(self):
        csv_data = 'date,daily_invested,contribution_value,counter_value\n15/11/2021," € 2.500,00 "," € 2.500,00 "," € 2.500,00 "\n16/11/2021, € -   ," € 2.500,00 "," € 2.500,00 "\n17/11/2021," € 10,00 "," € 2.510,00 "," € 2.510,00 "'
        inputfile = 'test_input.csv'
        with open(inputfile, "w", encoding='utf-8') as f:
            f.write(csv_data)
        readcsv(csv_file_path = 'test_input.csv')
        os.remove(inputfile)
        
if __name__ == '__main__':
    unittest.main()