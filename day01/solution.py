"""
Advent of Code 2025 - Day 1
"""

import time


def parse_input(input_text):
    """Parse the input"""
    lines = input_text.strip().split('\n')
    return lines


def part1(data):
    """Solve part 1"""
    current = 50
    zero_count = 0
    for i in range(len(data)):
        num = get_num(data[i])
        if "L" in data[i]:
            current, _ = rotate_left(current, num)
        if "R" in data[i]:
            current, _ = rotate_right(current, num)
        if current == 0:
            zero_count += 1
    return zero_count

def get_num(str):
    return int(str[1:])

def rotate_left(current, num):
    passes = 0
    while num > 0:
        current -= 1
        if current == 0:
            passes += 1
        elif current == -1:
            current = 99
        num -= 1
    return current, passes

def rotate_right(current, num):
    passes = 0
    while num > 0:
        current += 1
        if current == 100:
            passes += 1
            current = 0
        num -= 1
    return current, passes


def part2(data):
    """Solve part 2"""
    current = 50
    zero_count = 0
    for i in range(len(data)):
        num = get_num(data[i])
        passes = 0
        if "L" in data[i]:
            current, passes = rotate_left(current, num)
        if "R" in data[i]:
            current, passes = rotate_right(current, num)
        zero_count += passes
    return zero_count



if __name__ == "__main__":
    with open("day01/input.txt") as f:
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
