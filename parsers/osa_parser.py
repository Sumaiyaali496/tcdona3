import json
import pandas as pd
import os
import traceback


class OSAJsonParser:
    def __init__(self, dirpath="", resolution=501):

        self.dirpath = dirpath
        self.resolution = resolution

    def parse(self, dirpath=""):

        if dirpath == "":
            dirpath = self.dirpath
        else:
            self.dirpath = dirpath

        num_errors = 0

        resolution_list = [f"point_{str(i)}" for i in range(1, self.resolution + 1)]
        column_list = [
            "device_name",
            "measurement_label",
            "time",
            "index",
            "uid",
            "repeat_index",
        ] + resolution_list
        self.dataframe = pd.DataFrame(columns=column_list)

        for num, filename in enumerate(os.listdir(dirpath)):

            if num % 1000 == 0:
                print("Parsed %s files" % str(num))

            with open(os.path.join(dirpath, filename)) as f:
                data = json.load(f)

            osa_reading = data["osa_reading"].rstrip("\r\n")
            osa_reading = osa_reading.split(",")

            assert self.resolution == len(
                osa_reading
            ), f"recorded number of OSA points is greater than {self.resolution}. The actual length in JSON is {len(osa_reading)}"

            try:

                dataframe = pd.DataFrame(columns=column_list)

                for key in data.keys():

                    if key != "osa_reading":
                        dataframe.loc[0, key] = data[key]
                dataframe.loc[0, resolution_list] = osa_reading
                self.dataframe = pd.concat(
                    [self.dataframe, dataframe], ignore_index=True
                )

            except Exception as e:
                print(traceback.format_exc())
                print("Error occurred at filename %s" % str(filename))
                print(e)
                num_errors += 1
        print("Total %s errors occurred" % str(num_errors))
        print("Parsed %s JSON files in folder %s" % (str(num + 1), str(dirpath)))

        return self.dataframe

    @staticmethod
    def write_csv(csv_path, dframe, fname):

        fname = str(csv_path) + str(fname) + str(".csv")
        dframe.to_csv(fname, index=True)

    def get_csv(self, json_path="", csv_path=""):

        if csv_path[-1] != "/":
            csv_path += "/"
        self.csv_path = csv_path

        print("Writing CSV files...")

        dataframe = self.parse(dirpath=json_path)

        self.write_csv(csv_path, dataframe, "osa")
