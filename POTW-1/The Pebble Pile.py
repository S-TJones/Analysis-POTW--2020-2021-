# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-01/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'count_pebbles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER d
#  3. INTEGER_ARRAY queries
#


def count_pebbles(k, d, queries):
    # Count the total number of pebbles accumulated after the number of days indicated by each query

    total_pebble_list = list()

    max_day = max(queries)

    start_day = 1
    total_pebble = 0
    pebble_list = list()

    for query in queries:
        # Arithmetic Progression formula
        L = k + ((query-1) * k)
        pebble_amount = (query * (k + L)) // 2

        stolen_days = query // d
        stolen_pebbles = stolen_days * (k * d)

        pebble_amount -= stolen_pebbles

        total_pebble_list.append(pebble_amount)

    return total_pebble_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    k = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    queries = list(map(int, input().rstrip().split()))

    result = count_pebbles(k, d, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
