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
    def config_validate(config_dict):
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

if __name__ == "__main__":
    path = "../config/figure_config.csv"
    rc = ReadConfig(path)
    dict_csv = rc.config_read()
    val_dict = ReadConfig.config_validate(dict_csv)
    print(val_dict)
