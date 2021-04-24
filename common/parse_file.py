def parse_file(file_name):
    """
    Parse file info

    :param file_name: File path
    :return: List of the cities names from file
    """
    cities_l = list()
    file = open(file_name, "r")
    for city in file:
        cities_l.append(city)
    return cities_l
