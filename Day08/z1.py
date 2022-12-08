from args import INPUT_FILE
import numpy as np

def solution():
    with open(INPUT_FILE, 'r') as file:
        lines = file.readlines()

    board = np.array([
        [int(el) for el in line.strip()]
        for line in lines
    ], dtype=np.int32)
    visible_trees = np.zeros(board.shape, dtype=np.int8)
    for direction in range(4):
        n, m = board.shape
        for i in range(n):
            pref_max = -1
            for j in range(m):
                if board[i, j] > pref_max:
                    visible_trees[i, j] = 1
                pref_max = max(pref_max, board[i, j])
        board = np.rot90(board)
        visible_trees = np.rot90(visible_trees)


    return np.sum(visible_trees)



print(solution())