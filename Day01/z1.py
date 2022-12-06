from queue import PriorityQueue
from args import INPUT_FILE

def get_numbers(path=INPUT_FILE):
    ctr = 0
    with open(path, 'r') as file:
        for line in file:
            try:
                ctr += int(line)
            except ValueError:
                yield ctr
                ctr = 0

def solution():
    K = 3

    top_k = PriorityQueue()
    for i, number in enumerate(get_numbers(INPUT_FILE)):
        top_k.put(number)
        if i >= K:
            top_k.get()
    
    top_k_sum = 0
    while not top_k.empty():
        top_k_sum += top_k.get()

    return top_k_sum

print(solution())