import unittest

from import_utils import process_row

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
        self.assertEqual(process_row(row4), None)
if __name__ == '__main__':
    unittest.main()