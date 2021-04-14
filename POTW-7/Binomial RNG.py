# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-07/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import accumulate
from collections import Counter

#
# Complete the 'countFrequencies' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER_ARRAY watch
#  3. INTEGER_ARRAY binomial_parms
#  4. INTEGER_ARRAY lcrng_parms
#

# ------------------------- Helper Functions -----------------------

# Gets the list of Binomial Distributions


def getBinomialDistribution(n, p):

    distribution_values = list()

    for k in range(n+1):
        n_k = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
        value = n_k * (p ** k) * ((1-p) ** (n-k))

        distribution_values.append(value)

    return distribution_values

# -----------------------------------------------------------------


def countFrequencies(s, watch, binomial_parms, lcrng_parms):
    # Count frequencies of outcomes in watch after drawing s samples
    # from RNG derived from lcrng_parms with binomial_parms

    # Assign all values
    a = lcrng_parms[0]
    b = lcrng_parms[1]
    m = lcrng_parms[2]
    x0 = lcrng_parms[3] % m

    n = binomial_parms[0]
    pn = binomial_parms[1]
    pd = binomial_parms[2]
    p = pn / pd

    # Map all watch-values
    watch_count = dict()
    for num in watch:
        watch_count[num] = 0

    distribution_list = getBinomialDistribution(n, p)

    # Get all values of K
    def sum_of_all(x, y): return (x+y)
    all_k_values = list(accumulate(distribution_list, sum_of_all))
    length = len(all_k_values)

    # Generate a sequence of integers
    random_sequence = list()
    random_sequence.append(x0)

    for _ in range(1, s):
        x0 = ((a*x0) + b) % m
        random_sequence.append(x0)
    # --------------------------------------------------------------------

    sequences = dict(Counter(random_sequence))

    for number, count in sequences.items():
        k = number / m

        start = 0
        end = length - 1

        # Check for 'K' first...
        # if k in all_k_values:
        #     position = all_k_values.index(k)
        #     watch_count[position] += count
        #     continue

        # ... if not, then Binary Search for a new location
        while (start <= end):

            middle = (start + end) // 2
            search = all_k_values[middle]

            # I don't think 'K' will ever be in the list...
            # ... so therefore I don't need to check the middle anymore
            if search < k:
                start = middle + 1

            if search > k:
                end = middle-1

        # Identifies where 'K' should be in the list
        location = end + 1
        if location in watch_count.keys():
            watch_count[location] += count

    return list(watch_count.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lcrng_parms = list(map(int, input().rstrip().split()))

    binomial_parms = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    watch = list(map(int, input().rstrip().split()))

    result = countFrequencies(s, watch, binomial_parms, lcrng_parms)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
