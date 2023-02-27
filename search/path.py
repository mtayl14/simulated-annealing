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
        self.__all_states = all_states
        self.__cost = 0
        self.__remaining_states = set(all_states)
        self.__remaining_states.remove(initial)
        self.__current = initial
        self.__actions = list()
    
    # Use an action a single time
    def push_action(self, action):
        # Determine if action is valid
        next_state = action.transition(self.__current, self.__remaining_states)

        if next_state.is_ok():
            self.__cost += action.cost(self.__current, next_state.unwrap())
            self.__current = next_state.unwrap()
            self.__actions.append(action)
            self.__remaining_states.remove(self.__current)
            return Result.Ok(self.__current)
        else:
            return Result.Err(next_state.get_err())
    
    # Undo the last action
    def pop_action(self):
        raise Exception("Not implemented!")
    
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