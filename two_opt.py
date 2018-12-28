from graph import Graph
from math import sqrt

class TwoOpt(Graph):
    def run_2opt(self, route):
        improvement = True
        best_route = route
        best_distance = self.route_distance(route)
        total = len(best_route)

        while improvement:
            improvement = False
            for i in range(1, len(best_route) - 2):
                for k in range(i+1, len(best_route)):
                    new_route = self.swap_2opt(best_route, i, k)
                    new_distance = self.route_distance(new_route)
                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_route = new_route
                        improvement = True
                print('Processing:', str(round(i/total * 100, 2)) + '%')

        self.path = best_route
        self.total_distances = best_distance

        return self.show_path()

    def swap_2opt(self, route, i, k):
        return route[:i] + route[i:k+1][::-1] + route[k+1:]

    def route_distance(self, route):
        dist = 0
        for node in range(len(route) - 1):
            lat, long = route[node].lat, route[node].long
            n_lat, n_long = route[node + 1].lat, route[node + 1].long
            dist += sqrt((n_lat - lat)**2 + (n_long - long)**2)
        return dist
