#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    string_length = len(s)
    quotient = n // string_length
    remainder = n % string_length
    number_of_a_in_string = s.count('a')
    number_of_a_in_remainder = s[:remainder].count('a')
    return number_of_a_in_string * quotient + number_of_a_in_remainder

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
