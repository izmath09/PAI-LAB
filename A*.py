import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to end node
        self.f = 0  # Total cost: f = g + h

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def astar_search(grid, start, end):
    # Initialize start and end nodes
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize lists for open nodes and closed nodes
    open_list = []
    closed_list = set()

    # Heapify the open list and add the start node to it
    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    # Define possible movements (right, left, down, up, diagonal)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Loop until the open list is empty
    while open_list:
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node)

        # Check if we have reached the end node
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate children nodes
        children = []
        for direction in directions:
            # Get node position
            node_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            # Make sure within range
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[0]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if grid[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Calculate cost
            new_node.g = current_node.g + 1
            new_node.h = ((node_position[0] - end_node.position[0]) ** 2) + ((node_position[1] - end_node.position[1]) ** 2)
            new_node.f = new_node.g + new_node.h

            # Check if node is already in the open list and has a lower f value
            if any(node == new_node and node.f <= new_node.f for node in open_list):
                continue

            # Check if node is already in the closed list and has a lower f value
            if any(node == new_node and node.f <= new_node.f for node in closed_list):
                continue

            # Add the new node to the open list
            heapq.heappush(open_list, new_node)

    # If no path is found
    return None
