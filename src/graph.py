from abc import ABC, abstractmethod


class Graph(ABC):
    def __init__(self):
        self.path = []
        self.total_distances = 0

    def show_path(self):
        print('PATH:', '-> '.join([x.city_name for x in self.path]))
        print('TOTAL LENGTH:', self.total_distances)

    @abstractmethod
    def find_shortest_path(self):
        pass
