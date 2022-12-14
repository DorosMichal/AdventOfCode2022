from itertools import zip_longest
from typing import Any, List, Union
from args import INPUT_FILE

def group_by_k(iterator, k: int):
    while True:
        try:
            yield [next(iterator) for _ in range(k)]
        except StopIteration:
            break

def sgn(num: int) -> int:
    if num > 0: return 1
    if num == 0: return 0
    return -1

def to_list(arg: Union[List[Any], int]):
    return [arg] if isinstance(arg, int) else arg

def compare_packets(packet1, packet2):
    if isinstance(packet1, int) and isinstance(packet2, int):
        return sgn(packet2 - packet1)
    packet1 = to_list(packet1)
    packet2 = to_list(packet2)
    for e1, e2 in zip_longest(packet1, packet2):
        if e1 is None: return 1
        if e2 is None: return -1
        res = compare_packets(e1, e2)
        if res != 0: 
            return res
    return 0
    

def solution():
    with open(INPUT_FILE, 'r') as file:
        pair_ctr = 1
        proper_indices_sum = 0
        for line1, line2, _ in group_by_k(file, 3):
            packet1 = eval(line1.strip())
            packet2 = eval(line2.strip())
            if compare_packets(packet1, packet2) == 1:
                proper_indices_sum += pair_ctr
            pair_ctr += 1
    return proper_indices_sum
print(solution())