import sys
import basetest
import random

def has_correct_output():
    print('Checking output for initialise 5...')
    if basetest.simple_test(list(sys.argv[1]), [], [5]):
        print('Correct output :)')
    else:
        print('Failed to output the correct value')
    print('')


has_correct_output()