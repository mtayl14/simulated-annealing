import csv, random

from tsp.city import City
from tsp.tour import Tour
from tsp.actions.shortest_path import ShortestPath
from tsp.actions.next_available_city import NextAvailableCity
from tsp.actions.random_path import RandomPath
from annealing.anneal import Annealer

def main():
    cities = set()

    # Read cities from CSV
    with open('cities2.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            x, y = row
            cities.add(City(float(x), float(y)))
    
    # Use a random city as the start
    initial = random.choice(list(cities))

    # Find tour with shortest path
    solution_shortest = Tour(cities, initial)
    solution_shortest.use_action_until_solution(ShortestPath)

    print(f"Initial solution cost={solution_shortest.cost()}")

    solution_shortest.plot_tour(f"Shortest Only, Distance={solution_shortest.cost():.4f}")

    print("Starting annealling...")
    annealer = Annealer(solution_shortest, {NextAvailableCity, RandomPath})

    solution_annealed = annealer.anneal(2, 0.995, 2000)
    print(f"Annealed solution cost={solution_annealed.cost()}")

    solution_annealed.plot_tour(f"Annealed, Distance={solution_annealed.cost():.4f}")

    if solution_annealed.cost() < solution_shortest.cost():
        print(f'Annealed solution is {solution_shortest.cost() - solution_annealed.cost()} units cheaper!')
    else:
        print('Annealed solution was worse than initial!')

if __name__ == "__main__":
    main()