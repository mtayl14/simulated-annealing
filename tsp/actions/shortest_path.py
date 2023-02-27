from search.action import Action
from result import Result

class ShortestPath(Action):
    # Talk about unoptimized!
    # Searches for the nearest city
    
    def transition(current_state, available_states):
        if len(available_states) == 0:
            return Result.Err("No more states")
        
        # Unsorted search over available states to find cheapest next state
        cheapest_state = None
        cheapest_cost = -1
        for state in available_states:
            cost = ShortestPath.cost(current_state, state)
            
            # If this is the first state available
            if cheapest_state == None: 
                cheapest_cost = cost
                cheapest_state = state
                continue

            # Otherwise, if this is cheaper that the current best
            if cost < cheapest_cost:
                cheapest_cost = cost
                cheapest_state = state

        return Result.Ok(cheapest_state)
    
    def cost(current_state, next_state):
        return current_state.distance_to_city(next_state)