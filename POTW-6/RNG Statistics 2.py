# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-06/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findLargest' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER a
#  3. INTEGER b
#  4. INTEGER m
#  5. INTEGER n
#  6. INTEGER k
#


def findLargest(s, a, b, m, n, k):
    # Write your code here

    results = list()
    found = False

    s = s % m
    results.append(s)

    if n == 1:
        return results

    for num in range(n-1):
        psuedo = ((s**2) + a * s + b) % m

        # Check for pattern
        if psuedo in results:
            found = True
            position = results.index(psuedo)
            break

        s = psuedo

        results.append(psuedo)

    # Means there is a pattern
    if found:
        # print(f"Found at {position}")
        pattern = results[position:]
        extra = results[:position]

        pattern_length = len(pattern)
        extra_length = len(extra)

        repeats = (n-extra_length) // pattern_length
        remainder = (n-extra_length) - (repeats*pattern_length)

        results = extra + (pattern*repeats) + pattern[:remainder]

    if k == 1:
        return [max(results)]

    results.sort()

    return results[n-k:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    a = int(first_multiple_input[1])

    b = int(first_multiple_input[2])

    m = int(first_multiple_input[3])

    second_multiple_input = input().rstrip().split()

    n = int(second_multiple_input[0])

    k = int(second_multiple_input[1])

    result = findLargest(s, a, b, m, n, k)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
