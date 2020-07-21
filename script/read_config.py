import csv
import os
import sys

class ReadConfig:
    def __init__(self, path):
        try:
            if os.path.isfile(path) is False:
                raise OSError(2, 'No such file or directory', path)

            self.config_path = path
        except OSError as err:
            print(err)

    def config_read(self):
        with open(self.config_path) as f:
            read_line = csv.reader(f)
            config_dict = {line[0]:line[1] for line in read_line}
        return config_dict

    @staticmethod
    def figure_config_validate(config_dict):
        valid_dict={k:None for k in config_dict.keys()}
        try:
            valid_dict["figsize_w"] = float(config_dict["figsize_w"])
            valid_dict["figsize_h"] = float(config_dict["figsize_h"])
            valid_dict["dpi"] = int(config_dict["dpi"])
            valid_dict["facecolor"] = str(config_dict["facecolor"])
            valid_dict["linewidth"] = int(config_dict["linewidth"])
            valid_dict["edgecolor"] = str(config_dict["edgecolor"])
            valid_dict["tight_layout"] = bool(config_dict["tight_layout"])
            valid_dict["constrained_layout"] = bool(config_dict["constrained_layout"])

            if "figsize_w" in valid_dict and "figsize_h" in valid_dict:
                valid_dict["figsize"] = (valid_dict["figsize_w"],valid_dict["figsize_h"])

        except Exception as e:
            print(e)
        return valid_dict

    @staticmethod
    def axies_config_validate(config_dict):
        valid_dict={k:None for k in config_dict.keys()}
        try:
            valid_dict["xlabel"] = str(config_dict["xlabel"])
            valid_dict["ylabel"] = str(config_dict["ylabel"])
            valid_dict["title"] = str(config_dict["title"])
            valid_dict["set_xscale"] = str(config_dict["set_xscale"])
            valid_dict["marker"] = str(config_dict["marker"])
            valid_dict["ticker"] = str(config_dict["ticker"])
        except Exception as e:
            print(e)

        return valid_dict

if __name__ == "__main__":
    figure_config_path = "./config/figure_config_template.csv"

    figure_config = ReadConfig(figure_config_path)
    figure_csv = figure_config.config_read()
    figure_dict = ReadConfig.figure_config_validate(figure_csv)
    print(figure_dict)

    axies_config_path = "./config/axies_config_template.csv"
    axies_config = ReadConfig(axies_config_path)
    axies_csv = axies_config.config_read()
    axies_dict = ReadConfig.axies_config_validate(axies_csv)
    print(axies_dict)
