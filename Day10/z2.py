from args import INPUT_FILE

def solution():
    def nop():
        return lambda register: register

    def add(to_add):
        return lambda register: register + to_add

    with open(INPUT_FILE, 'r') as file:
        INTERVAL = 40
        START_VALUE = 20
        X = 40
        Y = 6

        cycles = 0
        added_cycles = 0
        register = 1
        signal_sum = 0
        operation = nop()
        result = [['.']*X for _ in range(Y)]

        for line in file:
            command = line.strip().split()
            match command:
                case ['noop']:
                    added_cycles = 1
                    operation = nop()
                case ['addx', arg]:
                    added_cycles = 2
                    operation = add(int(arg))

            for i in range(added_cycles):
                # draw pixel
                x_pos = cycles % X
                y_pos = cycles // X
                if abs(register - x_pos) <= 1:
                    result[y_pos][x_pos] = '#'

                cycles += 1
                    
            register = operation(register)
            
        return result
                    

for row in solution():
    print("".join(row))