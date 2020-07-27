import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import math

class Plot:
    def __init__(self, read_yaml, rcParams_dict):
        self.figure_config = read_yaml
        self.rcParams = rcParams_dict

    @staticmethod
    def read_csv(path):
        return pd.read_csv(path,header=0,index_col=0)

    @staticmethod
    def std_err_df(df_list):
        append_dict={index:{} for index, df in df_list[0].iterrows()}

        for i,df in enumerate(df_list):
            for index,series in df.iterrows():
                append_dict[index].update({str(i):series})

        key_concat = {index:pd.DataFrame(index_series_list).T for index,index_series_list in append_dict.items()}
        std_err_dict = {key:(concat_df.std(ddof=False) /  math.sqrt(len(concat_df)) ) for key, concat_df in key_concat.items()}
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

    def get_errbar_option(self,std_err_df):
        errbar_config = {"yerr":std_err_df}
        if "errbar" in self.figure_config:
            errbar_config = {**errbar_config, **self.figure_config["errbar"]}
        return errbar_config

    def set_axes_config(self):
        axes_config = self.figure_config["axes"]
        print(axes_config)
        self.ax.set_title(axes_config["title"])
        self.ax.set_xscale(axes_config["scale"]["xscale"])
        self.ax.set_yscale(axes_config["scale"]["yscale"])
        log_format = eval(f'ticker.{axes_config["scale"]["ticker"]}')()
        self.ax.get_yaxis().set_major_formatter(log_format)

    def set_label_name(self):
        axis_config = self.figure_config["axis"]
        self.ax.set_xlabel(axis_config["xlabel"])
        self.ax.set_ylabel(axis_config["ylabel"])

    def main_df_plot(self, csv_df, std_err_df=None):
        self.ax = self.fig.add_subplot(1, 1, 1)

        errbar_option = self.get_errbar_option(std_err_df) if std_err_df is not None else {}
        legend_option = self.get_legend_option()
        get_line_option = self.get_line_option()

        karg_option = {**errbar_option, **legend_option, **get_line_option}
        ax_subplot = csv_df.plot(ax=self.ax,**karg_option)

        return ax_subplot

    def figure_save(self,path=None):
        if path is not None:
            self.fig.savefig(path)
        else:
            file_path = f'{self.figure_config["output"]["filename"]}.{self.figure_config["output"]["extension"]}'
            self.fig.savefig(file_path)

    def figure_show(self):
        self.fig.show()
