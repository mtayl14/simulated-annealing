from matplotlib import pyplot as plt

from search.path import Path

class Tour(Path):
    # A path is a solution if it reaches every city
    def is_solution(self):
        # NOTE: manually mangled name!
        if len(self._Path__remaining_states) == 0:
            return True
        else:
            return False
    
    # Graph values
    def plot_tour(self, graph_title):
        
        plt.plot()
        plt.title(graph_title)

        # Collect points
        x_coords = list()
        y_coords = list()
        for point in self._Path__prev_states:
            x_coords.append(point.x)
            y_coords.append(point.y)
        
        # Plot the cities
        plt.scatter(x_coords, y_coords)

        # Plot the lines
        last_point = None
        for point in self._Path__prev_states:
            # If this is the first point
            if last_point == None:
                plt.text(point.x, point.y, f'START')
                last_point = point
                continue
            # Otherwise
            distance = last_point.distance_to_city(point)
            plt.plot([last_point.x, point.x], [last_point.y, point.y])
            # plt.text((last_point.x + point.x) / 2, (last_point.y + point.y) / 2, f'{distance:.3f}', ha='center', va='center')
            last_point = point

        plt.text(last_point.x, last_point.y, f'END')

        # Show the plot
        plt.show()
