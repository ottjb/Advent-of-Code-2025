"""
Advent of Code 2025 - Day 2
"""

import time
import re


def parse_input(input_text):
    """Parse the input"""
    lines = input_text.strip().split("\n")
    return lines


def part1(data):
    """Solve part 1"""
    count = 0

    for i in range(len(data)):
        id_range = data[i].split("-")
        id_range[0], id_range[1] = int(id_range[0]), int(id_range[1])
        for num in range(id_range[0], id_range[1] + 1):
            num_str = str(num)
            half = len(num_str) // 2
            if num_str[:half] == num_str[half:]:
                count += num

    return count


def part2(data):
    """Solve part 2"""
    count = 0
    regex = re.compile(r"^(\d+)\1+$")
    for i in range(len(data)):
        x, y = data[i].split("-")
        for num in range(int(x), int(y) + 1):
            match = regex.findall(str(num))
            if match:
                count += num

    return count


if __name__ == "__main__":
    with open("day02/input.txt") as f:
        input_text = f.read()
    data = parse_input(input_text)
    data = data[0].split(",")

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
