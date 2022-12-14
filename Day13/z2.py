from itertools import zip_longest
from typing import Any, List, Union
from args import INPUT_FILE
from functools import cmp_to_key

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
    DIVIDER_1 = [[2]]
    DIVIDER_2 = [[6]]
    with open(INPUT_FILE, 'r') as file:
        packets = []
        for line in file:
            line = line.strip()
            if line != '':
                packet = eval(line.strip())
                packets.append(packet)
    
    packets.append(DIVIDER_1)
    packets.append(DIVIDER_2)

    packets.sort(key=cmp_to_key(compare_packets), reverse=True)
    divider1_pos = packets.index(DIVIDER_1) + 1
    divider2_pos = packets.index(DIVIDER_2) + 1
            
    return divider1_pos * divider2_pos
    
print(solution())