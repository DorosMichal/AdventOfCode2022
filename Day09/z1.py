from args import INPUT_FILE

direction_map = {
    'U': complex(0, 1),
    'R': complex(1, 0),
    'L': complex(-1, 0),
    'D': complex(0, -1)
}

def move_closer(src, dest):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return min((src + complex(a,b) for a, b in dirs), key=lambda x: abs(dest - x))


def solution():
    start = complex(0,0)
    NUMBER_OF_KNOTS = 2
    knots = [start for _ in range(NUMBER_OF_KNOTS)]
    visited_possitions = set()
    visited_possitions.add(start)

    with open(INPUT_FILE, 'r') as file:
        for line in file:
            direction, n = line.split()
            for _ in range(int(n)):
                knots[0] += direction_map[direction]
                for i in range(1, NUMBER_OF_KNOTS):
                    if abs(knots[i-1] - knots[i]) >= 2:
                        knots[i] = move_closer(knots[i], knots[i-1])
                visited_possitions.add(knots[-1])
        
    return len(visited_possitions)



print(solution())