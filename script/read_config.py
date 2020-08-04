import csv
import os
import sys
import yaml


class ReadConfig:
    def __init__(self, path):
        try:
            if os.path.isfile(path) is False:
                raise OSError(2, "No such file or directory", path)
        except OSError as err:
            print(err)

        self.config_path = path

    def csv_config_read(self):
        with open(self.config_path) as f:
            read_line = csv.reader(f)
            config_dict = {line[0]: line[1] for line in read_line}
        return config_dict

    def yaml_config_read(self):
        try:
            with open(self.config_path) as f:
                read_file = yaml.safe_load(f)
            return read_file
        except Exception as e:
            print(e)
            print("Please check your yaml file")

    @staticmethod
    def separate_rcParams(read_file):
        rcParams_dict = {}
        for k in read_file.keys():
            if "rcParams" in read_file[k]:
                rcParams_dict = {**rcParams_dict, **read_file[k]["rcParams"]}
                read_file[k].pop("rcParams")
        return read_file, rcParams_dict


if __name__ == "__main__":
    config_path = "./config/config.yml"
    config = ReadConfig(config_path)
    read_yaml = config.yaml_config_read()
    read_yaml, rcParams_dict = ReadConfig.separate_rcParams(read_yaml)
    print(f"read_yaml: {read_yaml}")
    print(f"rcParams_dict: {rcParams_dict}")
