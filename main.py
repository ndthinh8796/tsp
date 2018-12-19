from os import access, R_OK
from os.path import isfile
from sys import stderr
from csv import reader
from node import Node
from graph import Graph, Heuristic

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

    graph = Graph()
    heuristic = Heuristic()

    graph.add_to_path(coordinates_list[0])

    for node in graph.path:
        if len(graph.path) < len(coordinates_list):
            cities_left = list(set(coordinates_list) - set(graph.path))
            nod, dis = heuristic.get_closest(node, cities_left)
            graph.add_to_path(nod)
            graph.add_distance(dis)
        else:
            nod, dis = heuristic.get_closest(node, [graph.path[0]])
            graph.add_to_path(nod)
            graph.add_distance(dis)
            break

    print('TOTAL LENGTH:', graph.total_distances)
    print('PATH:', '-> '.join([x.get_city() for x in graph.path]))


if __name__ == '__main__':
    main()
