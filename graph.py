from math import sqrt


class Graph:
    def __init__(self):
        self.path = []
        self.total_distances = 0

    def add_to_path(self, node):
        self.path.append(node)

    def add_distance(self, distance):
        self.total_distances += distance


class NNHeuristic:
    def get_closest(self, start_point, all_city):
        return self.shortest_distance(start_point, all_city)

    def shortest_distance(self, outset, cities):
        min_distance = tuple()
        s_lat, s_long = outset.get_pos()

        for node in cities:
            lat, long = node.get_pos()
            euclidean_distance = sqrt((lat - s_lat)**2 + (long - s_long)**2)
            # euclidean_distance = self.haversine(s_long, s_lat, long, lat)

            if min_distance:
                if euclidean_distance < min_distance[1]:
                    min_distance = (node, euclidean_distance)
            else:
                min_distance = (node, euclidean_distance)


        return min_distance


class TwoOpt:
    def __init__(self):
        self.total_distances = 0

    def run_2opt(self, route):
        improvement = True
        best_route = route
        best_distance = self.route_distance(route)

        while improvement:
            improvement = False
            for i in range(len(best_route) - 1):
                for k in range(i+1, len(best_route)):
                    new_route = self.swap_2opt(best_route, i, k)
                    new_distance = self.route_distance(new_route)
                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_route = new_route
                        improvement = True
                        self.total_distances += new_distance
                        break

                if improvement:
                    break
        assert len(best_route) == len(route)
        return best_route

    def swap_2opt(self, route, i, k):
        assert i >= 0 and i < (len(route) - 1)
        assert k > i and k < len(route)
        new_route = route[0:i]
        new_route.extend(reversed(route[i:k + 1]))
        new_route.extend(route[k+1:])
        assert len(new_route) == len(route)
        return new_route

    def route_distance(self, route):
        dist = 0
        prev = route[-1]
        for node in route:
        	dist += node.euclidean_dist(prev)
        	prev = node
        return dist
