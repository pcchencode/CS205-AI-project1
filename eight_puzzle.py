from collections import deque
import heapq

def uniform_cost_search(start_state, goal_state):
    q = deque() # Expanding
    visited = set() # Check whether the current state is visited, prunning
    parent = {} # Save the parent state for every current state, backtracking

    solution_depth = None
    max_q_size = 0
    expanded_nodes = 0

    q.appendleft(start_state)
    visited.add(tuple(start_state))
    parent[tuple(start_state)] = None

    while q:
        max_q_size = max(len(q), max_q_size)
        current_state = q.pop()
        
        # Stop condition
        if current_state == goal_state:
            ## Backtracking
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent[tuple(current_state)]
            path.reverse()
            solution_depth = len(path) - 1
            return path, solution_depth, max_q_size, expanded_nodes

        # Expanding
        neighbor_indexes = []
        zero_index = current_state.index(0)
        if zero_index // 3 > 0:
            neighbor_indexes.append(zero_index-3) #up
        if zero_index // 3 < 2:
            neighbor_indexes.append(zero_index+3) #down
        if zero_index % 3 > 0:
            neighbor_indexes.append(zero_index-1) #left
        if zero_index % 3 < 2:
            neighbor_indexes.append(zero_index+1) #right

        expanded = False    
        for idx in neighbor_indexes:
            next_state = list(current_state)
            next_state[zero_index] = next_state[idx]
            next_state[idx] = 0
            if tuple(next_state) not in visited:
                q.appendleft(next_state)
                visited.add(tuple(next_state))
                parent[tuple(next_state)] = current_state
                expanded = True
        if expanded:
            expanded_nodes += 1
    
    return None, solution_depth, max_q_size, expanded_nodes


def misplaced_tile_heu(state, goal):
    return sum(1 for i, tile in enumerate(state) if tile != goal[i] and tile != 0)

def manhattan_distance_heu(state, goal):
    distance = 0
    side_length = 3  # Since it's an 8-puzzle, the board side length is 3
    for index, value in enumerate(state):
        if value != 0:
            target_index = goal.index(value)
            # Calculate the distances based on current and target indices
            current_row, current_col = divmod(index, side_length)
            target_row, target_col = divmod(target_index, side_length)
            distance += abs(current_row - target_row) + abs(current_col - target_col)
    return distance

def a_star_search_mp(start_state, goal_state):
    pq = []  # Priority queue for A*
    visited = set()  # Check whether the current state is visited
    parent = {}  # Save the parent state for every current state
    cost = {}  # Track g(n) - the cost to reach current node

    solution_depth = None
    max_q_size = 0
    expanded_nodes = 0

    # Initial setup
    heapq.heappush(pq, (0+misplaced_tile_heu(start_state, goal_state), start_state))
    visited.add(tuple(start_state))
    parent[tuple(start_state)] = None
    cost[tuple(start_state)] = 0

    while pq:
        _, current_state = heapq.heappop(pq)
        
        # Stop condition
        if current_state == goal_state:
            # Backtracking to find path
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent[tuple(current_state)]
            path.reverse()
            solution_depth = len(path) - 1
            return path, solution_depth, max_q_size, expanded_nodes

        # Expanding nodes
        zero_index = current_state.index(0)
        neighbor_indexes = []
        if zero_index // 3 > 0:
            neighbor_indexes.append(zero_index-3) # up
        if zero_index // 3 < 2:
            neighbor_indexes.append(zero_index+3) # down
        if zero_index % 3 > 0:
            neighbor_indexes.append(zero_index-1) # left
        if zero_index % 3 < 2:
            neighbor_indexes.append(zero_index+1) # right

        expanded = False
        for idx in neighbor_indexes:
            next_state = list(current_state)
            next_state[zero_index], next_state[idx] = next_state[idx], 0
            tuple_state = tuple(next_state)
            
            g = cost[tuple(current_state)] + 1  # Assuming each move costs 1
            if tuple_state not in visited or g < cost.get(tuple_state, float('inf')):
                heapq.heappush(pq, (g + misplaced_tile_heu(next_state, goal_state), next_state))
                visited.add(tuple_state)
                parent[tuple_state] = current_state
                cost[tuple_state] = g
                expanded = True
                max_q_size = max(max_q_size, len(pq))
        if expanded:
            expanded_nodes += 1
    
    return None, solution_depth, max_q_size, expanded_nodes

def a_star_search_mh(start_state, goal_state):
    pq = []  # Priority queue for A*
    visited = set()  # Check whether the current state is visited
    parent = {}  # Save the parent state for every current state
    cost = {}  # Track g(n) - the cost to reach current node

    solution_depth = None
    max_q_size = 0
    expanded_nodes = 0

    # Initial setup
    heapq.heappush(pq, (0+manhattan_distance_heu(start_state, goal_state), start_state))
    visited.add(tuple(start_state))
    parent[tuple(start_state)] = None
    cost[tuple(start_state)] = 0

    while pq:
        _, current_state = heapq.heappop(pq)
        
        # Stop condition
        if current_state == goal_state:
            # Backtracking to find path
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent[tuple(current_state)]
            path.reverse()
            solution_depth = len(path) - 1
            return path, solution_depth, max_q_size, expanded_nodes

        # Expanding nodes
        zero_index = current_state.index(0)
        neighbor_indexes = []
        if zero_index // 3 > 0:
            neighbor_indexes.append(zero_index-3) # up
        if zero_index // 3 < 2:
            neighbor_indexes.append(zero_index+3) # down
        if zero_index % 3 > 0:
            neighbor_indexes.append(zero_index-1) # left
        if zero_index % 3 < 2:
            neighbor_indexes.append(zero_index+1) # right

        expanded = False
        for idx in neighbor_indexes:
            next_state = list(current_state)
            next_state[zero_index], next_state[idx] = next_state[idx], 0
            tuple_state = tuple(next_state)
            
            
            g = cost[tuple(current_state)] + 1  # Assuming each move costs 1
            if tuple_state not in visited or g < cost.get(tuple_state, float('inf')):
                heapq.heappush(pq, (g + manhattan_distance_heu(next_state, goal_state), next_state))
                visited.add(tuple_state)
                parent[tuple_state] = current_state
                cost[tuple_state] = g
                expanded = True
                max_q_size = max(max_q_size, len(pq))
        if expanded:
            expanded_nodes += 1
    
    return None, solution_depth, max_q_size, expanded_nodes



def print_state_matrix(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
        if i == 6:
            print("=========")


if __name__ == '__main__':
    # Test Case
    start_state = [2, 8, 3, 1, 0, 4, 7, 6, 5]
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    # path, depth, q_size, n_expand = uniform_cost_search(start_state, goal_state)
    # path, depth, q_size, n_expand = a_star_search_mp(start_state, goal_state)
    path, depth, q_size, n_expand = a_star_search_mh(start_state, goal_state)

    if path:
        print("Solution Founded!")
        for state in path:
            print_state_matrix(state)
    else:
        print("No Solution")
    print(f"Solution depth was {depth}")
    print(f"Number of nodes expanded: {n_expand}")
    print(f"Max queue size: {q_size}")
