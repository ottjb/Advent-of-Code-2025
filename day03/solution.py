"""
Advent of Code 2025 - Day 3
"""

import time


def parse_input(input_text):
    """Parse the input"""
    lines = input_text.strip().split("\n")
    return lines


def part1(data):
    """Solve part 1"""
    count = 0
    for bank in data:
        count += int(findNext(bank, 0, 2))
    return count


def part2(data):
    """Solve part 2"""
    count = 0
    for bank in data:
        count += int(findNext(bank, 0, 12))
    return count


def findNext(bank, nextIndex, numbersLeft):
    idx = -1
    largest = 0

    for i in range(nextIndex, len(bank) - (numbersLeft - 1)):
        num = int(bank[i])
        if num > largest:
            idx = i
            largest = num

    if numbersLeft == 1:
        return str(largest)
    else:
        return str(largest) + findNext(bank, idx + 1, numbersLeft - 1)


if __name__ == "__main__":
    with open("day03/input.txt") as f:
        input_text = f.read()

    data = parse_input(input_text)

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
