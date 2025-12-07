"""
Advent of Code 2025 - Day 7
"""

import time
from functools import cache


def parse_input(input_text):
    """Parse the input"""
    lines = input_text.strip().split("\n")
    return lines


def part1(grid):
    tachyons = []
    splitters = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                tachyons.append([x, y])
            elif grid[y][x] == "^":
                splitters.append([x, y])
    splits = 0
    for i in range(len(grid)):
        new_tachyons = []
        for t in tachyons:
            t[1] += 1
            if t in splitters:
                splits += 1
                new_tachyons.append([t[0] + 1, t[1]])
                t[0] -= 1
        tachyons = tachyons + new_tachyons
        tachyons = remove_duplicates(tachyons)

    return splits


def remove_duplicates(l):
    new_list = []
    for x in l:
        if x not in new_list:
            new_list.append(x)
    return new_list


@cache
def path(gridHeight, splitters, x, y):
    y += 1
    if (x, y) in splitters:
        return path(gridHeight, splitters, x - 1, y) + path(
            gridHeight, splitters, x + 1, y
        )
    elif y >= gridHeight:
        return 1
    else:
        return path(gridHeight, splitters, x, y)


def part2(grid):
    tachyon = None
    splitters = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                tachyon = [x, y]
            elif grid[y][x] == "^":
                splitters.append((x, y))
    splitters_set = frozenset(splitters)
    return path(len(grid), splitters_set, tachyon[0], tachyon[1])


if __name__ == "__main__":
    with open("day07/input.txt") as f:
        input_text = f.read()

    data = parse_input(input_text)
    data = [list(x) for x in data]

    # Part 1
    start = time.perf_counter()
    result1 = part1(data)
    end = time.perf_counter()
    print(f"Part 1: {result1} ({(end - start) * 1000:.2f}ms)")

    # Part 2
    start = time.perf_counter()
    result2 = part2(data)
    end = time.perf_counter()
    print(f"Part 2: {result2} ({(end - start) * 1000:.2f}ms)")
