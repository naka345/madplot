import csv
import os
import sys
import glob
import fire
from script.plot import Plot
from script.read_config import ReadConfig


class Main:
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
    DEFAULT_CONFIG_PATH = os.path.join(ROOT_PATH, "config", "config_template.yml")

    def __init__(self, path=None):
        self.path = self.DEFAULT_CONFIG_PATH if path is None else path

    def read_yaml_config(self):
        config = ReadConfig(self.path)
        read_yaml = config.yaml_config_read()
        self.read_config_dict, self.rcParams_dict = ReadConfig.separate_rcParams(
            read_yaml
        )

    def init_plot_configure(self):
        self.plt_class = Plot(self.read_config_dict, self.rcParams_dict)
        self.plt_class.init_figure()

    def set_data_files(self):
        file_list = self.read_config_dict["datafile"]["files"].split(",")
        file_dir = self.read_config_dict["datafile"]["filedir"]

        data_files_dict = {}
        for fl in file_list:
            if "*" in fl:
                all_file_list = glob.glob(os.path.join(file_dir, fl))
                all_file_dict = {file.split(os.sep)[-1]: file for file in all_file_list}
                data_files_dict = {**data_files_dict, **all_file_dict}
            else:
                data_files_dict.update({fl: os.path.join(file_dir, fl)})
        return data_files_dict


def madplot(config_path="", std_err=True):
    main = Main(path=config_path) if config_path else Main()
    main.read_yaml_config()
    main.init_plot_configure()

    files_dict = main.set_data_files()
    df_dict = {k.split(".")[0]: Plot.read_csv(v) for k, v in files_dict.items()}

    std_err = Plot.std_err_df(df_dict) if std_err else None

    for csv_name, df in df_dict.items():
        subplot_ax = main.plt_class.main_df_plot(df.T, std_err_df=std_err)
        main.plt_class.set_axes_config(title=csv_name)
        main.plt_class.set_label_name()

        # main.plt_class.figure_show()
        main.plt_class.figure_save()
        main.plt_class.remove_axes(subplot_ax)


if __name__ == "__main__":
    fire.Fire({"madplot": madplot})
