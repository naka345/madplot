import csv
import os
import sys
from script.plot import Plot
from script.read_config import ReadConfig

class Main:
    def __init__(self):
        pass

    def read_yaml_config(self, path="./config/config_template.yml"):
        config = ReadConfig(path)
        read_yaml = config.yaml_config_read()
        read_yaml, rcParams_dict = ReadConfig.separate_rcParams(read_yaml)
        return read_yaml, rcParams_dict

if __name__ == "__main__":
    main = Main()
    read_config_dict, rcParams_dict = main.read_yaml_config()

    plt_class = Plot(read_config_dict, rcParams_dict)
    plt_class.init_figure()

    file_list = ["./example_data/H6-1.csv","./example_data/H6-2.csv","./example_data/H6-3.csv"]
    df_list = [Plot.read_csv(file) for file in file_list]
    std_err = Plot.std_err_df(df_list)
    plot_df = Plot.read_csv(file_list[0])
    print("here")
    subplot_ax = plt_class.main_df_plot(plot_df.T, std_err_df=std_err)
    plt_class.set_axes_config()
    plt_class.set_label_name()

    plt_class.figure_show()
    plt_class.figure_save("./output/save.png")
