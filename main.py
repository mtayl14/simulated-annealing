
import csv, random

from tsp.city import City
from tsp.tour import Tour
from tsp.actions.shortest_path import ShortestPath

def main():
    cities = set()

    # Read cities from CSV
    with open('cities1.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            x, y = row
            cities.add(City(float(x), float(y)))
    
    # Use a random city as the start
    initial = random.choice(list(cities))

    # Find tour with shortest path
    solution = Tour(cities, initial)
    solution.use_action_until_solution(ShortestPath)

    print(f"Found solution! Cost={solution.cost()}")

if __name__ == "__main__":
    main()