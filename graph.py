from math import sqrt


class Graph:
    def __init__(self):
        self.path = []
        self.total_distances = 0

    def path(self):
        return self.path

    def total_distance(self):
        return self.total_distances

    def add_to_path(self, node):
        self.path.append(node)

    def add_distance(self, distance):
        self.total_distances += distance


class Heuristic():
    def get_closest(self, start_point, all_city):
        return self.shortest_distance(start_point, all_city)

    def shortest_distance(self, outset, cities):
        min_distance = tuple()
        s_lat, s_long = outset.get_pos()

        for node in cities:
            lat, long = node.get_pos()
            euclidean_distance = sqrt((lat - s_lat)**2 + (long - s_long)**2)

            if min_distance:
                if euclidean_distance < min_distance[1]:
                    min_distance = (node, euclidean_distance)
            else:
                min_distance = (node, euclidean_distance)


        return min_distance
