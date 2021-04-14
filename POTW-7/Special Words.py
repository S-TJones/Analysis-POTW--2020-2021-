# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-07/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'countSpecialWords' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s
#


def countSpecialWords(k, s):
    # Count the number of k-special 2-letter words that can be formed from s

    memo = dict()
    length = len(s)
    count = 0
    prev_count = 0
    alphabet_value = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M",
                      14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
    alphabet_letter = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
                       "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

    for num in range(length):
        prev_count = count
        letter = s[num]

        # Check for repeats
        if letter in memo.keys():
            count += memo[letter]
            continue

        letter_value = alphabet_letter[letter]
        new_word = s[:num] + s[num+1:]
        word_count = dict(Counter(new_word))

        upper_value = abs(letter_value + k)
        lower_value = abs(letter_value - k)

        # Check for Double
        if (2 * letter_value) == k:
            potential_letter = letter
        else:
            potential_letter = None

        # Check for letter or character
        if upper_value in alphabet_value.keys():
            upper_letter = alphabet_value[upper_value]
        else:
            upper_letter = None

        if lower_value in alphabet_value.keys():
            lower_letter = alphabet_value[lower_value]
        else:
            lower_letter = None

        # Letters exist, add count
        if upper_letter and upper_letter in new_word:
            count += word_count[upper_letter]
        if lower_letter and lower_letter in new_word:
            count += word_count[lower_letter]
        # if potential_letter and potential_letter in new_word:
        #     count += word_count[potential_letter]

        memo[letter] = count-prev_count

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    k = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    s = input()

    result = countSpecialWords(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
