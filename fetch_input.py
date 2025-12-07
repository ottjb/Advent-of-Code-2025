import os
import sys
import requests
from pathlib import Path

# Configuration
YEAR = 2025
BASE_URL = f"https://adventofcode.com/{YEAR}/day"
SESSION_FILE = ".session"


def get_session_cookie():
    """Read session cookie from .session file"""
    session_path = Path(__file__).parent / SESSION_FILE

    if not session_path.exists():
        print(f"Error: {SESSION_FILE} file not found!")
        print("\nTo get your session cookie:")
        print("1. Go to https://adventofcode.com")
        print("2. Log in")
        print("3. Open browser dev tools (F12)")
        print("4. Go to Application/Storage > Cookies")
        print("5. Copy the value of the 'session' cookie")
        print(f"6. Paste it into a file named '{SESSION_FILE}' in the repo root")
        sys.exit(1)

    with open(session_path) as f:
        return f.read().strip()


def fetch_input(day, session_cookie):
    """Download input for a specific day"""
    url = f"{BASE_URL}/{day}/input"
    cookies = {"session": session_cookie}

    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        print(f"Day {day} not available yet (404)")
        return None
    elif response.status_code == 400:
        print(f"Day {day} not unlocked yet")
        return None
    else:
        print(f"Error fetching day {day}: {response.status_code}")
        return None


def save_input(day, content):
    """Save input to file"""
    day_dir = Path(__file__).parent / f"day{day:02d}"
    day_dir.mkdir(exist_ok=True)

    input_file = day_dir / "input.txt"
    with open(input_file, "w") as f:
        f.write(content)

    print(f"✓ Saved input for day {day}")


def create_solution_template(day):
    """Create solution file template if it doesn't exist"""
    day_dir = Path(__file__).parent / f"day{day:02d}"
    solution_file = day_dir / "solution.py"
    sample_file = day_dir / "sample_input.txt"

    if solution_file.exists():
        return

    sample_file.touch()

    template = f'''"""
Advent of Code {YEAR} - Day {day}
"""

import time


def parse_input(input_text):
    """Parse the input"""
    lines = input_text.strip().split('\\n')
    return lines


def part1(data):
    """Solve part 1"""
    pass


def part2(data):
    """Solve part 2"""
    pass


if __name__ == "__main__":
    with open("day{day:02d}/input.txt") as f:
        input_text = f.read()
    
    data = parse_input(input_text)
    
    # Part 1
    start = time.perf_counter()
    result1 = part1(data)
    end = time.perf_counter()
    print(f"Part 1: {{result1}} ({{(end - start) * 1000:.2f}}ms)")
    
    # Part 2
    start = time.perf_counter()
    result2 = part2(data)
    end = time.perf_counter()
    print(f"Part 2: {{result2}} ({{(end - start) * 1000:.2f}}ms)")
'''

    with open(solution_file, "w") as f:
        f.write(template)

    print(f"✓ Created solution template for day {day}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_input.py <day> [day2 day3 ...]")
        print("   or: python fetch_input.py all")
        sys.exit(1)

    session_cookie = get_session_cookie()

    if sys.argv[1] == "all":
        days = range(1, 26)
    else:
        days = [int(d) for d in sys.argv[1:]]

    for day in days:
        if not (1 <= day <= 25):
            print(f"Day must be between 1 and 25, got {day}")
            continue

        content = fetch_input(day, session_cookie)
        if content:
            save_input(day, content)
            create_solution_template(day)


if __name__ == "__main__":
    main()
