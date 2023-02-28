import random
import math

from search.state import State
from search.action import Action
from search.path import Path

class Annealer:

    def __init__(self, initial_solution, possible_actions):
        # Possible actions needs to be a set
        self.initial_solution = initial_solution
        self.possible_actions = possible_actions

    # Randomly generate a related solution
    def __neighbor(self, current_sol):
        # Index
        i = random.randint(0, len(current_sol._Path__actions) - 1)
        j = random.choice(list(self.possible_actions))
        # print(f"Changing action {i} from {current_sol._Path__actions[i]} to {j}")
        return current_sol.change_action(i, j)

    # Start annealing with an initial temperature T_start, minimum temperature T_min, scaler alpha, performing n iterations
    # 
    def anneal(self, start_temperature, alpha, n):
        temp = start_temperature
        best_solution = self.initial_solution
        current_solution = best_solution

        for i in range(0, n):
            new_solution = self.__neighbor(current_solution)
            
            # If the new solution beats the previous best
            if new_solution.cost() < best_solution.cost():
                best_solution = new_solution
            
            # Difference between current and new
            diff = new_solution.cost() - current_solution.cost()

            # Calculate acceptance chance
            if diff < 0 or random.random() < math.exp(-diff / temp):
                current_solution = new_solution

            # Cool temperature
            temp *= alpha
            # Break if temp is too low
            if temp < 1e-6:
                print("Breaking out of annealing because temp is too low")
                break
        
        return best_solution
            

