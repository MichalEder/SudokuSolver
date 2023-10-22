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