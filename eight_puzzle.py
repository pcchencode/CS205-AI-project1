
import time
from collections import deque
import heapq

def uniform_cost_search(start_state, goal_state):
    q = deque() # Expanding
    visited = set() # Check whether the current state is visited, prunning
    parent = {} # Save the parent state for every current state, backtracking
    solution_depth = None
    max_q_size = 0
    expanded_nodes = 0
    s = time.time()

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
            e = time.time()
            time_cost = str(round(e-s, 4))
            return path, solution_depth, max_q_size, expanded_nodes, time_cost

        # Expanding
        ## print g(n) and h(n)
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
    e = time.time()
    time_cost = str(round(e-s, 4))  
    return None, solution_depth, max_q_size, expanded_nodes, time_cost


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
    gh_map = {} # save g(n) and g(n) for every state
    

    solution_depth = None
    max_q_size = 0
    expanded_nodes = 0
    s = time.time()

    # Initial setup
    h_0 = misplaced_tile_heu(start_state, goal_state)
    heapq.heappush(pq, (0 + h_0, start_state))
    gh_map[tuple(start_state)] = (0, h_0)
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
            e = time.time()
            time_cost = str(round(e-s, 4))
            return path, solution_depth, max_q_size, expanded_nodes, time_cost, gh_map

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
                h = misplaced_tile_heu(next_state, goal_state)
                gh_map[tuple(next_state)] = (g, h)
                heapq.heappush(pq, (g + h, next_state))
                visited.add(tuple_state)
                parent[tuple_state] = current_state
                cost[tuple_state] = g
                expanded = True
                max_q_size = max(max_q_size, len(pq))
        if expanded:
            expanded_nodes += 1
    e = time.time()
    time_cost = str(round(e-s, 4))
    return None, solution_depth, max_q_size, expanded_nodes, time_cost, gh_map

def a_star_search_mh(start_state, goal_state):
    pq = []  # Priority queue for A*
    visited = set()  # Check whether the current state is visited
    parent = {}  # Save the parent state for every current state
    cost = {}  # Track g(n) - the cost to reach current node
    gh_map = {} # save g(n) and g(n) for every state

    solution_depth = None
    max_q_size = 0
    expanded_nodes = 0
    s = time.time()

    # Initial setup
    h_0 = manhattan_distance_heu(start_state, goal_state)
    heapq.heappush(pq, (0 + h_0, start_state))
    gh_map[tuple(start_state)] = (0, h_0)
    visited.add(tuple(start_state))
    parent[tuple(start_state)] = None
    cost[tuple(start_state)] = 0
    gh_map[tuple(start_state)] = (0, manhattan_distance_heu(start_state, goal_state))

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
            e = time.time()
            time_cost = str(round(e-s, 4))
            return path, solution_depth, max_q_size, expanded_nodes, time_cost, gh_map

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
                h = manhattan_distance_heu(next_state, goal_state)
                heapq.heappush(pq, (g + h, next_state))
                gh_map[tuple(next_state)] = (g, h)
                visited.add(tuple_state)
                parent[tuple_state] = current_state
                cost[tuple_state] = g
                expanded = True
                max_q_size = max(max_q_size, len(pq))
        if expanded:
            expanded_nodes += 1
    e = time.time()
    time_cost = str(round(e-s, 4))
    return None, solution_depth, max_q_size, expanded_nodes, time_cost, gh_map



def print_state_matrix(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
        if i == 6:
            print("=========")


if __name__ == '__main__':
    gh_map = None
    # Test Case
    start_state = [2, 8, 3, 1, 0, 4, 7, 6, 5]
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    # path, depth, q_size, n_expand, time_cost = uniform_cost_search(start_state, goal_state)
    path, depth, q_size, n_expand, time_cost, gh_map = a_star_search_mp(start_state, goal_state)
    # path, depth, q_size, n_expand, time_cost, gh_map = a_star_search_mh(start_state, goal_state)

    
    if path:
        print("Solution Founded!")
        for state in path:
            if gh_map:
                g, h = gh_map[tuple(state)]
                print(f"The best state to expand with a g(n) = {g} and h(n) = {h} is...")
            print_state_matrix(state)
    else:
        print("No Solution")
    print(f"Solution depth was {depth}")
    print(f"Number of nodes expanded: {n_expand}")
    print(f"Max queue size: {q_size}")
    print(f"It costs {time_cost} sec")
