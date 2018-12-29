from graph import Graph
from itertools import permutations
from math import sqrt


class BruteForce(Graph):
    def find_shortest_path(self, route):
        shortest_path = tuple()

        for path in permutations(route[1:]):
            print(path)
            path = (route[0],) + path
            total_distances = self.__route_distance(path)
            if shortest_path:
                if total_distances < shortest_path[1]:
                    shortest_path = (path, total_distances)
            else:
                shortest_path = (path, total_distances)

        self.path, self.total_distances = shortest_path

        return self.show_path()

    def __route_distance(self, path):
        dist = 0
        for node in range(len(path) - 1):
            lat, long = path[node].lat, path[node].long
            n_lat, n_long = path[node + 1].lat, path[node + 1].long
            dist += sqrt((n_lat - lat)**2 + (n_long - long)**2)
        return dist
