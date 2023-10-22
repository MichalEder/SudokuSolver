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