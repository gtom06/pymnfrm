import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from portfolioReader import plot_data

class TestPortfolioReader(unittest.TestCase):
    def test_plot_data(self):
        # Create a sample DataFrame for testing
        df = pd.DataFrame({
            'date': pd.date_range(start='1/1/2022', periods=100),
            'contribution_value': np.random.rand(100),
            'counter_value': np.random.rand(100)
        })
        plot_data(df)
        
if __name__ == '__main__':
    unittest.main()