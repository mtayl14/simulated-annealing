from search.action import Action
from result import Result

class NextAvailableCity(Action):
    # Returns the first available city
    
    def transition(current_state, available_states):
        if len(available_states) == 0:
            return Result.Err("No more states")
        
        for state in available_states:
            return Result.Ok(state)
    
    def cost(current_state, next_state):
        return current_state.distance_to_city(next_state)