# tests/test_plotting.py
import unittest
import matplotlib.pyplot as plt

from visuals import default_plot_settings

class TestPlotting(unittest.TestCase):
    def test_default_plot_settings(self):
        default_plot_settings()
        self.assertEqual(plt.rcParams['figure.figsize'], [10, 6])

if __name__ == '__main__':
    unittest.main()