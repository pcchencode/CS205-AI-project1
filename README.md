# CS205-AI-project1
project 1 of solving classical 8-puzzle

## File description
* `eight_puzzle.py`: Main function containing Uniform Cost Search, A* Algorithms.
* `driver.py`: Driver programm starting the puzzle.

## How to run?
* If you are going to test the main algorithm function: `eight_puzzle.py`
run:
    ```bash
    $ python3 eight_puzzle.py
    ```
    Expected result:
    ```
    Solution Founded!
    [2, 8, 3]
    [1, 0, 4]
    [7, 6, 5]
    =========
    [2, 0, 3]
    [1, 8, 4]
    [7, 6, 5]
    =========
    [0, 2, 3]
    [1, 8, 4]
    [7, 6, 5]
    =========
    [1, 2, 3]
    [0, 8, 4]
    [7, 6, 5]
    =========
    [1, 2, 3]
    [8, 0, 4]
    [7, 6, 5]
    =========
    Solution depth was 4
    Number of nodes expanded: 4
    Max queue size: 6
    It costs 0.0001 sec
    ```

* If you are going to play the game and check different algorithm result: `driver.py`
Run:
    ```
    $ python3 driver.py
    ```
    - Default puzzle:
        ```
        [1, 2, 3]
        [4, 5, 6]
        [7, 0, 8]
        ```

    Expected result:(Suppose we are playing the default puzzle and implement the uniform cost search)

    1. Choose the default puzzle
        ```
        Welcome to my 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own.
        Your choice: 1
        ```

    2. Choose uniform cost search algorithm
        ```
        Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) for the Manhattan Distance Heuristic.
        Your choice: 1
        ```

    3. See the simulation result
        ```
        Puzzle state:
        [1, 2, 3]
        [4, 5, 6]
        [7, 0, 8]
        =========
        Algorithm choice: (1) Uniform Cost Search
        Solution Founded!
        [1, 2, 3]
        [4, 5, 6]
        [7, 0, 8]
        =========
        [1, 2, 3]
        [4, 5, 6]
        [7, 8, 0]
        =========
        Solution depth was 1
        Number of nodes expanded: 3
        Max queue size: 5
        It costs 0.0001 sec
        ```

Note that the default puzzle is an easy one that only needs one step to be solved.

## Play a more complicated puzzle using A* heuristic algorithm
1. Run `driver.py` and follow the instruction from terminal:
    ```
    $ python3 driver.py
    ```

2. Create our own puzzle, let's try to create the following puzzle:
    ```
    [1, 3, 6]
    [5, 0, 2]
    [4, 7, 8]
    ```

    1. Choose to create it on our own
        ```
        Welcome to my 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own.
        Your choice: 2
        ```
    2. Construct it
        ```
        Enter your puzzle, using a zero to represent the blank. Please only enter valid 8-puzzles. Enter the puzzle delimiting the numbers with a space. Type RET only when finished.
        Enter the 1 row: 1 3 6
        Enter the 2 row: 5 0 2
        Enter the 3 row: 4 7 8
        ```
    3. Choose Misplaced Tile as the heuristic function in A* algorithm
        ```
        Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) for the Manhattan Distance Heuristic.
        Your choice: 2
        ```

    4. See the simulation result
        ```
        Puzzle state:
        [1, 3, 6]
        [5, 0, 2]
        [4, 7, 8]
        =========
        Algorithm choice: (2) Misplaced Tile Heuristic
        Solution Founded!
        [1, 3, 6]
        [5, 0, 2]
        [4, 7, 8]
        =========
        [1, 3, 6]
        [5, 2, 0]
        [4, 7, 8]
        =========
        [1, 3, 0]
        [5, 2, 6]
        [4, 7, 8]
        =========
        [1, 0, 3]
        [5, 2, 6]
        [4, 7, 8]
        =========
        [1, 2, 3]
        [5, 0, 6]
        [4, 7, 8]
        =========
        [1, 2, 3]
        [0, 5, 6]
        [4, 7, 8]
        =========
        [1, 2, 3]
        [4, 5, 6]
        [0, 7, 8]
        =========
        [1, 2, 3]
        [4, 5, 6]
        [7, 0, 8]
        =========
        [1, 2, 3]
        [4, 5, 6]
        [7, 8, 0]
        =========
        Solution depth was 8
        Number of nodes expanded: 16
        Max queue size: 15
        It costs 0.0014 sec
        ```

# 🥳 Hope you have fun:)