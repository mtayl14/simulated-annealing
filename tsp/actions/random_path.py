#
# This one is super cool. I submitted the code for NextAvaliableCity and some context, and ChatGPT wrote this!
#

import random

from search.action import Action
from result import Result

class RandomPath(Action):
    # Chooses a random city from the available states
    
    def transition(current_state, available_states):
        if len(available_states) == 0:
            return Result.Err("No more states")

        # Seed the random number generator with the current state's coordinates
        seed = str(current_state.x) + str(current_state.y)
        random.seed(seed)

        # Choose a random state from the available states
        next_state = random.choice(list(available_states))

        return Result.Ok(next_state)

    def cost(current_state, next_state):
        return current_state.distance_to_city(next_state)
