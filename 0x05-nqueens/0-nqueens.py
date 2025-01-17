#!/usr/bin/python3
""" Module that solves the n queens problem """
import sys


def is_safe(board, row, col, N):
    """ Check if a queen can be placed at board[row][col] """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """ Add solution points to list """
    if col >= N:
        solutions.append([[i, board[i].index(1)] for i in range(N)])
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N, solutions) or res
            board[i][col] = 0  # backtrack

    return res


def solve_nqueens(N):
    """ Solve the n queens """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    if not solve_nqueens_util(board, 0, N, solutions):
        print("No solutions found.")
    else:
        for solution in solutions:
            print(solution)


def main():
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

    solve_nqueens(N)


if __name__ == "__main__":
    main()
