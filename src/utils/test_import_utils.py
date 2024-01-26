import unittest
from import_utils import process_row
import csv

class TestImportUtils(unittest.TestCase):
    def test_process_row(self):
        # Test case 1: Valid row with all columns filled
        row1 = ["15/11/2021"," â‚¬ 2.500,00 "," â‚¬ 2.500,00 "," â‚¬ 2.500,00 "]
        expected1 = ('15/11/2021', 2500.0, 2500.0, 2500.0)
        self.assertEqual(process_row(row1), expected1)

        # Test case 2: Valid row with empty column 3
        row2 = ["15/11/2021"," â‚¬ 2.500,00 "," â‚¬ 2.500,00 ",""]
        expected2 = ('15/11/2021', 2500.0, 2500.0, '')
        self.assertEqual(process_row(row2), expected2)

        # Test case 3: Valid row with empty column 1 and column 2
        row3 = ["15/11/2021","",""," â‚¬ 2.500,00 "]
        #expected3 = ('15/11/2021', '', '', 2500.0)
        self.assertEqual(process_row(row3), None)

if __name__ == '__main__':
    unittest.main()