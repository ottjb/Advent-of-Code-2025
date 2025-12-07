"""
Advent of Code 2025 - Day 5
"""

import time


def parse_input(input_text):
    """Parse the input"""
    lines = input_text.strip().split("\n")
    return lines


def part1(ranges, items):
    """Solve part 1"""
    count = 0
    for itm in items:
        valid = False
        for rng in ranges:
            if valid:
                break
            if itm >= rng[0] and itm <= rng[1]:
                count += 1
                valid = True
    return count


def part2(ranges):
    """Solve part 2"""
    ranges = merge_ranges(ranges)
    count = 0
    for r in ranges:
        count += (r[1] - r[0]) + 1
    return count


def sort_ranges(ranges):
    new_ranges = ranges
    while True:
        swapped = False
        for i in range(len(new_ranges) - 1):
            if new_ranges[i][0] > new_ranges[i + 1][0]:
                new_ranges[i], new_ranges[i + 1] = new_ranges[i + 1], new_ranges[i]
                swapped = True
        if not swapped:
            break
    return new_ranges


def merge_ranges(ranges):
    r = sort_ranges(ranges)
    merged = [r[0]]
    for current in r[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    return merged


if __name__ == "__main__":
    with open("day05/input.txt") as f:
        input_text = f.read()

    data = parse_input(input_text)
    idx = data.index("")
    ranges = [r.split("-") for r in data[:idx]]
    ranges = [[int(r) for r in rng] for rng in ranges]
    items = [int(i) for i in data[idx + 1 :]]

    # Part 1
    start = time.perf_counter()
    result1 = part1(ranges, items)
    end = time.perf_counter()
    print(f"Part 1: {result1} ({(end - start) * 1000:.2f}ms)")

    # Part 2
    start = time.perf_counter()
    result2 = part2(ranges)
    end = time.perf_counter()
    print(f"Part 2: {result2} ({(end - start) * 1000:.2f}ms)")
