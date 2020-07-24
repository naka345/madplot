import csv
import os
import sys
from script.plot import Plot
from script.read_config import ReadConfig

class Main:
    def __init__(self):
        pass

    def read_figure_config(self, path="./config/figure_config_template.csv"):
        figure_config_obj = ReadConfig(path)
        figure_csv = figure_config_obj.config_read()
        figure_config = ReadConfig.figure_config_validate(figure_csv)
        return figure_config

    def read_axies_config(self, path="./config/axies_config_template.csv"):
        axies_config_obj = ReadConfig(path)
        axies_csv = axies_config_obj.config_read()
        axies_config = ReadConfig.axies_config_validate(axies_csv)
        return axies_config

    def read_errbar_config(self, path="./config/errbar_config_template.csv"):
        errbar_config_obj = ReadConfig(path)
        errbar_csv = errbar_config_obj.config_read()
        errbar_config = ReadConfig.axies_config_validate(errbar_csv)
        return errbar_config

if __name__ == "__main__":

    main = Main()
    figure_config = main.read_figure_config()
    axies_config = main.read_axies_config()
    errbar_config = main.read_errbar_config()

    plt_class = Plot(figure_config, axies_config,errbar_config=errbar_config)
    plt_class.init_figure()

    file_list = ["./example_data/H6-1.csv","./example_data/H6-2.csv","./example_data/H6-3.csv"]
    df_list = [Plot.read_csv(file) for file in file_list]
    std_err = Plot.std_err_df(df_list)
    plot_df = Plot.read_csv(file_list[0])

    plt_class.main_plot(plot_df.T, std_err_df=std_err)
    plt_class.figure_show()
    plt_class.figure_save("./output/save.png")
