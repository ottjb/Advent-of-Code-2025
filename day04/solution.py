"""
Advent of Code 2025 - Day 4
"""

import time

directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]


def parse_input(input_text):
    """Parse the input"""
    lines = input_text.strip().split("\n")
    return lines


def get_bounds(grid):
    return len(grid[0]), len(grid)


def out_of_grid(x, y, width, height):
    return x < 0 or x >= width or y < 0 or y >= height


def part1(data):
    """Solve part 1"""
    width, height = get_bounds(data)
    count = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "@":
                if check_surroundings(x, y, data, width, height) < 4:
                    count += 1
    return count


def check_surroundings(x, y, grid, width, height):
    count = 0
    for dir in directions:
        dx, dy = dir
        newX, newY = x + dx, y + dy
        if not out_of_grid(newX, newY, width, height) and grid[newY][newX] == "@":
            count += 1
    return count


def part2(grid, to_remove=[], start=True):
    width, height = get_bounds(data)
    new_grid = grid
    if not start and len(to_remove) == 0:
        return 0
    for pos in to_remove:
        x, y = pos
        new_grid[y][x] = "."
    remove = []
    for y in range(len(new_grid)):
        for x in range(len(new_grid[0])):
            if new_grid[y][x] == "@":
                if check_surroundings(x, y, new_grid, width, height) < 4:
                    remove.append((x, y))
    return len(remove) + part2(new_grid, remove, False)


if __name__ == "__main__":
    with open("day04/input.txt") as f:
        input_text = f.read()

    data = parse_input(input_text)
    data = [list(string) for string in data]

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
