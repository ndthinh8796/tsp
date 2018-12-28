from graph import Graph
from math import sqrt


class NNHeuristic(Graph):
    def shortest_distance(self, outset, cities):
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

    def run(self, coordinates_list):
        self.path.append(coordinates_list.pop(0))
        nod = self.path[0]
        total = len(coordinates_list)
        count = 0
        while coordinates_list:
            nod, dis = self.shortest_distance(nod, coordinates_list)
            self.path.append(nod)
            coordinates_list.remove(nod)
            self.total_distances += dis
            # print('Processing:', str(round(count/total*100, 2)))
            count += 1
        return self.show_path(), self.path
