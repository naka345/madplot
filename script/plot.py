import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import math

class Plot:
    def __init__(self, figure_config, axies_config, errbar_config=None):
        self.figure_config = figure_config
        self.ticker = axies_config.pop("ticker") if "ticker" in axies_config else None
        self.axies_config = axies_config
        self.errbar_config = errbar_config

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
        self.fig = plt.figure(**self.figure_config)

    def init_axes(self):
        plt.rcParams[]

    def init_errbar(self,std_err_df):
        errbar_config = {"yerr":std_err_df}
        if self.errbar_config is not None:
            self.errbar_config = {**errbar_config, **self.errbar_config}


    def main_plot(self, csv_df, std_err_df=None):
        ax = self.fig.add_subplot(1, 1, 1)

        plot_config = self.axies_config
        if std_err_df is not None:
            self.init_errbar(std_err_df)


        print("============")
        print(plot_config)
        ax_subplot = csv_df.plot(ax=ax,**errbar_config)
        #ax_subplot.set_xscale(self.axies_config["xscale"])
        #ax_subplot.set_yscale(self.axies_config["yscale"])
        if self.ticker is not None:
            log_format = eval(f'ticker.{self.ticker}')()
            ax_subplot.get_yaxis().set_major_formatter(log_format)

        #ax_subplot.set_ylabel(self.axies_config["ylabel"])
        #ax_subplot.set_xlabel(self.axies_config["xlabel"])
        #ax_subplot.set_title(self.axies_config["title"])

    def figure_save(self,path):
        self.fig.savefig(path)

    def figure_show(self):
        self.fig.show()
