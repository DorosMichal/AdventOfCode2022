from args import INPUT_FILE
from parse import parse

def is_contained(L1, R1, L2, R2):
    return L2 <= L1 and R1 <= R2

def dont_overlap(L1, R1, L2, R2):
    return R1 < L2 or R2 < L1

def solution():
    with open(INPUT_FILE, 'r') as file:
        ctr = 0
        for line in file:
            L1, R1, L2, R2 = parse("{:d}-{:d},{:d}-{:d}", line.strip()).fixed
            ctr += not dont_overlap(L1, R1, L2, R2)
    return ctr

print(solution())