import pytest
from madplot.plot import Plot

@pytest.fixture(scope="class", autouse=True)
def init_plot_class():
    config_dict = {"datafile": {"filedir": "example_data", "files": "*.csv"}}
    rcParams = {"figure.figsize": (6.4, 4.8), "font.family": "Arial"}
    plot = Plot(config_dict, rcParams)

    yield("test")
