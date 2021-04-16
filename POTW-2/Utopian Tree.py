# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-02/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.


def utopianTree(n):

    # pow(2,(n+2)//2)-1 if n%2==0 else pow(2,(n+3)//2)-2
    if n % 2 == 0:
        ans = int((n + 2) / 2)
        result = (2 ** ans) - 1
    else:
        ans = int((n + 3) / 2)
        result = (2 ** ans) - 2

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
