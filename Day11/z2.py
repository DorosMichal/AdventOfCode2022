from args import INPUT_FILE
from operator import add, mul
from queue import Queue
from parse import parse
from heapq import nlargest

global_test = 1

class Test:
    def __init__(self, divisible_by, if_true, if_false):
        global global_test
        global_test *= divisible_by
        self.divisible_by = divisible_by
        self.if_true = if_true
        self.if_false = if_false

    def __call__(self, worry_level):
        return self.if_true if worry_level % self.divisible_by == 0 else self.if_false

class Operation:
    def __init__(self, e1, op, e2):
        self.op = {'+': add, '*': mul}[op]
        self.e1 = e1
        self.e2 = e2

    def __call__(self, old):
        e1 = old if self.e1=='old' else int(self.e1)
        e2 = old if self.e2=='old' else int(self.e2)
        return self.op(e1, e2)

class Monkey:
    def __init__(self, items, operation, test):
        self.items = Queue()
        for item in items:
            self.items.put(item)
        self.operation = operation
        self.test = test
        self.inspections_performed = 0

    def __repr__(self):
        items = []
        while not self.items.empty():
            items.append(self.items.get())
        res = f"Monkey with items {items}"
        for item in items:
            self.items.put(item)
        print(self.items.qsize())
        return res

    def play_round(self, monkeys):
        while not self.items.empty():
            self._play_turn(monkeys)

    def _play_turn(self, monkeys):
        item_worry = self.items.get()
        self.inspections_performed += 1
        item_worry = self.operation(item_worry)
        item_worry = item_worry % global_test
        pass_to = self.test(item_worry)
        self.pass_item(item_worry, monkeys[pass_to])

    def pass_item(self, item, receiving_mokey):
        receiving_mokey.receive_item(item)

    def receive_item(self, item):
        self.items.put(item)

def parse_monkey(lines):
    lines = [line.strip() for line in lines]
    items = parse("Starting items: {}", lines[1]).fixed
    expression = parse("Operation: new = {} {} {}", lines[2]).fixed
    divisible_by = parse("Test: divisible by {:d}", lines[3]).fixed[0]
    if_true = parse("If true: throw to monkey {:d}", lines[4]).fixed[0]
    if_false = parse("If false: throw to monkey {:d}", lines[5]).fixed[0]

    items = [int(item) for item in items[0].split(',')]
    operation = Operation(*expression)
    test = Test(divisible_by, if_true, if_false)

    return Monkey(items, operation, test)

def group_by_k(iterator, k):
    while True:
        try:
            yield [next(iterator) for _ in range(k)]
        except StopIteration:
            break

def solution():
    LINES_PER_MONKEY = 7
    NUM_OF_ROUNDS = 10000
    monkeys = []
    with open(INPUT_FILE, 'r') as file:
        for lines in group_by_k(file, LINES_PER_MONKEY):
            monkey = parse_monkey(lines)
            monkeys.append(monkey)

    for _ in range(NUM_OF_ROUNDS):
        for monkey in monkeys:
            monkey.play_round(monkeys)
    
    inspected_items = [monkey.inspections_performed for monkey in monkeys]
    best1, best2 = nlargest(2, inspected_items)
    return best1 * best2

print(solution())