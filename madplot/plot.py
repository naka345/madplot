import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import math
import os.path


class Plot:
    def __init__(self, read_yaml, rcParams_dict):
        self.figure_config = read_yaml
        self.rcParams = rcParams_dict
        self.file_count = 0

    @staticmethod
    def read_csv(path):
        return pd.read_csv(path, header=0, index_col=0)

    @staticmethod
    def std_err_df(df_dict):
        df_list = [df for df in df_dict.values()]
        append_dict = {index: {} for index, df in df_list[0].iterrows()}

        for i, df in enumerate(df_list):
            for index, series in df.iterrows():
                append_dict[index].update({str(i): series})

        key_concat = {
            index: pd.DataFrame(index_series_list).T
            for index, index_series_list in append_dict.items()
        }
        std_err_dict = {
            key: (concat_df.std(ddof=False) / math.sqrt(len(concat_df)))
            for key, concat_df in key_concat.items()
        }
        std_err_df = pd.DataFrame(std_err_dict)
        return std_err_df

    def init_figure(self):
        plt.style.use(self.rcParams)
        plt_option = self.figure_config["figure"]
        self.fig = plt.figure(**plt_option)

    def get_line_option(self):
        return self.figure_config["lines"]

    def get_legend_option(self):
        return self.figure_config["legend"]

    def get_errbar_option(self, std_err_df):
        errbar_config = {"yerr": std_err_df}
        if "errbar" in self.figure_config:
            errbar_config = {**errbar_config, **self.figure_config["errbar"]}
        return errbar_config

    def set_axes_config(self, **kargs):
        axes_config = self.figure_config["axes"]
        if "title" in kargs and axes_config["title"]["specific"] is False:
            self.csv_title = kargs["title"]
            self.ax.set_title(self.csv_title)
        else:
            self.ax.set_title(axes_config["title"]["name"])

        self.format_scale(axes_config["scale"])

    def format_scale(self, scale_config):
        for config_key in scale_config.keys():
            if not "scale" in config_key:
                continue
            if scale_config[config_key] == "same":
                continue

            scale_type = scale_config[config_key]
            eval(f"self.ax.set_{config_key}")(scale_type)

            if scale_config[config_key] == "log":
                formatter = eval(f'ticker.{scale_config["ticker"]}')()
                eval(f"self.ax.get_{config_key[0]}axis().set_major_formatter")(
                    formatter
                )

    def set_label_name(self):
        axis_config = self.figure_config["axis"]
        self.ax.set_xlabel(axis_config["xlabel"])
        self.ax.set_ylabel(axis_config["ylabel"])

    def main_df_plot(self, csv_df, std_err_df=None):
        self.ax = self.fig.add_subplot(1, 1, 1)

        errbar_option = (
            self.get_errbar_option(std_err_df) if std_err_df is not None else {}
        )
        legend_option = self.get_legend_option()
        get_line_option = self.get_line_option()

        karg_option = {**errbar_option, **legend_option, **get_line_option}
        ax_subplot = csv_df.plot(ax=self.ax, **karg_option)

        return ax_subplot

    def remove_axes(self, ax):
        self.fig.delaxes(ax)

    def figure_save(self, path=None):
        output_dir = self.figure_config["output"]["dir"]
        ext = self.figure_config["output"]["extension"]
        exec_abs_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

        if path is not None:
            self.fig.savefig(path)
        elif self.figure_config["output"]["title"]["specific"] is False and hasattr(
            self, "csv_title"
        ):
            file_name = f"{self.csv_title}.{ext}"
            file_path = os.path.join(exec_abs_path, output_dir, file_name)
            self.fig.savefig(file_path)
        else:
            file_name = self.figure_config["output"]["title"]["filename"]
            if self.file_count == 0:
                file_name = f"{file_name}.{ext}"
                file_path = os.path.join(exec_abs_path, output_dir, file_name)
            else:
                file_name = f"{file_name}_{self.file_count}.{ext}"
                file_path = os.path.join(exec_abs_path, output_dir, file_name)
            self.fig.savefig(file_path)
            self.file_count += 1

    def figure_show(self):
        self.fig.show()
