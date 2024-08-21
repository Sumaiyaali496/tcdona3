import json
import pandas as pd
import os
import traceback


class PolatisJsonParser:
    def __init__(self, dirpath=""):

        self.dirpath = dirpath

    @staticmethod
    def unroll_dict(dict_, out={}, prefix=""):

        for key, value in dict_.items():
            if isinstance(value, dict):
                PolatisJsonParser.unroll_dict(value, out, key)
            else:
                if prefix == "":
                    out[key] = value
                else:
                    out[str(prefix) + "_" + key] = value

        return out

    @staticmethod
    def init_dframe_component():

        return pd.DataFrame(
            columns=[
                "type",
                "local_port",
                "location",
                "input_port",
                "input_power",
                "input_patch",
                "input_shutter",
                "input_monmode",
                "input_wavelength",
                "input_offset",
                "input_atime",
                "output_port",
                "output_power",
                "output_patch",
                "output_shutter",
                "output_monmode",
                "output_wavelength",
                "output_offset",
                "output_atime",
            ]
        )

    def init_dframes(self, data):

        self.setup_dataset = pd.DataFrame(
            columns=[
                "device_name",
                "measurement_label",
                "time",
                "index",
                "uid",
                "repeat_index",
            ]
        )

        self.component_dframes = {}

        for key, value in data.items():

            if key not in self.setup_dataset.columns:
                self.component_dframes[key] = self.init_dframe_component()

    def parse(self, dirpath=""):

        if dirpath == "":
            dirpath = self.dirpath
        else:
            self.dirpath = dirpath

        num_errors = 0
        for num, filename in enumerate(os.listdir(dirpath)):

            if num % 1000 == 0:
                print("Parsed %s files" % str(num))

            with open(os.path.join(dirpath, filename)) as f:
                data = json.load(f)

            if num == 0:
                self.init_dframes(data)

            try:

                setup_dataset = pd.DataFrame(
                    columns=[
                        "device_name",
                        "measurement_label",
                        "time",
                        "index",
                        "uid",
                        "repeat_index",
                    ]
                )
                for column in self.setup_dataset.columns:
                    setup_dataset.loc[0, column] = data[column]
                self.setup_dataset = pd.concat(
                    [self.setup_dataset, setup_dataset], ignore_index=True
                )

                for component in self.component_dframes.keys():
                    dframe_ = pd.DataFrame([self.unroll_dict(data[component])])
                    self.component_dframes[component] = pd.concat(
                        [self.component_dframes[component], dframe_], ignore_index=True
                    )

            except Exception as e:
                print(traceback.format_exc())
                print("Error occurred at filename %s" % str(filename))
                print(e)
                num_errors += 1
        print("Total %s errors occurred" % str(num_errors))
        print("Parsed %s JSON files in folder %s" % (str(num + 1), str(dirpath)))

        return {"setup": self.setup_dataset, "component": self.component_dframes}

    def write_csv(self, dframe, fname):

        fname = str(self.csv_path) + str(fname) + str(".csv")
        dframe.to_csv(fname, index=True)

    def get_csv(self, json_path="", csv_path=""):

        if csv_path[-1] != "/":
            csv_path += "/"
        self.csv_path = csv_path

        print("Writing CSV files...")

        datalist = self.parse(dirpath=json_path)

        self.write_csv(datalist["setup"], "polatis_setup")

        for component, dframe in datalist["component"].items():
            self.write_csv(dframe, component)

        print("Completed... ")
