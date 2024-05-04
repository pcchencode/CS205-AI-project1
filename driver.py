from eight_puzzle import *

def valid_row(row):
    #檢查輸入的行是否有效：三個數字且都在0到8之間
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
    
    # Assuming a function `solve_puzzle` exists in your game logic that takes puzzle state and algorithm choice
    # For now, we just print the puzzle and choice:
    print("Puzzle state: ")
    print_state_matrix(puzzle)
    print("Algorithm choice:", algorithm_choice)
    
    # solve_puzzle
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    if algorithm_choice == "1":
        path, depth, q_size, n_expand = uniform_cost_search(puzzle, goal_state)
    elif algorithm_choice == "2":
        path, depth, q_size, n_expand = a_star_search_mp(puzzle, goal_state)
    else:
        path, depth, q_size, n_expand = a_star_search_mh(puzzle, goal_state)

    if path:
        print("Solution Founded!")
        for state in path:
            print_state_matrix(state)
    else:
        print("No Solution")
    print(f"Solution depth was {depth}")
    print(f"Number of nodes expanded: {n_expand}")
    print(f"Max queue size: {q_size}")

if __name__ == '__main__':
    main()
