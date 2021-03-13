# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-03/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys


def cons(x, y):
    return [x, y]


def car(p):
    return p[0]


def cdr(p):
    return p[1]


nil = []


def makeBinTree(root, left, right):
    return cons(left, cons(root, right))


emptyTree = nil

# ----- Place your code in this section -----

# Complete the binary tree ADT below


def isEmpty(tree):
    if tree == emptyTree:
        return True
    return False


def root(tree):
    return car(cdr(tree))


def left(tree):
    return car(tree)


def right(tree):
    return cdr(cdr(tree))


def isLeaf(tree):
    if isEmpty(left(tree)) and isEmpty(right(tree)):
        return True
    return False

#
# Complete the 'findNumSpecialPaths' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. BINARY_TREE tree The tree of all links connecting the islands
#  2. INTEGER secret The secret modulus
#  3. INTEGER low The minimum number of treasures on a desirable path
#  4. INTEGER high The maximum number of treasures on a desirable path
#


def findNumSpecialPaths(tree, secret, low, high):
    # Determine the number of paths in tree on which the number of treasures is between low and high

    # Traverses through the tree
    def treeHelper(tree, treasure_count, island_value):
        if isEmpty(tree):
            # record.append(treasure_count)
            return []
        else:
            # Keeps track of the total value per island on each branch
            island_value += root(tree)
            # Checks to see if the total island-value matches the secret
            if island_value % secret == 0:
                treasure_count += 1

            if isLeaf(tree):
                return [treasure_count]
            else:
                return treeHelper(left(tree), treasure_count, island_value) + treeHelper(right(tree), treasure_count, island_value)

    records = treeHelper(tree, 0, 0)
    # print(records)

    # Counts all the total treasure in the list within low-high range
    count = 0
    for total in records:
        if total in range(low, high+1):
            count += 1

    return count

# ---- End of Section containing your answer -----


def buildTreeAndSearch(connections, s, l, h):
    n = len(connections)
    nodes = [None] * (n+1)
    nodes[0] = emptyTree
    for (i, v, j, k) in connections:
        nodes[i] = makeBinTree(v, nodes[j], nodes[k])
    r = findNumSpecialPaths(nodes[1], s, l, h)
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    s = int(first_multiple_input[1])

    l = int(first_multiple_input[2])

    h = int(first_multiple_input[3])

    connections = []

    for _ in xrange(n):
        connections.append(map(int, raw_input().rstrip().split()))

    result = buildTreeAndSearch(connections, s, l, h)

    fptr.write(str(result) + '\n')

    fptr.close()
