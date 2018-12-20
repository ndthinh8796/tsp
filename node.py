from math import sqrt

class Node:
    def __init__(self, city_name, latitude, longtitude):
        self.city_name = city_name
        self.latitude = float(latitude)
        self.longtitude = float(longtitude)

    def get_pos(self):
        return (self.latitude, self.longtitude)

    def euclidean_dist(self, other):
        dx = self.latitude - other.latitude
        dy = self.longtitude - other.longtitude
        euclidean_distance = sqrt((dx)**2 + (dy)**2)
        return euclidean_distance
