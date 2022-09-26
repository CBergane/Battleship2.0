import random

"""
Create Battle Grid
"""


def build_grid(grid):
    return [["O" for count in range(grid)] for count in range(grid)]


print(build_grid(8))