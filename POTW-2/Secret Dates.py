# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-02/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'find_earliest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER m
#  3. INTEGER_ARRAY enc_dates
#

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


def find_earliest(k, m, enc_dates):
    # Decipher the dates and return the earliest one

    # print(enc_dates)
    m_inverse = ext_Euclid(m, k)

    # Collects all deciphered dates
    all_dates = list()
    for date in enc_dates:
        encoded_date = (m_inverse * date) % m
        all_dates.append(encoded_date)

    # print(all_dates)
    return min(all_dates)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    k = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    enc_dates = []

    for _ in range(n):
        enc_dates_item = int(input().strip())
        enc_dates.append(enc_dates_item)

    result = find_earliest(k, m, enc_dates)

    fptr.write(str(result) + '\n')

    fptr.close()
