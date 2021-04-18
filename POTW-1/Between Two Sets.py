# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-01/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here

    small_factor = min(a)
    large_factor = max(a)
    small_multiple = min(b)

    # First determine if the smaller number is a factor of larger number
    # if large_factor % small_factor == 0:
    #     main_factor = large_factor
    # else:
    #     main_factor = small_factor * large_factor
    lcm = a[0]

    for num in a[1:]:
        lcm = int(lcm * num / math.gcd(lcm, num))

    main_factor = lcm

    # Get multiples of the main-factor and store them
    multiples = list()
    count = 1

    while count <= small_multiple:
        multiple = count * main_factor

        # If this multiple is larer than the smallest-multiple...
        # ... there's no need to continue
        if multiple > small_multiple:
            break

        # Check if this multiple is a factor of the smallest-multiple
        is_multiple = False

        if small_multiple % multiple == 0:
            for num in b:
                if num % multiple == 0:
                    is_multiple = True
                else:
                    is_multiple = False
                    break
            if is_multiple:
                multiples.append(multiple)

        count += 1

    total_multiples = len(multiples)
    return total_multiples


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
