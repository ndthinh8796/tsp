class Node:
    __slots__ = ['city_name', 'lat', 'long']

    def __init__(self, city_name, latitude, longtitude):
        self.city_name = city_name
        self.lat = float(latitude)
        self.long = float(longtitude)
