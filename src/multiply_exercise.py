import sys
import basetest
import random

def has_correct_output():
    print('Checking output...')
    if basetest.simple_test(list(sys.argv[1]), [5, 4], [20]):
        print('Correct output :)')
    else:
        print('Failed to output the correct value')
    print('')

def passes_random_inputs():
    print('Checking output with random inputs...')
    passes = True
    iterations = 50
    for i in range(0, iterations):
        x = random.randint(1, 40)
        y = random.randint(1, 40)
        if not basetest.simple_test(list(sys.argv[1]), [x, y], [x * y]):
            passes = False
            break
    if passes:
        print('Correct output on', iterations, 'random tests :)')
    else:
        print('Failed to output the correct value on random tests')
    print('')

def has_correct_output_and_data():
    print('Strictly checking output and data tape...')
    if basetest.strict_test(list(sys.argv[1]), [5, 4], [20], [5, 4, 20]):
        print('Correct data tape :)')
    else:
        print('Your data tape needs to match the spec')
    print('')


has_correct_output()
passes_random_inputs()
has_correct_output_and_data()