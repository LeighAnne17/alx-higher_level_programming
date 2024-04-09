#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                 return False

        for i, j in zip(range(row, -1, -1), range(col, len(board))):
         if board[i][j] == 1:
                return False

        return True

def solve_nqueens(board, row):
    if row == len(board):
        print_solution(board)
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            solve_nqueens(board, row + 1)

            board[row][col] = 0

def print_solution(board):
    print([[r, c] for r, c in enumerate(board) if c])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)

