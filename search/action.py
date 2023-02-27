# Action is a *strategy* to choose new state
class Action:
    # Chooses the next state from avaialble state set or Error
    def transition(current_state, available_states):
        raise Exception("Not Implemented!")

    # Returns the cost of the this action or Error
    def cost(current_state, next_state):
        raise Exception("Not Implemented!")