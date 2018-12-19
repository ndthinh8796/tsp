class Node:
    def __init__(self, city_name, latitude, longtitude):
        self.city_name = city_name
        self.latitude = latitude
        self.longtitude = longtitude

    def get_pos(self):
        return (float(self.latitude), float(self.longtitude))

    def get_city(self):
        return self.city_name
