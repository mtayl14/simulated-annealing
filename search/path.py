from copy import deepcopy

from result import Result
from search.state import State
from search.action import Action

# Class the represents a path
# Can either be worked step-by-step or can generate a solution using an Action
class Path:
    def __init__(self, all_states, initial):
        if not isinstance(initial, State):
            raise Exception("Initial state is not an instance of State!")

        self.__initial = initial
        self.__all_states = set(all_states)
        self.__reset()

    def __reset(self):
        self.__cost = 0
        self.__prev_states = list()
        self.__remaining_states = set(self.__all_states)
        self.__remaining_states.remove(self.__initial)
        self.__current = self.__initial
        self.__actions = list()
    
    # Use an action a single time
    def push_action(self, action):
        # Determine if action is valid
        next_state = action.transition(self.__current, self.__remaining_states)

        if next_state.is_ok():
            self.__prev_states.append(self.__current)
            # Update cost
            self.__cost += action.cost(self.__current, next_state.unwrap())
            # Update the current state
            self.__current = next_state.unwrap()
            # Record what we jsut did
            self.__actions.append(action)
            # Remove the current state from the pool of potential states
            self.__remaining_states.remove(self.__current)
            return Result.Ok(self.__current)
        else:
            return Result.Err(next_state.get_err())
    
    # Change the action taken at a point in time and redo every future
    # Returns a copy
    def change_action(self, index, new_action):
        # Deep copy will still be an instance of subclass, not just Path
        new_self = deepcopy(self)
        # Reset
        new_self.__reset()
        # Replay our actions up to index
        for action in self.__actions[:index]:
            if not new_self.push_action(action).is_ok():
                raise Exception("Couldn't replay previous actions!")
        
        # Do the new action
        new_self.push_action(new_action)

        # Replay the other actions
        for action in self.__actions[index + 1:]:
            if not new_self.push_action(action).is_ok():
                return Result.Err("Changing action makes solution impossible!")
        
        # Now new_self is ready
        return new_self


    # Use an action until a solution is reached or all states covered, whichever is first
    def use_action_until_solution(self, action):
        max_next_states = len(self.__remaining_states)
        used_states = 0

        while used_states < max_next_states:
            self.push_action(action)
            used_states += 1
            if self.is_solution():
                return
        
        raise Exception("Could not find solution before max iterations!")
            

    def cost(self):
        return self.__cost


    def is_solution(self):
        raise Exception("Not implemented!")