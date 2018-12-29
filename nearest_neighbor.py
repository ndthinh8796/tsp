from graph import Graph
from math import sqrt


class NNHeuristic(Graph):
    def __shortest_distance(self, outset, cities):
        lat, long = outset.lat, outset.long
        closest_city = tuple()
        for node in cities:
            euclidean_dist = sqrt((node.lat - lat)**2 +
                                    (node.long - long)**2)
            if closest_city:
                if closest_city[1] > euclidean_dist:
                    closest_city = (node, euclidean_dist)
            else:
                closest_city = (node, euclidean_dist)
        return closest_city

    def find_shortest_path(self, coordinates_list):
        self.path.append(coordinates_list.pop(0))
        nod = self.path[0]
        while coordinates_list:
            nod, dis = self.__shortest_distance(nod, coordinates_list)
            self.path.append(nod)
            coordinates_list.remove(nod)
            self.total_distances += dis
        return self.show_path(), self.path
