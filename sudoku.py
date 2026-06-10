import random
import copy

def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True


def find_empty_location(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def solve_sudoku(board):
    empty = find_empty_location(board)

    if not empty:
        return True

    row, col = empty
    numbers = list(range(1, 10))
    random.shuffle(numbers)

    for num in numbers:
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def generate_complete_board():
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)
    return board


def generate_puzzle(empty_count=40):
    solution = generate_complete_board()
    puzzle = copy.deepcopy(solution)

    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    for i in range(empty_count):
        r, c = cells[i]
        puzzle[r][c] = 0

    return puzzle, solution