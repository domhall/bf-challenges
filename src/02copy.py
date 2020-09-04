import sys
import basetest
import random

def has_correct_output():
    print('Checking output for copy 5...')
    if basetest.strict_test(list(sys.argv[1]), [5], [], [5, 5]):
        print('Correct output :)')
    else:
        print('Failed to output the correct value')
    print('')


has_correct_output()