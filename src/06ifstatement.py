import sys
import basetest
import random

def has_correct_true():
    print('Checking output for if true...')
    if basetest.simple_test(list(sys.argv[1]), [1, 5, 4], [5]):
        print('Correct output :)')
    else:
        print('Failed to output the correct value')
    print('')

def has_correct_false():
    print('Checking output for if false...')
    if basetest.simple_test(list(sys.argv[1]), [0, 5, 4], [4]):
        print('Correct output :)')
    else:
        print('Failed to output the correct value')
    print('')

has_correct_true()
has_correct_false()