"""AoC_Year2025_Day4_Part2"""

INPUT_PATH = r"input.txt"
EXAMPLE_INPUT_PATH = r"example1.txt"


from enum import Enum

import numpy as np

grid = []

with open(INPUT_PATH, "r") as f:
    while line := f.readline().strip():
        grid.append(list(map(str, line)))


grid = np.array(grid)
# print(grid)

rows, cols = grid.shape


def check_bounds(pos):
    if pos[1] < 0 or pos[0] < 0 or pos[0] > rows - 1 or pos[1] > cols - 1:
        return False
    return True


class Directions(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    TOP_LEFT = (-1, -1)
    TOP_RIGHT = (1, -1)
    BOTTOM_LEFT = (-1, 1)
    BOTTOM_RIGHT = (1, 1)


ans = 0

keep_running = True
while keep_running:
    keep_running = False
    for x in range(rows):
        for y in range(cols):
            # print(grid[x, y])
            if grid[x, y] == "@":
                nu = 0
                for direction in Directions:
                    dx, dy = direction.value
                    nx, ny = x + dx, y + dy
                    if check_bounds((nx, ny)) and grid[nx, ny] == "@":
                        nu += 1
                    if nu >= 4:
                        break
                else:
                    ans += 1
                    grid[x, y] = "x"
                    keep_running = True

print(ans)
