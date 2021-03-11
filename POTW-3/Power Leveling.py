# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-03/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compute_levels' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER x
#  4. INTEGER_ARRAY exc_points
#


def compute_levels(a, b, x, exc_points):
    # Determine the levels attained after each excursion
    """--------------------------------------------------"""
    def calc_level(total_exp):
        level = 0

        # Check for level zero
        if total_exp < a:
            return level, a

        """Determines the current level"""
        level += 1  # Already checked for level-zero
        level_exp = a
        while True:
            level_exp_req = a + (level * b)
            level_exp += level_exp_req

            if total_exp < level_exp:
                return level, level_exp
            level += 1
    """--------------------------------------------------"""

    """--------------------------------------------------"""
    def calc_level_exp(level, total_exp, user_exp):
        """Determines the current level"""
        level += 1  # moves to next level
        level_exp = total_exp

        while True:
            level_exp_req = a + (level * b)
            level_exp += level_exp_req

            if user_exp < level_exp:
                print("Inside", level, total_exp, level_exp)
                return level, level_exp
            level += 1
        return level, level_exp
    """--------------------------------------------------"""

    # print(a,b,x,exc_points)
    all_levels = list()
    curr_exp = x

    # Determines current level
    #level, req_exp = calc_level(curr_exp)
    level, req_exp = calc_level_exp(0, a, curr_exp)
    # all_levels.append(level)

    for exp in exc_points:
        curr_exp += exp

        if curr_exp < req_exp:
            all_levels.append(level)
            continue
        else:
            level, req_exp = calc_level_exp(level, req_exp, curr_exp)
            print(level, req_exp, curr_exp)
            all_levels.append(level)

        # If level doesn't change, add it to the list
        # if level not in all_levels:
            # all_levels.append(level)

    return all_levels


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    e = int(first_multiple_input[3])

    excursions = list(map(int, input().rstrip().split()))

    levels = compute_levels(a, b, x, excursions)

    fptr.write('\n'.join(map(str, levels)))
    fptr.write('\n')

    fptr.close()
