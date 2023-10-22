import sys
from typing import List, Tuple

def parse_input(input_str: str) -> List[List[int]]:
    """
        Parse the input string into a Sudoku board.

        Args:
            input_str (str): A string containing 81 characters representing the Sudoku puzzle.

        Returns:
            List[List[int]]: A 9x9 list representing the Sudoku board.
    """
    # Check if the input string has exactly 81 characters
    if len(input_str) != 81:
        raise ValueError("Input string must have 81 characters")
    # Check if string is numeric
    if not input_str.isnumeric():
        raise TypeError("Input string must contain nubmbers only")

    board: List[List[int]] = []
    for i in range(9):
        row = [int(input_str[i * 9 + j]) for j in range(9)]
        board.append(row)
    return board

def print_board(board: List[List[int]]) -> None:
    """
        Print the Sudoku board in a human-readable format.

        Args:
            board (List[List[int]]): The Sudoku board to be printed.
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board: List[List[int]]) -> Tuple[int, int]:
    """
        Find the first empty cell (cell with value 0) in the Sudoku board.

        Args:
            board (List[List[int]]): The Sudoku board.

        Returns:
            Tuple[int, int]: A tuple (row, col) of the first empty cell's coordinates.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

def solve(board: List[List[int]]) -> bool:
    """
    Solve the Sudoku puzzle using a backtracking algorithm.

    Args:
        board (List[List[int]]): The Sudoku board to be solved.

    Returns:
        bool: True if the puzzle is solvable, False if it's not.
    """
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def valid(board: List[List[int]], num: int, pos: Tuple[int, int]) -> bool:
    """
    Check if it's valid to place 'num' at position 'pos' on the Sudoku board.

    Args:
        board (List[List[int]]): The Sudoku board.
        num (int): The number to be placed.
        pos (Tuple[int, int]): The row and column coordinates (row, col).

    Returns:
        bool: True if it's valid, False if it's not.
    """
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py 'sudoku_string'")
    else:
        sudoku_string = sys.argv[1]
        try:
            game_board_start = parse_input(sudoku_string)
            print("Input Sudoku:")
            print_board(game_board_start)
            solved_solution = solve(game_board_start)
            if solved_solution:
                print("Solved Sudoku:")
                print_board(game_board_start)
            else:
                print("This Sudoku is unsolvable")

        except ValueError as e:
            print(f"Invalid input: {e}")
        except TypeError as e:
            print(f"Invalid input: {e}")