from sys import stderr, argv
from nearest_neighbor import NNHeuristic
from two_opt import TwoOpt
from time import time

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


def main():
    start = time()
    coordinates_list = read_csv(argv[-1])
    _, path = NNHeuristic().run(coordinates_list)
    TwoOpt().run_2opt(path)
    end = time()
    print('TIME RUN:', end - start)


if __name__ == '__main__':
    main()
