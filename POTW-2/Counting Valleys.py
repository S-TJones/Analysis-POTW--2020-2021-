# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-02/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    sea_level = 0
    print(path)

    for step in range(steps):
        if path[step] == "U":
            sea_level += 1
        else:
            sea_level -= 1

        # Checks for Mountain or Valley
        if sea_level > 0:
            is_valley = False
        elif sea_level < 0:
            is_valley = True

        # Check to see if we made it back to sea level, which is zero
        if sea_level == 0 and is_valley:
            valleys += 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
