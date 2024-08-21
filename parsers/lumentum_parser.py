import json
import pandas as pd
import numpy as np
import os
import traceback


class LumentumJsonParser:
    def __init__(self, dirpath=""):

        self.dirpath = dirpath

        self.column_list = []
        for i in range(1, 96):
            self.column_list.append("channel_" + str(i))

    def init_dframes(self):

        self.mux_datalist = {}
        self.mux_datalist[
            "channel_attenuation"
        ] = mux_channel_attenuation = pd.DataFrame(columns=self.column_list)
        self.mux_datalist["open_channel_index"] = mux_open_channel_index = pd.DataFrame(
            columns=self.column_list
        )
        self.mux_datalist["input_power"] = mux_input_power = pd.DataFrame(
            columns=self.column_list
        )
        self.mux_datalist["output_power"] = mux_output_power = pd.DataFrame(
            columns=self.column_list
        )
        self.mux_datalist["ocm_power"] = mux_ocm_power = pd.DataFrame(
            columns=self.column_list
        )

        self.demux_datalist = {}
        self.demux_datalist[
            "channel_attenuation"
        ] = demux_channel_attenuation = pd.DataFrame(columns=self.column_list)
        self.demux_datalist[
            "open_channel_index"
        ] = demux_open_channel_index = pd.DataFrame(columns=self.column_list)
        self.demux_datalist["input_power"] = demux_input_power = pd.DataFrame(
            columns=self.column_list
        )
        self.demux_datalist["output_power"] = demux_output_power = pd.DataFrame(
            columns=self.column_list
        )
        self.demux_datalist["ocm_power"] = demux_ocm_power = pd.DataFrame(
            columns=self.column_list
        )

        self.port_datalist = {}
        self.port_datalist["line_port"] = line_port = pd.DataFrame(
            columns=[
                "entity-description",
                "operational-state",
                "input-power",
                "output-power",
                "outvoa-actual-attenuation",
                "measurement_label",
            ]
        )

        self.port_datalist["mux_port"] = mux_port = pd.DataFrame(
            columns=["entity-description", "operational-state", "input-power"]
        )
        self.port_datalist["demux_port"] = demux_port = pd.DataFrame(
            columns=["entity-description", "operational-state", "input-power"]
        )

        self.setup_datalist = pd.DataFrame(
            columns=[
                "uid",
                "additional_attn",
                "label",
                "num_repeat",
                "measurement_label",
                "index",
                "repeat_index",
            ]
        )

        self.preamp_params = pd.DataFrame(
            columns=[
                "control_mode",
                "maintenance-state",
                "target_power",
                "target_gain",
                "target_gain_tilt",
                "input_power",
                "output_power",
                "voa_input_power",
                "voa_output_power",
                "voa_attenuation",
                "lotee:custom-name",
                "lotee:maintenance-state",
                "lotee:control-mode",
                "lotee:gain-switch-mode",
                "lotee:target-gain",
                "lotee:target-power",
                "lotee:target-gain-tilt",
                "lotee:los-shutdown",
                "lotee:optical-loo-threshold",
                "lotee:optical-loo-hysteresis",
                "lotee:input-overload-threshold",
                "lotee:input-overload-hysteresis",
                "lotee:force-apr",
                "entity-description",
                "operational-state",
                "output-power",
                "measured-gain",
                "voa-input-power-debug",
                "voa-output-power-debug",
                "voa-attentuation-debug",
                "pump1-current",
                "pump1-tec-current",
                "pump1-tec-temperature",
                "pump2-current",
                "pump2-tec-current",
                "pump2-tec-temperature",
                "erbium-temperature",
            ]
        )

        self.booster_params = pd.DataFrame(
            columns=[
                "control_mode",
                "maintenance-state",
                "target_power",
                "target_gain",
                "target_gain_tilt",
                "input_power",
                "output_power",
                "voa_input_power",
                "voa_output_power",
                "voa_attenuation",
                "lotee:custom-name",
                "lotee:maintenance-state",
                "lotee:control-mode",
                "lotee:gain-switch-mode",
                "lotee:target-gain",
                "lotee:target-power",
                "lotee:target-gain-tilt",
                "lotee:los-shutdown",
                "lotee:optical-loo-threshold",
                "lotee:optical-loo-hysteresis",
                "lotee:input-overload-threshold",
                "lotee:input-overload-hysteresis",
                "lotee:input-low-degrade-threshold",
                "lotee:input-low-degrade-hysteresis",
                "lotee:optical-los-threshold",
                "lotee:optical-los-hysteresis",
                "lotee:orl-threshold-warning-threshold",
                "lotee:orl-threshold-warning-hysteresis",
                "lotee:force-apr",
                "entity-description",
                "operational-state",
                "output-power",
                "measured-gain",
                "als-disabled-seconds-remaining",
                "back-reflection-power",
                "optical-return-loss",
                "voa-input-power-debug",
                "voa-output-power-debug",
                "voa-attentuation-debug",
                "pump1-current",
                "pump1-tec-current",
                "pump1-tec-temperature",
                "pump2-current",
                "pump2-tec-current",
                "pump2-tec-temperature",
                "erbium-temperature",
            ]
        )

    def mux_append_current_json(self, data):

        mux_channel_attenuation = self.mux_datalist["channel_attenuation"]
        mux_open_channel_index = self.mux_datalist["open_channel_index"]
        mux_input_power = self.mux_datalist["input_power"]
        mux_output_power = self.mux_datalist["output_power"]
        mux_ocm_power = self.mux_datalist["ocm_power"]

        mux_channel_attenuation_ = pd.DataFrame(
            np.array(data["measurement_data"]["mux_channel_attenuation"])[:, 1].reshape(
                1, 95
            ),
            columns=self.column_list,
        )
        mux_input_power_ = pd.DataFrame(
            np.array(data["measurement_data"]["mux_input_power"])[:, 1].reshape(1, 95),
            columns=self.column_list,
        )
        mux_output_power_ = pd.DataFrame(
            np.array(data["measurement_data"]["mux_output_power"])[:, 1].reshape(1, 95),
            columns=self.column_list,
        )
        mux_ocm_power_ = pd.DataFrame(
            np.array(data["measurement_data"]["mux_ocm_power"])[:, 1].reshape(1, 95),
            columns=self.column_list,
        )

        tmp_ = np.zeros((1, 95))
        for channel in data["measurement_data"]["mux_open_channel_index"]:
            tmp_[0, channel - 1] = 1
        mux_open_channel_index_ = pd.DataFrame(tmp_, columns=self.column_list)

        self.mux_datalist["channel_attenuation"] = pd.concat(
            [mux_channel_attenuation, mux_channel_attenuation_], ignore_index=True
        )
        self.mux_datalist["open_channel_index"] = pd.concat(
            [mux_open_channel_index, mux_open_channel_index_], ignore_index=True
        )
        self.mux_datalist["input_power"] = pd.concat(
            [mux_input_power, mux_input_power_], ignore_index=True
        )
        self.mux_datalist["output_power"] = pd.concat(
            [mux_output_power, mux_output_power_], ignore_index=True
        )
        self.mux_datalist["ocm_power"] = pd.concat(
            [mux_ocm_power, mux_ocm_power_], ignore_index=True
        )

    def demux_append_current_json(self, data):

        demux_channel_attenuation = self.demux_datalist["channel_attenuation"]
        demux_open_channel_index = self.demux_datalist["open_channel_index"]
        demux_input_power = self.demux_datalist["input_power"]
        demux_output_power = self.demux_datalist["output_power"]
        demux_ocm_power = self.demux_datalist["ocm_power"]

        demux_channel_attenuation_ = pd.DataFrame(
            np.array(data["measurement_data"]["demux_channel_attenuation"])[
                :, 1
            ].reshape(1, 95),
            columns=self.column_list,
        )
        demux_input_power_ = pd.DataFrame(
            np.array(data["measurement_data"]["demux_input_power"])[:, 1].reshape(
                1, 95
            ),
            columns=self.column_list,
        )
        demux_output_power_ = pd.DataFrame(
            np.array(data["measurement_data"]["demux_output_power"])[:, 1].reshape(
                1, 95
            ),
            columns=self.column_list,
        )
        demux_ocm_power_ = pd.DataFrame(
            np.array(data["measurement_data"]["demux_ocm_power"])[:, 1].reshape(1, 95),
            columns=self.column_list,
        )

        tmp_ = np.zeros((1, 95))
        for channel in data["measurement_data"]["demux_open_channel_index"]:
            tmp_[0, channel - 1] = 1
        demux_open_channel_index_ = pd.DataFrame(tmp_, columns=self.column_list)

        self.demux_datalist["channel_attenuation"] = pd.concat(
            [demux_channel_attenuation, demux_channel_attenuation_], ignore_index=True
        )
        self.demux_datalist["open_channel_index"] = pd.concat(
            [demux_open_channel_index, demux_open_channel_index_], ignore_index=True
        )
        self.demux_datalist["input_power"] = pd.concat(
            [demux_input_power, demux_input_power_], ignore_index=True
        )
        self.demux_datalist["output_power"] = pd.concat(
            [demux_output_power, demux_output_power_], ignore_index=True
        )
        self.demux_datalist["ocm_power"] = pd.concat(
            [demux_ocm_power, demux_ocm_power_], ignore_index=True
        )

    def port_append_current_json(self, data):

        line_port = self.port_datalist["line_port"]
        mux_port = self.port_datalist["mux_port"]
        demux_port = self.port_datalist["demux_port"]

        data["measurement_data"]["line_port"]["measurement_label"] = data[
            "measurement_label"
        ]
        line_port_ = pd.DataFrame([data["measurement_data"]["line_port"]])
        self.port_datalist["line_port"] = line_port = pd.concat(
            [line_port, line_port_], ignore_index=True
        )

        mux_port_ = pd.DataFrame([data["measurement_data"]["mux_input_port_1"]])
        self.port_datalist["mux_port"] = mux_port = pd.concat(
            [mux_port, mux_port_], ignore_index=True
        )

        demux_port_ = pd.DataFrame([data["measurement_data"]["demux_output_port_1"]])
        self.port_datalist["demux_port"] = demux_port = pd.concat(
            [demux_port, demux_port_], ignore_index=True
        )

    def booster_append_current_json(self, data):

        booster_params_t1 = pd.DataFrame(
            [data["measurement_data"]["booster"]["params"]]
        )
        booster_params_t2 = pd.DataFrame(
            [data["measurement_data"]["debug"]["data"]["edfas"]["edfa"][0]["config"]]
        )

        dict_ = data["measurement_data"]["debug"]["data"]["edfas"]["edfa"][0]["state"]

        booster_params_t3 = pd.DataFrame()
        assert str(dict_["entity-description"]) == "Booster"
        booster_params_t3.loc[0, "entity-description"] = dict_["entity-description"]
        booster_params_t3.loc[0, "operational-state"] = dict_["operational-state"]
        booster_params_t3.loc[0, "output-power"] = dict_["output-power"]
        booster_params_t3.loc[0, "measured-gain"] = dict_["measured-gain"]
        booster_params_t3.loc[0, "als-disabled-seconds-remaining"] = dict_[
            "als-disabled-seconds-remaining"
        ]
        booster_params_t3.loc[0, "back-reflection-power"] = dict_[
            "back-reflection-power"
        ]
        booster_params_t3.loc[0, "optical-return-loss"] = dict_["optical-return-loss"]

        booster_params_t3.loc[0, "voa-input-power-debug"] = dict_["voas"]["voa"][
            "voa-input-power"
        ]
        booster_params_t3.loc[0, "voa-output-power-debug"] = dict_["voas"]["voa"][
            "voa-output-power"
        ]
        booster_params_t3.loc[0, "voa-attentuation-debug"] = dict_["voas"]["voa"][
            "voa-attentuation"
        ]

        booster_params_t3.loc[0, "pump1-current"] = dict_["pumps"]["pump"][0][
            "pump-current"
        ]
        booster_params_t3.loc[0, "pump1-tec-current"] = dict_["pumps"]["pump"][0][
            "tec-current"
        ]
        booster_params_t3.loc[0, "pump1-tec-temperature"] = dict_["pumps"]["pump"][0][
            "tec-temperature"
        ]

        booster_params_t3.loc[0, "pump2-current"] = dict_["pumps"]["pump"][1][
            "pump-current"
        ]
        booster_params_t3.loc[0, "pump2-tec-current"] = dict_["pumps"]["pump"][1][
            "tec-current"
        ]
        booster_params_t3.loc[0, "pump2-tec-temperature"] = dict_["pumps"]["pump"][1][
            "tec-temperature"
        ]

        booster_params_t3.loc[0, "erbium-temperature"] = dict_["erbium-coils"][
            "erbium-coil"
        ]["erbium-temperature"]

        booster_params_ = pd.concat(
            [booster_params_t1, booster_params_t2, booster_params_t3], axis=1
        )
        self.booster_params = pd.concat(
            [self.booster_params, booster_params_], ignore_index=True
        )

    def preamp_append_current_json(self, data):

        preamp_params_t1 = pd.DataFrame([data["measurement_data"]["preamp"]["params"]])
        preamp_params_t2 = pd.DataFrame(
            [data["measurement_data"]["debug"]["data"]["edfas"]["edfa"][1]["config"]]
        )

        dict_ = data["measurement_data"]["debug"]["data"]["edfas"]["edfa"][1]["state"]

        preamp_params_t3 = pd.DataFrame()
        assert str(dict_["entity-description"]) == "Pre-amplifier"
        preamp_params_t3.loc[0, "entity-description"] = dict_["entity-description"]
        preamp_params_t3.loc[0, "operational-state"] = dict_["operational-state"]
        preamp_params_t3.loc[0, "output-power"] = dict_["output-power"]
        preamp_params_t3.loc[0, "measured-gain"] = dict_["measured-gain"]

        preamp_params_t3.loc[0, "voa-input-power-debug"] = dict_["voas"]["voa"][
            "voa-input-power"
        ]
        preamp_params_t3.loc[0, "voa-output-power-debug"] = dict_["voas"]["voa"][
            "voa-output-power"
        ]
        preamp_params_t3.loc[0, "voa-attentuation-debug"] = dict_["voas"]["voa"][
            "voa-attentuation"
        ]

        preamp_params_t3.loc[0, "pump1-current"] = dict_["pumps"]["pump"][0][
            "pump-current"
        ]
        preamp_params_t3.loc[0, "pump1-tec-current"] = dict_["pumps"]["pump"][0][
            "tec-current"
        ]
        preamp_params_t3.loc[0, "pump1-tec-temperature"] = dict_["pumps"]["pump"][0][
            "tec-temperature"
        ]

        preamp_params_t3.loc[0, "pump2-current"] = dict_["pumps"]["pump"][1][
            "pump-current"
        ]
        preamp_params_t3.loc[0, "pump2-tec-current"] = dict_["pumps"]["pump"][1][
            "tec-current"
        ]
        preamp_params_t3.loc[0, "pump2-tec-temperature"] = dict_["pumps"]["pump"][1][
            "tec-temperature"
        ]

        preamp_params_t3.loc[0, "erbium-temperature"] = dict_["erbium-coils"][
            "erbium-coil"
        ]["erbium-temperature"]

        preamp_params_ = pd.concat(
            [preamp_params_t1, preamp_params_t2, preamp_params_t3], axis=1
        )
        self.preamp_params = pd.concat(
            [self.preamp_params, preamp_params_], ignore_index=True
        )

    def setup_append_current_json(self, data):

        setup_datalist = pd.DataFrame(
            columns=[
                "uid",
                "additional_attn",
                "label",
                "num_repeat",
                "measurement_label",
                "index",
                "repeat_index",
            ]
        )

        setup_datalist.loc[0, "uid"] = data["uid"]
        setup_datalist.loc[0, "additional_attn"] = data["measurement_setup_label"][
            "attn"
        ]
        setup_datalist.loc[0, "label"] = data["measurement_setup_label"]["label"]
        setup_datalist.loc[0, "num_repeat"] = data["measurement_setup_label"][
            "num_repeat"
        ]
        setup_datalist.loc[0, "measurement_label"] = data["measurement_label"]
        setup_datalist.loc[0, "index"] = data["measurement_setup"]["index"]
        setup_datalist.loc[0, "repeat_index"] = data["measurement_setup"][
            "repeat_index"
        ]

        self.setup_datalist = pd.concat(
            [self.setup_datalist, setup_datalist], ignore_index=True
        )

    def parse(self, dirpath=""):

        if dirpath == "":
            dirpath = self.dirpath
        else:
            self.dirpath = dirpath

        self.init_dframes()
        num_errors = 0
        for num, filename in enumerate(os.listdir(dirpath)):

            if num % 1000 == 0:
                print("Parsed %s files" % str(num))

            with open(os.path.join(dirpath, filename)) as f:
                data = json.load(f)

                try:

                    self.mux_append_current_json(data)
                    self.demux_append_current_json(data)
                    self.port_append_current_json(data)
                    self.booster_append_current_json(data)
                    self.preamp_append_current_json(data)

                    try:
                        self.setup_append_current_json(data)
                    except:
                        continue

                except Exception as e:

                    print(traceback.format_exc())
                    print("Error occurred at filename %s" % str(filename))
                    print(e)
                    num_errors += 1
                    pass
        print("Total %s errors occurred" % str(num_errors))
        print("Parsed %s JSON files in folder %s" % (str(num + 1), str(dirpath)))

        return {
            "mux": self.mux_datalist,
            "demux": self.demux_datalist,
            "port": self.port_datalist,
            "preamp": self.preamp_params,
            "booster": self.booster_params,
            "setup": self.setup_datalist,
        }

    def write_csv(self, dframe, fname):

        fname = str(self.csv_path) + str(fname) + str(".csv")
        dframe.to_csv(fname, index=True)

    def get_csv(self, json_path="", csv_path=""):

        if csv_path[-1] != "/":
            csv_path += "/"
        self.csv_path = csv_path

        print("Writing CSV files...")

        datalist = self.parse(dirpath=json_path)

        self.write_csv(datalist["booster"], "booster_params")
        self.write_csv(datalist["preamp"], "preamp_params")

        self.write_csv(datalist["port"]["line_port"], "line_port")
        self.write_csv(datalist["port"]["mux_port"], "mux_port")
        self.write_csv(datalist["port"]["demux_port"], "demux_port")

        self.write_csv(
            datalist["mux"]["channel_attenuation"], "mux_channel_attenuation"
        )
        self.write_csv(datalist["mux"]["open_channel_index"], "mux_open_channel_index")
        self.write_csv(datalist["mux"]["input_power"], "mux_input_power")
        self.write_csv(datalist["mux"]["output_power"], "mux_output_power")
        self.write_csv(datalist["mux"]["ocm_power"], "mux_ocm_power")

        self.write_csv(
            datalist["demux"]["channel_attenuation"], "demux_channel_attenuation"
        )
        self.write_csv(
            datalist["demux"]["open_channel_index"], "demux_open_channel_index"
        )
        self.write_csv(datalist["demux"]["input_power"], "demux_input_power")
        self.write_csv(datalist["demux"]["output_power"], "demux_output_power")
        self.write_csv(datalist["demux"]["ocm_power"], "demux_ocm_power")

        self.write_csv(datalist["setup"], "setup")

        print("Completed... ")
