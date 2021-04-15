# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-08/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the function below.

# --------------------- Helper Functions -------------------------

# Generates a list of possible positions as tuples from a starting position...
# ... without including thorn locations.
def possibleMoves(position, x_limit, y_limit, movement_options, low_row, low_col):

    #     validPositions = []

    #     for [x, y] in movement_options:

    #         xCandidate = position[0] + x
    #         yCandidate = position[1] + y

    #         # Respective location
    #         location = [xCandidate, yCandidate]

    #         if (0 <= xCandidate < x_limit) and (0 <= yCandidate < y_limit):
    #             validPositions.append( (xCandidate, yCandidate) )

    # List comprehension version
    validPositions = [((position[0] + x), (position[1] + y)) for x, y in movement_options if (
        low_row <= (position[0] + x) < x_limit) and (low_col <= (position[1] + y) < y_limit)]

    return validPositions


def countHops(m, n, pr, pc, a, b, br, bc):
    # Write your code here.

    # Mark the starting and target location
    starts = (a, b)
    squash = (br, bc)

    # Store the value of the lowest row and column - can be updated for efficiency
    low_row, low_col = 0, 0

    # Possible positions - Calculator?
    # This can be used to generate all 8 possible moves for the Rabbit in 'L' format
    movement_options = [(-pc, -pr), (-pc, +pr), (+pc, -pr),
                        (+pc, +pr), (-pr, -pc), (-pr, +pc), (+pr, -pc), (+pr, +pc)]

    # Check for the Squash in respective to the Rabbits location
    if a < br:
        """
            If the starting row is less than the Squash's row; 
            Meaning, the Squash is 'below' the Rabbit on the grid.
        """

        # Update the lowest row value, so the code doesn't check for 'jump' locations above the Rabbit
        low_row = a

        if b < bc:
            """
                If the starting column is less than the Squash's column; 
                Meaning, the Squash is on the 'right' of the Rabbit on the grid.
            """
            low_col = b  # Update, and don't check 'jump' locations on the left of the Rabbit

        elif b > bc:
            """
                If the starting column is greater than the Squash's column; 
                Meaning, the Squash is on the 'left' of the Rabbit on the grid.
            """
            n = b  # Update, and don't check 'jump' locations on the right of the Rabbit

    elif a > br:
        """
            If the starting row is greater than the Squash's row; 
            Meaning, the Squash is 'above' the Rabbit on the grid.
        """

        # Update the lowest row value, so the code doesn't check for 'jump' locations below the Rabbit
        m = a

        if b < bc:
            low_col = b

        elif b > bc:
            n = b
    else:

        if b < bc:
            low_col = b

        elif b > bc:
            n = b

    # Gets the next possible moves from the starting location
    next_plots = set(possibleMoves(
        starts, m, n, movement_options, low_row, low_col))

    """----------------------------------------------------"""
    # Check if it's within 1 move
    # if squash in next_plots:
    # return 1
    """----- There was no need for this check ^ above -----"""

    # Keeps track of all visited plots
    tracker = set([starts])

    # Tracks the count and every plot available for that move
    count = 1

    plots_length = len(next_plots)
    while plots_length:

        # Update the moves counter
        count += 1
        tracker.update(next_plots)

        # Get all possible plots to move to - Unvisited plots we can travel to
        possible_plots = set()
        for plot in next_plots:
            possible_plots.update(possibleMoves(
                plot, m, n, movement_options, low_row, low_col))

        # Check for squash
        # print(count, "possible -", possible_plots)
        if squash in possible_plots:
            return count

        # Get the next avaiable 'unchecked' plots to visit...
        # ...then add them to the list, excluding the ones we just checked.
        next_plots = possible_plots - tracker

        # Update length
        plots_length = len(next_plots)

        # print(f"others - {next_plots}")

    # print("T-",tracker)
    return "No Squash"


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    mn = input().split()

    m = int(mn[0])
    n = int(mn[1])

    prpc = input().split()

    pr = int(prpc[0])
    pc = int(prpc[1])

    ab = input().split()

    a = int(ab[0])
    b = int(ab[1])

    brbc = input().split()

    br = int(brbc[0])
    bc = int(brbc[1])

    h = countHops(m, n, pr, pc, a, b, br, bc)

    f.write(str(h) + "\n")

    f.close()
