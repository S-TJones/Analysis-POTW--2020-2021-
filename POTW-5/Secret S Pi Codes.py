# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-05/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

# Special imports
from functools import reduce
from operator import mul
from itertools import accumulate

from collections import Counter

# Helper Function from Dr.Fokums Project 1 - Modified


def ext_Euclid(m, n):
    """Extended Euclidean algorithm. It returns the multiplicative
        inverse of n mod m"""

    a = (1, 0, m)
    b = (0, 1, n)

    while True:
        if b[2] == 0:
            return a[2]
        if b[2] == 1:
            # return int(b[1] + (m if b[1] < 0 else 0))
            if b[1] < 0:
                return int(b[1] + m)
            return int(b[1])

        q = math.floor(a[2] / float(b[2]))

        t = (a[0] - (q * b[0]), a[1] - (q*b[1]), a[2] - (q*b[2]))
        a = b
        b = t


# --------------------------------------------------
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    arr = list(map(int, input().rstrip().split()))
    #range_keys = [1] + list(accumulate(arr, mul))

    results = []
    modulo = ((10**9)+7)

    def product_of_all(x, y): return (x*y) % modulo
    range_keys = [1] + list(accumulate(arr, product_of_all))
    #print (range_keys)

    for _ in range(q):
        pair = list(map(int, input().rstrip().split()))
        start = pair[0]-1
        end = pair[1]

        m_inverse = ext_Euclid(modulo, range_keys[start])

        #secret_key = (range_keys[end] // range_keys[start-1])
        #secret_key = reduce(mul, arr[start-1:end])
        secret_key = m_inverse * range_keys[end]

        results.append(secret_key % modulo)

    # ----------------------------------------------------------

    fptr.write('\n'.join(map(str, results)))
    fptr.write('\n')

    fptr.close()
