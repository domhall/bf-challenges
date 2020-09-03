def get_data(data, index):
    while len(data) <= index:
        data.append(0)
    return data[index]


def interpret(instructions, data):
    data_index = 0
    instruction_index = 0
    outputs = []
    while(instruction_index < len(instructions)):
        instruction = instructions[instruction_index]
        if instruction == '+':
            data[data_index] = get_data(data, data_index) + 1
        elif instruction == '-':
            data[data_index] = get_data(data, data_index) - 1
        elif instruction == '>':
            data_index += 1
        elif instruction == '<':
            if data_index == 0:
                raise Exception('Tried to move off the tape left')
            data_index -= 1
        elif instruction == '[':
            if get_data(data, data_index) == 0:
                pairs = 1
                while pairs > 0:
                    instruction_index += 1
                    if instructions[instruction_index] == '[':
                        pairs += 1
                    elif instructions[instruction_index] == ']':
                        pairs -= 1
        elif instruction == ']':
            if get_data(data, data_index) != 0:
                pairs = 1
                while pairs > 0:
                    instruction_index -= 1
                    if instructions[instruction_index] == '[':
                        pairs -= 1
                    elif instructions[instruction_index] == ']':
                        pairs += 1
        elif instruction == '.':
            outputs.append(get_data(data, data_index))
        instruction_index += 1
    return (outputs, data)