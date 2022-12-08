from args import INPUT_FILE

from args import INPUT_FILE
import numpy as np

directions = [(1,0), (0,1), (-1,0), (0,-1)]

def get_score_for_direction(i, j, direction, board):
    current_high = board[i, j]
    n, m = board.shape
    di, dj = direction

    score = 0
    while True:
        i += di
        j += dj
        if (0 <= i < n and 0 <= j < m):
            score += 1
            if board[i, j] < current_high:
                continue
        return score


def solution():
    with open(INPUT_FILE, 'r') as file:
        lines = file.readlines()

    board = np.array([
        [int(el) for el in line.strip()]
        for line in lines
    ], dtype=np.int32)
    
    n, m = board.shape
    best_score = 0
    for i in range(n):
        for j in range(m):
            score = 1
            for direction in directions:
                score *= get_score_for_direction(i, j, direction, board)
            best_score = max(score, best_score)

    return best_score


print(solution())