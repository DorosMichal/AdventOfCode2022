from args import INPUT_FILE
from queue import Queue

LOW = 0
HIGH = 25

def get_moves(possition, board):
    i, j = possition
    n, m = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    moves = []

    for di, dj in directions:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < n and 0 <= new_j < m:
            if board[new_i][new_j] - board[i][j] <= 1:
                moves.append((new_i, new_j))
    return moves


def bfs(start, end, board):
    q = Queue()
    q.put((start, 0))
    visited = set()
    while not q.empty():
        current_pos, depth = q.get()
        visited.add(current_pos)
        if current_pos == end:
            return depth
            
        for dest in get_moves(current_pos, board):
            if dest in visited:
                continue
            visited.add(dest)
            q.put((dest, depth + 1))


def solution():
    board = []
    starts = []
    end = None
    with open(INPUT_FILE, 'r') as file:
        for i, line in enumerate(file):
            row = []
            for j, let in enumerate(line.strip()):
                if let == 'S':
                    starts.append((i, j))
                    row.append(LOW)
                elif let == 'E':
                    end = (i, j)
                    row.append(HIGH)
                else:
                    height = ord(let) - ord('a')
                    if height == 0:
                        starts.append((i, j))
                    row.append(height)
            board.append(row)

    results = [res for start in starts if (res:=bfs(start, end, board)) is not None]
    return min(results)

print(solution())