from enum import Enum

class Play(Enum):
    ROCK = 0 
    PAPER = 1
    SCISORS = 2

class Result(Enum):
    LOSS = 0
    DRAW = 1 
    WIN = 2

def evaluate_game(opponent: Play, me: Play):
    return Result((me.value - opponent.value + 1) % 3)

def score_for_game(opponent: Play, me: Play):
    result = evaluate_game(opponent, me)
    return 3 * result.value + (me.value + 1)

def get_correct_play(oppontent: Play, result: Result):
    return Play((result.value + oppontent.value - 1) % 3)

def solution(path='input.txt'):
    with open(path, 'r') as file:
        score = 0
        for line in file:
            opponent, result = line.strip().split()
            opponent = Play(ord(opponent) - ord('A'))
            result = Result(ord(result) - ord('X'))
            me = get_correct_play(opponent, result)
            score += score_for_game(opponent, me)

    return score

print(solution('input.txt'))
rock = Play(0)
paper = Play(1)
scisors = Play(2)