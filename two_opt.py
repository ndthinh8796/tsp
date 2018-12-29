from graph import Graph
from math import sqrt


class TwoOpt(Graph):
    def find_shortest_path(self, route):
        improvement = True
        best_route = route
        best_distance = self.__route_distance(route)

        while improvement:
            improvement = False
            for i in range(1, len(best_route) - 2):
                for k in range(i+1, len(best_route)):
                    new_route = self.__swap_2opt(best_route, i, k)
                    new_distance = self.__route_distance(new_route)
                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_route = new_route
                        improvement = True

        self.path = best_route
        self.total_distances = best_distance

        return self.show_path()

    def __swap_2opt(self, route, i, k):
        return route[:i] + route[i:k+1][::-1] + route[k+1:]

    def __route_distance(self, route):
        dist = 0
        for node in range(len(route) - 1):
            lat, long = route[node].lat, route[node].long
            n_lat, n_long = route[node + 1].lat, route[node + 1].long
            dist += sqrt((n_lat - lat)**2 + (n_long - long)**2)
        return dist
