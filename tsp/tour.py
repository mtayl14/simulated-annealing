from search.path import Path

class Tour(Path):
    # A path is a solution if it reaches every city
    def is_solution(self):
        # NOTE: manually mangled name!
        if len(self._Path__remaining_states) == 0:
            return True
        else:
            return False
