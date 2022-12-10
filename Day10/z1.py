from args import INPUT_FILE

def solution():
    def nop():
        return lambda register: register

    def add(to_add):
        return lambda register: register + to_add

    with open(INPUT_FILE, 'r') as file:
        INTERVAL = 40
        START_VALUE = 20

        cycles = 0
        added_cycles = 0
        register = 1
        signal_sum = 0
        operation = nop()

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
                cycles += 1

                if START_VALUE <= cycles and (cycles - START_VALUE) % INTERVAL == 0:
                    signal_sum += cycles * register
                    
            register = operation(register)
            
        
        return signal_sum
                    

print(solution())