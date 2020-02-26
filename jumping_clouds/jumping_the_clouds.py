#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    """
         the input is the number of clouds, and the type of cloud we are working with
    """
    inputLength = len(c)
    valueChecks = 0
    jump = False
    print(c)
    for number in range(len(c)):
        print(c[number])
        if c[number] == '0':
            if number != (inputLength - 1):
                if c[number+1] == '0':
                    valueChecks += 1
                else:
                    if c[number+2] == '0':
                        jump = True
                        valueChecks += 1

    return valueChecks

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(input())
    print(c)

    result = jumpingOnClouds(c)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
