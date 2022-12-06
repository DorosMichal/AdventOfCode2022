from args import INPUT_FILE
from operator import and_
from functools import reduce
ELF_GROUP_SIZE = 3

def get_item_priority(item: str):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def group_by_k(iterator, k):
    while True:
        try:
            yield [next(iterator) for _ in range(k)]
        except StopIteration:
            break

def get_badge(elf_group: list[str]):
    return reduce(and_, map(set, elf_group)).pop()

def solution():
    with open(INPUT_FILE, 'r') as file:
        result = 0
        for elf_group_raw in group_by_k(iter(file), ELF_GROUP_SIZE):
            elf_group = map(str.strip, elf_group_raw)
            badge = get_badge(elf_group)

            result += get_item_priority(badge)

    return result

print(solution())