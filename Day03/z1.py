from args import INPUT_FILE

def get_duplicated_item(backpack: str):
    n = len(backpack) // 2
    return (set(backpack[:n]) & set(backpack[n:])).pop()

def get_item_priority(item: str):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def solution():
    with open(INPUT_FILE, 'r') as file:
        result = 0
        for line in file:
            item = get_duplicated_item(line.strip())
            result += get_item_priority(item)

    return result

print(solution())