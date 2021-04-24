import getopt
import sys

from common.parse_file import parse_file
from common.log_city_info import log_city_info
from common.parse_args import parse_args


def get_args():
    """
    Getting arguments from command and proceeding to log function

    Supports either:
    1) cities names list, iterated by comma
    2) file name (file located in root dir of the project)
    """
    full_cmd_arguments = sys.argv
    argument_list = full_cmd_arguments[1:]

    short_options = "hf:"
    long_options = ["help", "file="]

    try:
        cities_list = list()
        arguments, values = getopt.getopt(argument_list, short_options, long_options)

        if len(arguments) > 0:
            for current_argument, current_value in arguments:
                if current_argument in ("-h", "--help"):
                    print("Test task for Madgicx Company")
                    print("Gets cities names and returns short info about each")
                    print('Made by Russ Kovalchuk')
                    print('------------')
                    print('Use: \n '
                          'python madgicx_geo.py -f <file_path>\n'
                          ' python madgicx_geo.py <cities_names_iterated_with_commas>')
                elif current_argument in ("-f", "--file"):
                    print("Entering from file (%s)" % current_value)
                    cities_list = parse_file(current_value)
        else:
            cities_list = parse_args(argument_list)

        log_city_info(cities_list)

    except getopt.error as err:
        print(str(err))
        sys.exit(2)


get_args()
