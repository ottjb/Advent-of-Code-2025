"""
Advent of Code 2025 - Day 6
"""

import time


def parse_input(input_text):
    """Parse the input"""
    lines = input_text.strip().split("\n")
    return lines


def parse_input_p2(input_text):
    """Parse the input"""
    lines = input_text.split("\n")
    return lines


def part1(data):
    """Solve part 1"""
    for i in range(len(data)):
        if data[i][0] == "+" or data[i][0] == "*":
            data[i] = process_row(data[i], False)
        else:
            data[i] = process_row(data[i])
    total = 0
    for i in range(len(data[0])):
        nums = []
        for j in range(len(data) - 1):
            nums.append(data[j][i])
        if data[-1][i] == "+":
            total += sum(nums)
        else:
            product = 1
            for n in nums:
                product *= n
            total += product
    return total


def process_row(row, ints=True):
    new_row = row.split(" ")
    new_row = [x for x in new_row if x != ""]
    if ints:
        new_row = [int(x) for x in new_row]
    return new_row


def part2(data):
    """Solve part 2"""
    problems = []
    problem = []
    for i in range(len(data[0])):
        col = []
        for j in range(len(data)):
            n = data[j][i]
            col.append(n)
        if len(set(col)) <= 1:
            problems.append(problem)
            problem = []
        elif i == len(data[0]) - 1:
            problem.append(col)
            problems.append(problem)
        else:
            problem.append(col)

    total = 0
    for p in problems:
        nums, sign = parse_prob(p)
        if sign == "+":
            total += sum(nums)
        else:
            product = 1
            for n in nums:
                product *= n
            total += product
    return total


def parse_prob(prob):
    sign = prob[0][-1]
    nums = []
    for i in range(len(prob)):
        num_str = ""
        for j in range(len(prob[i])):
            item = prob[i][j]
            if item != "+" and item != "*":
                num_str += item
        nums.append(int(num_str))
    return nums, sign


if __name__ == "__main__":
    with open("day06/input.txt") as f:
        input_text = f.read()

    p1_data = parse_input(input_text)
    p2_data = parse_input_p2(input_text)

    # Part 1
    start = time.perf_counter()
    result1 = part1(p1_data)
    end = time.perf_counter()
    print(f"Part 1: {result1} ({(end - start) * 1000:.2f}ms)")

    # Part 2
    start = time.perf_counter()
    result2 = part2(p2_data)
    end = time.perf_counter()
    print(f"Part 2: {result2} ({(end - start) * 1000:.2f}ms)")
