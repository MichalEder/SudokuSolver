# SudokuSolver

A Python script to solve Sudoku puzzles using a backtracking algorithm.


## Introduction

This Python script provides a command-line interface to solve Sudoku puzzles. It takes a Sudoku puzzle as input and attempts to find a solution using a backtracking algorithm. If a solution exists, it will print the solved puzzle. If no solution is found, it will indicate that the puzzle is unsolvable.

## Features

- Solves Sudoku puzzles of varying difficulty levels.
- Handles invalid input with informative error messages.
- Provides human-readable output of Sudoku puzzles.

## Usage

Change your directory to the project folder:

Run the script with a Sudoku puzzle as a command-line argument. The puzzle should be a string of 81 (row after row) characters where '0' represents empty cells:

python sudoku_solver.py '400006000306500000510370000003900200000020000060001700004500102000003807000100506'
The script will attempt to solve the puzzle and provide the result.
