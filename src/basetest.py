import interpret

def _compare_data(expected, data):
    if len(expected) > len(data):
        return False
    for i, val in enumerate(expected):
        if val != data[i]:
            return False
    return True

def _test(instructions, initial_data, expected_output, expected_data, strict):
    output, data = interpret.interpret(instructions, initial_data)
    if output != expected_output:
        print('Incorrect output:')
        print('  Expected:', expected_output)
        print('       Got:', output)
    if strict and not _compare_data(expected_data, data):
        print('Incorrect data tape:')
        print('  Expected:', expected_data)
        print('       Got:', data)
    return output == expected_output and ((not strict) or _compare_data(expected_data, data))


def strict_test(instructions, initial_data, expected_output, expected_data):
    return _test(instructions, initial_data, expected_output, expected_data, True)

def simple_test(instructions, initial_data, expected_output):
    return _test(instructions, initial_data, expected_output, [], False)