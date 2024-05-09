from eight_puzzle import *

def valid_row(row):
    # Checking whether the length of single row is <=3
    numbers = row.split()
    if len(numbers) != 3:
        return False
    try:
        numbers = [int(num) for num in numbers]
    except ValueError:
        return False
    return all(num in range(9) for num in numbers)

def main():
    # Step 1: Welcome message and initial choice
    print("Welcome to my 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own.")
    choice = input("Your choice: ")
    
    # Step 2: Define the puzzle
    if choice == '1':
        puzzle = [1, 2, 3, 4, 5, 6, 7, 0, 8]  # default puzzle (solved state for example)
    elif choice == '2':
        puzzle = []
        print("Enter your puzzle, using a zero to represent the blank. Please only enter valid 8-puzzles. Enter the puzzle delimiting the numbers with a space. Type RET only when finished.")
        while len(puzzle) < 9:
            row = input(f"Enter the {len(puzzle)//3 + 1} row: ")
            if valid_row(row):
                puzzle.extend(int(num) for num in row.split())
            else:
                print("Invalid row. Each row must consist of exactly three numbers, all between 0 and 8.")
            if len(puzzle) == 9 and len(set(puzzle)) != 9:
                print("Invalid puzzle. Ensure all numbers from 0 to 8 are present and unique.")
                puzzle.clear()  # Reset puzzle to start over
    
    # Step 3: Algorithm choice
    print("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) for the Manhattan Distance Heuristic.")
    algorithm_choice = input("Your choice: ")
    
    # Print the puzzle and choice:
    print("Puzzle state: ")
    print_state_matrix(puzzle)
    if algorithm_choice == "1":
        print("Algorithm choice: (1) Uniform Cost Search")
    elif algorithm_choice == "2":
        print("Algorithm choice: (2) Misplaced Tile Heuristic")
    else:
        print("Algorithm choice: (3) Manhattan Distance Heuristic")
    
    # solve_puzzle
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    gh_map = None
    if algorithm_choice == "1":
        path, depth, q_size, n_expand, time_cost = uniform_cost_search(puzzle, goal_state)
    elif algorithm_choice == "2":
        path, depth, q_size, n_expand, time_cost, gh_map = a_star_search_mp(puzzle, goal_state)
    else:
        path, depth, q_size, n_expand, time_cost, gh_map = a_star_search_mh(puzzle, goal_state)

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

if __name__ == '__main__':
    main()
