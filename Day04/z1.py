from args import INPUT_FILE
from parse import parse

def is_contained(L1, R1, L2, R2):
    return L2 <= L1 and R1 <= R2

def solution():
    with open(INPUT_FILE, 'r') as file:
        ctr = 0
        for line in file:
            L1, R1, L2, R2 = parse("{:d}-{:d},{:d}-{:d}", line.strip()).fixed
            ctr += is_contained(L1,R1,L2,R2) or is_contained(L2,R2, L1,R1)
    return ctr

print(solution())