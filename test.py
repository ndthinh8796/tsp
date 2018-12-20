from os import access, R_OK
from os.path import isfile
from sys import stderr
from csv import reader
from node import Node
from graph import Graph, Greedy
from math import sqrt

def check_file(file):
    if not isfile(file) or not access(file, R_OK):
        stderr.write('Invalid file\n')
        exit(1)
    return True


def list_nodes(csv_file):
    try:
        return [Node(city, lat, long) for city, lat, long in csv_file]
    except ValueError:
        stderr.write('Invalid file\n')
        exit(1)


def read_csv(f_name):
    if check_file(f_name):
        with open(f_name, 'r') as city_file:
            csv_reader = reader(city_file)
            return list_nodes(csv_reader)


def main():
    coordinates_list = read_csv('vn_map.csv')
    lat, long = coordinates_list[0].get_pos()
    a = []
    for city in coordinates_list[1:]:
        s_lat, s_long = city.get_pos()
        euclidean_distance = sqrt((lat - s_lat)**2 + (long - s_long)**2)
        a.append((city, euclidean_distance))

    print('TOTAL DISTANCE:', sum([x[1] for x in a]))
    print('PATH:', [x[0].city_name for x in sorted(a, key=lambda v: v[1])])

main()
