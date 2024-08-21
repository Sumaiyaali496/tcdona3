# from parser.ila_parser import ILAXMLParser
from parser.lumentum_parser import LumentumJsonParser
from parser.polatis_parser import PolatisJsonParser
from parser.osa_parser import OSAJsonParser
from parser.ila_parser import ILAJsonParser

import os
import argparse

argparser = argparse.ArgumentParser(
    description="Script to convert JSON monitoring files to csv"
)
argparser.add_argument(
    "--source",
    action="store",
    type=str,
    required=False,
    default="./",
    help="Source folder for JSON files",
)
argparser.add_argument(
    "--dest",
    action="store",
    type=str,
    required=False,
    default="./",
    help="Destination path for CSV files",
)

argparser.add_argument(
    "--test",
    action="store",
    type=str,
    required=False,
    default="False",
    help="test mode",
)

argparser.add_argument(
    "--osa_resolution",
    action="store",
    type=int,
    required=False,
    default=501,
    help="Resolution of points in OSA",
)


argparser.add_argument(
    "--osa",
    action="store_true",
)

argparser.add_argument("--roadm", action="store_true")

argparser.add_argument("--roadm_preamp", action="store_true")

argparser.add_argument(
    "--polatis",
    action="store_true",
)

argparser.add_argument(
    "--ila",
    action="store_true",
)

if __name__ == "__main__":

    args = argparser.parse_args()

    folder = args.source
    csv = args.dest

    if csv[-1] != "/":
        csv += "/"
    if folder[-1] != "/":
        folder += "/"

    if args.polatis:
        pol_path = csv + "polatis"
        pol_folder = folder + "polatis"
    if args.roadm:
        lum_path = csv + "roadm"
        lum_folder = folder + "roadm"

    if args.roadm_preamp:
        dut_lum_path = csv + "lumentum_dut"
        dut_lum_folder = folder + "lumentum_dut"

        aux_lum_path = csv + "lumentum_aux"
        aux_lum_folder = folder + "lumentum_aux"

    if args.osa:
        osa_path = csv + "osa"
        osa_folder = folder + "osa"

    if args.ila:
        ila_path = csv + "ila"
        ila_folder = folder + "ila"

    if not os.path.isdir(csv):
        os.makedirs(csv)
    if args.polatis and not os.path.isdir(pol_path):
        os.makedirs(pol_path)
    if args.roadm and not os.path.isdir(lum_path):
        os.makedirs(lum_path)
    if args.osa and not os.path.isdir(osa_path):
        os.makedirs(osa_path)
    if args.roadm_preamp and not os.path.isdir(dut_lum_path):
        os.makedirs(dut_lum_path)
    if args.roadm_preamp and not os.path.isdir(aux_lum_path):
        os.makedirs(aux_lum_path)
    if args.ila and not os.path.isdir(ila_path):
        os.makedirs(ila_path)

    if args.test != "False":
        pass

    else:

        if args.polatis:
            pol_parser = PolatisJsonParser()
            pol_parser.get_csv(json_path=pol_folder, csv_path=pol_path)

        if args.roadm:
            lum_parser = LumentumJsonParser()
            lum_parser.get_csv(json_path=lum_folder, csv_path=lum_path)

        if args.osa:
            osa_parser = OSAJsonParser(resolution=args.osa_resolution)
            osa_parser.get_csv(json_path=osa_folder, csv_path=osa_path)

        if args.ila:
            ila_parser = ILAJsonParser()
            ila_parser.get_csv(json_path=ila_folder, csv_path=ila_path)

        if args.roadm_preamp:
            dut_lum_parser = LumentumJsonParser()
            dut_lum_parser.get_csv(json_path=dut_lum_folder, csv_path=dut_lum_path)

            aux_lum_parser = LumentumJsonParser()
            aux_lum_parser.get_csv(json_path=aux_lum_folder, csv_path=aux_lum_path)

        print("Finished...")
