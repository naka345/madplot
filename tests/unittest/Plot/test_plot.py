import pytest
import mock
from madplot.plot import Plot

class TestPlot:
    @mock.patch("pandas.read_csv")
    def test_read_csv(self,pd_read_csv):
        test_path = "/path/to/file"
        Plot.read_csv(test_path)
        pd_read_csv.assert_called_once_with("/path/to/file", header=0, index_col=0)

    def test_std_err_df(init_plot_class):
        plot = init_plot_class
        print(plot)
        pass

    def test_fix(init_plot_class):
        print(init_plot_class)
