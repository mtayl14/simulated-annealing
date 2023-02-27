from search.state import State
from math import sqrt, pow

class City(State):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_city(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))