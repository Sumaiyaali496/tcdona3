import pandas as pd
import os
import json
import traceback


class ILAJsonParser:
    def __init__(self, dirpath=""):

        self.dirpath = dirpath

    def init_dframes(self):

        self.setup_dframe = pd.DataFrame(
            columns=["measurement_label", "time", "index", "uid", "repeat_index"]
        )
        self.amp_dframe = pd.DataFrame(
            columns=[
                "amplifiers_amplifier0_name",
                "amplifiers_amplifier0_config_name",
                "amplifiers_amplifier0_config_type_@xmlns:oc-opt-amp",
                "amplifiers_amplifier0_config_type_#text",
                "amplifiers_amplifier0_config_gain-range_@xmlns:oc-opt-amp",
                "amplifiers_amplifier0_config_gain-range_#text",
                "amplifiers_amplifier0_config_target-gain",
                "amplifiers_amplifier0_config_target-gain-tilt",
                "amplifiers_amplifier0_config_amp-mode_@xmlns:oc-opt-amp",
                "amplifiers_amplifier0_config_amp-mode_#text",
                "amplifiers_amplifier0_config_enabled",
                "amplifiers_amplifier0_config_autolos",
                "amplifiers_amplifier0_state_actual-gain_instant",
                "amplifiers_amplifier0_state_actual-gain-tilt_instant",
                "amplifiers_amplifier0_state_input-power-c-band_instant",
                "amplifiers_amplifier0_state_input-power-total_instant",
                "amplifiers_amplifier0_state_input-power-l-band_instant",
                "amplifiers_amplifier0_state_output-power-c-band_instant",
                "amplifiers_amplifier0_state_output-power-total_instant",
                "amplifiers_amplifier0_state_output-power-l-band_instant",
                "amplifiers_amplifier0_state_operational-state",
                "amplifiers_amplifier0_state_pump-temperature",
                "amplifiers_amplifier0_state_pump1-temperature",
                "amplifiers_amplifier0_state_laser-bias-current_instant",
                "amplifiers_amplifier0_state_laser-bias1-current_instant",
                "amplifiers_amplifier0_state_back-reflection_instant",
                "amplifiers_amplifier0_state_back-reflection-ratio_instant",
                "amplifiers_amplifier1_name",
                "amplifiers_amplifier1_config_name",
                "amplifiers_amplifier1_config_type_@xmlns:oc-opt-amp",
                "amplifiers_amplifier1_config_type_#text",
                "amplifiers_amplifier1_config_gain-range_@xmlns:oc-opt-amp",
                "amplifiers_amplifier1_config_gain-range_#text",
                "amplifiers_amplifier1_config_target-gain",
                "amplifiers_amplifier1_config_target-gain-tilt",
                "amplifiers_amplifier1_config_amp-mode_@xmlns:oc-opt-amp",
                "amplifiers_amplifier1_config_amp-mode_#text",
                "amplifiers_amplifier1_config_enabled",
                "amplifiers_amplifier1_config_autolos",
                "amplifiers_amplifier1_state_actual-gain_instant",
                "amplifiers_amplifier1_state_actual-gain-tilt_instant",
                "amplifiers_amplifier1_state_input-power-c-band_instant",
                "amplifiers_amplifier1_state_input-power-total_instant",
                "amplifiers_amplifier1_state_input-power-l-band_instant",
                "amplifiers_amplifier1_state_output-power-c-band_instant",
                "amplifiers_amplifier1_state_output-power-total_instant",
                "amplifiers_amplifier1_state_output-power-l-band_instant",
                "amplifiers_amplifier1_state_operational-state",
                "amplifiers_amplifier1_state_pump-temperature",
                "amplifiers_amplifier1_state_pump1-temperature",
                "amplifiers_amplifier1_state_laser-bias-current_instant",
                "amplifiers_amplifier1_state_laser-bias1-current_instant",
                "amplifiers_amplifier1_state_back-reflection_instant",
                "amplifiers_amplifier1_state_back-reflection-ratio_instant",
            ]
        )

    @staticmethod
    def dict_parser(dict_, out={}, prefix=""):

        if isinstance(dict_, list):
            for num, value in enumerate(dict_):
                key = ""
                if value == 0:
                    key = prefix + "_ILA_AB"
                elif value == 1:
                    key = prefix + "_ILA_BA"
                else:
                    key = prefix + str(num)
                out = ILAJsonParser.dict_parser(value, out, key)

        elif isinstance(dict_, dict):
            for key, value in dict_.items():
                if prefix != "":
                    key = prefix + "_" + str(key)
                else:
                    key = str(key)
                out = ILAJsonParser.dict_parser(value, out, key)
        else:
            out[prefix] = dict_

        return out

    def parse(self, dirpath=""):

        if dirpath == "":
            dirpath = self.dirpath
        else:
            self.dirpath = dirpath
        self.init_dframes()
        num_errors = 0
        for num, filename in enumerate(os.listdir(dirpath)):

            try:

                if num % 1000 == 0:
                    print("Parsed %s files" % str(num))

                with open(os.path.join(dirpath, filename)) as f:
                    data = json.load(f)

                ## Setup dataframe
                setup_dframe = pd.DataFrame(
                    columns=[
                        "measurement_label",
                        "time",
                        "index",
                        "uid",
                        "repeat_index",
                    ]
                )
                for column in self.setup_dframe.columns:
                    setup_dframe.loc[0, column] = data[column]
                self.setup_dframe = pd.concat(
                    [self.setup_dframe, setup_dframe], ignore_index=True
                )

                ## Amplifier dataframe
                amp_dframe = pd.DataFrame(
                    columns=[
                        "amplifiers_amplifier0_name",
                        "amplifiers_amplifier0_config_name",
                        "amplifiers_amplifier0_config_type_@xmlns:oc-opt-amp",
                        "amplifiers_amplifier0_config_type_#text",
                        "amplifiers_amplifier0_config_gain-range_@xmlns:oc-opt-amp",
                        "amplifiers_amplifier0_config_gain-range_#text",
                        "amplifiers_amplifier0_config_target-gain",
                        "amplifiers_amplifier0_config_target-gain-tilt",
                        "amplifiers_amplifier0_config_amp-mode_@xmlns:oc-opt-amp",
                        "amplifiers_amplifier0_config_amp-mode_#text",
                        "amplifiers_amplifier0_config_enabled",
                        "amplifiers_amplifier0_config_autolos",
                        "amplifiers_amplifier0_state_actual-gain_instant",
                        "amplifiers_amplifier0_state_actual-gain-tilt_instant",
                        "amplifiers_amplifier0_state_input-power-c-band_instant",
                        "amplifiers_amplifier0_state_input-power-total_instant",
                        "amplifiers_amplifier0_state_input-power-l-band_instant",
                        "amplifiers_amplifier0_state_output-power-c-band_instant",
                        "amplifiers_amplifier0_state_output-power-total_instant",
                        "amplifiers_amplifier0_state_output-power-l-band_instant",
                        "amplifiers_amplifier0_state_operational-state",
                        "amplifiers_amplifier0_state_pump-temperature",
                        "amplifiers_amplifier0_state_pump1-temperature",
                        "amplifiers_amplifier0_state_laser-bias-current_instant",
                        "amplifiers_amplifier0_state_laser-bias1-current_instant",
                        "amplifiers_amplifier0_state_back-reflection_instant",
                        "amplifiers_amplifier0_state_back-reflection-ratio_instant",
                        "amplifiers_amplifier1_name",
                        "amplifiers_amplifier1_config_name",
                        "amplifiers_amplifier1_config_type_@xmlns:oc-opt-amp",
                        "amplifiers_amplifier1_config_type_#text",
                        "amplifiers_amplifier1_config_gain-range_@xmlns:oc-opt-amp",
                        "amplifiers_amplifier1_config_gain-range_#text",
                        "amplifiers_amplifier1_config_target-gain",
                        "amplifiers_amplifier1_config_target-gain-tilt",
                        "amplifiers_amplifier1_config_amp-mode_@xmlns:oc-opt-amp",
                        "amplifiers_amplifier1_config_amp-mode_#text",
                        "amplifiers_amplifier1_config_enabled",
                        "amplifiers_amplifier1_config_autolos",
                        "amplifiers_amplifier1_state_actual-gain_instant",
                        "amplifiers_amplifier1_state_actual-gain-tilt_instant",
                        "amplifiers_amplifier1_state_input-power-c-band_instant",
                        "amplifiers_amplifier1_state_input-power-total_instant",
                        "amplifiers_amplifier1_state_input-power-l-band_instant",
                        "amplifiers_amplifier1_state_output-power-c-band_instant",
                        "amplifiers_amplifier1_state_output-power-total_instant",
                        "amplifiers_amplifier1_state_output-power-l-band_instant",
                        "amplifiers_amplifier1_state_operational-state",
                        "amplifiers_amplifier1_state_pump-temperature",
                        "amplifiers_amplifier1_state_pump1-temperature",
                        "amplifiers_amplifier1_state_laser-bias-current_instant",
                        "amplifiers_amplifier1_state_laser-bias1-current_instant",
                        "amplifiers_amplifier1_state_back-reflection_instant",
                        "amplifiers_amplifier1_state_back-reflection-ratio_instant",
                    ]
                )
                temp_dframe = self.dict_parser(
                    data["nc:rpc-reply"]["data"]["open-optical-device"][
                        "optical-amplifier"
                    ],
                    {},
                )
                for column in self.amp_dframe.columns:
                    amp_dframe.loc[0, column] = temp_dframe[column]
                self.amp_dframe = pd.concat(
                    [self.amp_dframe, amp_dframe], ignore_index=True
                )

            except Exception as e:
                print(traceback.format_exc())
                print("Error occurred at filename %s" % str(filename))
                print(e)
                num_errors += 1
        print("Total %s errors occurred" % str(num_errors))
        print("Parsed %s JSON files in folder %s" % (str(num + 1), str(dirpath)))

        self.amp_dframe.columns = [
            "amp1_name",
            "amp1_config_name",
            "amp1_config_type_@xmlns:oc-opt-amp",
            "amp1_config_type_#text",
            "amp1_config_gain-range_@xmlns:oc-opt-amp",
            "amp1_config_gain-range_#text",
            "amp1_config_target-gain",
            "amp1_config_target-gain-tilt",
            "amp1_config_amp-mode_@xmlns:oc-opt-amp",
            "amp1_config_amp-mode_#text",
            "amp1_config_enabled",
            "amp1_config_autolos",
            "amp1_state_actual-gain_instant",
            "amp1_state_actual-gain-tilt_instant",
            "amp1_state_input-power-c-band_instant",
            "amp1_state_input-power-total_instant",
            "amp1_state_input-power-l-band_instant",
            "amp1_state_output-power-c-band_instant",
            "amp1_state_output-power-total_instant",
            "amp1_state_output-power-l-band_instant",
            "amp1_state_operational-state",
            "amp1_state_pump-temperature",
            "amp1_state_pump1-temperature",
            "amp1_state_laser-bias-current_instant",
            "amp1_state_laser-bias1-current_instant",
            "amp1_state_back-reflection_instant",
            "amp1_state_back-reflection-ratio_instant",
            "amp2_name",
            "amp2_config_name",
            "amp2_config_type_@xmlns:oc-opt-amp",
            "amp2_config_type_#text",
            "amp2_config_gain-range_@xmlns:oc-opt-amp",
            "amp2_config_gain-range_#text",
            "amp2_config_target-gain",
            "amp2_config_target-gain-tilt",
            "amp2_config_amp-mode_@xmlns:oc-opt-amp",
            "amp2_config_amp-mode_#text",
            "amp2_config_enabled",
            "amp2_config_autolos",
            "amp2_state_actual-gain_instant",
            "amp2_state_actual-gain-tilt_instant",
            "amp2_state_input-power-c-band_instant",
            "amp2_state_input-power-total_instant",
            "amp2_state_input-power-l-band_instant",
            "amp2_state_output-power-c-band_instant",
            "amp2_state_output-power-total_instant",
            "amp2_state_output-power-l-band_instant",
            "amp2_state_operational-state",
            "amp2_state_pump-temperature",
            "amp2_state_pump1-temperature",
            "amp2_state_laser-bias-current_instant",
            "amp2_state_laser-bias1-current_instant",
            "amp2_state_back-reflection_instant",
            "amp2_state_back-reflection-ratio_instant",
        ]

        return self.setup_dframe, self.amp_dframe

    @staticmethod
    def write_csv(csv_path, dframe, fname):

        fname = str(csv_path) + str(fname) + str(".csv")
        dframe.to_csv(fname, index=True)

    def get_csv(self, json_path="", csv_path=""):

        if csv_path[-1] != "/":
            csv_path += "/"
        self.csv_path = csv_path

        print("Writing CSV files...")

        setup_dframe, amp_dframe = self.parse(dirpath=json_path)

        self.write_csv(csv_path, setup_dframe, "setup")
        self.write_csv(csv_path, amp_dframe, "amp")
