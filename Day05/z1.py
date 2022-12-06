from args import INPUT_FILE
from parse import parse

def parse_stacks(stack_lines):
    content, numbers = stack_lines[:-1], stack_lines[-1]
    numbers = numbers.strip().split()
    N = int(numbers[-1])

    stacks = [list() for _ in range(N)]
    for line in reversed(content):
        for i, crate in enumerate(line.strip().replace('[','').replace(']', '').split()):
            if crate == '-':
                continue
            else:
                stacks[i].append(crate)
    return stacks
            
def solution():
    with open(INPUT_FILE, 'r') as file:
        stack_lines = []
        while (line := next(file)) != '\n':
            stack_lines.append(line)
        stacks = parse_stacks(stack_lines)
        print(stacks)

        for line in file:
            n, src, dest = parse("move {:d} from {:d} to {:d}\n", line).fixed
            for _ in range(n):
                stacks[dest-1].append(stacks[src-1].pop())

    result = []
    for stack in stacks:
        result.append(stack.pop())

    return "".join(result)

print(solution())