from sys import stderr


"""
    Use csv module to read file
"""

def check_file(file):
    from os import access, R_OK
    from os.path import isfile

    if not isfile(file) or not access(file, R_OK):
        stderr.write('Invalid file\n')
        exit(1)
    return True


def list_nodes(csv_file):
    from node import Node

    try:
        return [Node(city, lat, long) for city, lat, long in csv_file]
    except ValueError:
        stderr.write('Invalid file\n')
        exit(1)


def read_csv(f_name):
    from csv import reader

    if check_file(f_name):
        with open(f_name, 'r') as city_file:
            return list_nodes(reader(city_file))
