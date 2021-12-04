#!/usr/bin/env python

import fileinput
import copy


def check_bingo(board):
    for row in board:
        if row.count("X") == len(board):
            return True

    for col in range(len(board)):
        column = [board[row][col] for row in range(len(board))]
        if column.count("X") == len(board):
            return True

    return False


def mark_num(num, boards):
    for board in boards:
        for r, row in enumerate(board):
            board[r] = ["X" if val == num else val for val in row]


def play(nums, boards):
    first_bingo = last_bingo = None
    bingo_boards = [False for _ in range(len(boards))]
    for num in nums:
        mark_num(num, boards)
        for i, board in enumerate(boards):
            if check_bingo(board):
                if first_bingo is None:
                    first_bingo = copy.deepcopy(board), num
                if not bingo_boards[i]:
                    last_bingo = copy.deepcopy(board), num
                bingo_boards[i] = True

    return first_bingo, last_bingo


def compute_score(board, num):
    return sum([int(val) for row in board for val in row if val != "X"]) * num


def parse_boards(data):
    boards = []
    for i in range(1, len(data)):
        if data[i] == "":
            boards.append([])
            continue
        boards[-1].append(data[i].split())
    return boards


if __name__ == '__main__':
    data = [l.strip() for l in fileinput.input()]
    nums = data[0].split(",")
    boards = parse_boards(data)
    (board_p1, num_p1), (board_p2, num_p2) = play(nums, boards)

    p1 = compute_score(board_p1, int(num_p1))
    p2 = compute_score(board_p2, int(num_p2))

    assert p1 == 16716
    assert p2 == 4880
    print("p1:", p1, " p2:", p2)
