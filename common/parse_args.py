def parse_args(args_list):
    """
    Parse arguments from command line

    :param args_list: list of cities names (type=string)
    :return: cities list (type=list)
    """
    cities_str = str()
    for idx, item in enumerate(args_list):
        if (args_list[idx].endswith(',') and idx != 0) \
                or (idx == len(args_list)-1 and not args_list[idx-1].endswith(',')):
            cities_str += ' %s' % item
        else:
            cities_str += item

    return cities_str.split(",")
