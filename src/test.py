import unittest
import pandas as pd
import random
from portfolioReader import plot_data
from utils.import_utils import process_csv, process_row
class TestPortfolioReader(unittest.TestCase):
    def test_plot_data(self):
        # Create a sample DataFrame for testing
        df = pd.DataFrame({
            'date': pd.date_range(start='1/1/2022', periods=100),
            'contribution_value': random.uniform(0.0, 1.0),
            'counter_value': random.uniform(0.0, 1.0)
        })
        plot_data(df)
class TestImportUtils(unittest.TestCase):
    def test_process_row(self):
        # Test case 1: Valid row with all values
        row1 = ["15/11/2021"," â‚¬ 2.500,00 "," â‚¬ 2.500,00 "," â‚¬ 2.500,00 "]
        expected1 = ('15/11/2021', 2500.0, 2500.0, 2500.0)
        self.assertEqual(process_row(row1), expected1)

        # Test case 2: Valid row with empty values
        row2 = ["15/11/2021","","",""]
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
        # Add assertions to validate the output file contents
        
if __name__ == '__main__':
    unittest.main()