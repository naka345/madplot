import csv
import os
import sys
import glob
from script.plot import Plot
from script.read_config import ReadConfig

class Main:
    def __init__(self, path="./config/config_template.yml"):
        self.path = path

    def read_yaml_config(self):
        config = ReadConfig(self.path)
        read_yaml = config.yaml_config_read()
        self.read_config_dict, self.rcParams_dict = ReadConfig.separate_rcParams(read_yaml)

    def init_plot_configure(self):
        self.plt_class = Plot(self.read_config_dict, self.rcParams_dict)
        self.plt_class.init_figure()

    def set_data_files(self):
        file_list = self.read_config_dict["datafile"]["files"].split(",")
        file_dir = self.read_config_dict["datafile"]["filedir"]

        data_files_dict = {}
        for fl in file_list:
            if "*" in fl:
                all_file_list = glob.glob(f'{file_dir}/{fl}')
                all_file_dict = {file.split("/")[-1]:file for file in all_file_list}
                data_files_dict = {**data_files_dict, **all_file_dict}
            else:
                data_files_dict.update({fl : f'{file_dir}/{fl}'})
        return data_files_dict

if __name__ == "__main__":
    main = Main()
    main.read_yaml_config()
    main.init_plot_configure()

    files_dict = main.set_data_files()
    df_dict = {k:Plot.read_csv(v) for k,v in files_dict.items()}

    std_err = Plot.std_err_df(df_dict)

    for csv_name, df in df_dict.items():
        print("here")
        subplot_ax = main.plt_class.main_df_plot(df.T, std_err_df=std_err)
        main.plt_class.set_axes_config()
        main.plt_class.set_label_name()

        # main.plt_class.figure_show()
        main.plt_class.figure_save(f"./output/{csv_name}.png")
        main.plt_class.remove_axes(subplot_ax)
