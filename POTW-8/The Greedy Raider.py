# Link to the Hackerrank exercise: https://www.hackerrank.com/contests/uwi-comp2211-2021-potw-08/challenges

# -----------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findShortestValuablePath function below.
def findShortestValuablePath(height, width, maze, values, t):

    # --------------------- Helper Functions ------------------------------------------------------------

    # Generates a list of possible positions as tuples from a starting position...
    # ... without including thorn locations.
    def possibleMoves(position):

        validPositions = [((position[0] + x), (position[1] + y)) for x, y in movement_options if (
            0 < (position[0] + x) <= height) and (0 < (position[1] + y) <= width)]

        return validPositions

    # Recursive Helper Function ------------------------------------------------------------------------
    def pathFinder(start, steps, total, target, visited):
        # Base Case
        if total >= target:
            return steps
        else:
            # Update the steps
            steps += 1

            visited.add(start)
            go_where = (set(possibleMoves(start)) - walls) - visited
            # print(go_where, "Go here")

            # print(total, "T-before", "add-", position_value[start])
            total += position_value[start]
            # print("T-",total, "when ",start, "Step-", steps)

            # Check for "No more options"
            if len(go_where) == 0:
                return 999

            lst = [999]
            for possible_move in go_where:
                lst.append(pathFinder(possible_move,
                                      steps, total, target, visited))

            return min(lst)
    # ---------------------------------------------------------------------------------------------------

    # print(m, n, maze, values, t)

    start = None
    overall_total = 0  # Keeps track of the total treasures in the Maze
    position_value = dict()

    # Possible positions - Calculator?
    # This can be used to generate all 4 possible moves for the Rabbit in '+' format
    movement_options = [[-1, 0], [0, -1], [+1, 0], [0, +1]]

    # Should store all wall locations
    walls = set()

    # Determines all wall locations--------------------------------------------------------------------
    x = 1
    for row in maze:

        y = 1
        for char in row:

            location = (x, y)

            # Checks for specific characters
            if char == "#":
                walls.add(location)
            elif char == "M":
                walls.add(location)
                walls.update(possibleMoves(location))
            elif char == "S":
                start = location
                position_value[location] = 0
            elif char == ".":
                position_value[location] = 0
            else:
                overall_total += values[int(char)]
                position_value[location] = values[int(char)]

            y += 1
        x += 1

    # print(f"PV-  {position_value}\nStart- {start}\nWalls- {walls}")
    # -------------------------------------------------------------------------------------------------

    # print(overall_total, "-MAX")
    if overall_total < t:
        return -1

    result = 0
    result = pathFinder(start, -1, 0, t, set())
    # print(result)
    #result = min( result )

    if result == 999:
        return -1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mnt = input().rstrip().split()

    m = int(mnt[0])

    n = int(mnt[1])

    t = int(mnt[2])

    maze = []

    for _ in range(m):
        maze_item = input()
        maze.append(maze_item)

    values = list(map(int, input().rstrip().split()))

    result = findShortestValuablePath(m, n, maze, values, t)

    fptr.write(str(result) + '\n')

    fptr.close()
