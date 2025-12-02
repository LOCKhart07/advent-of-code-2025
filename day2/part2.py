"""AoC_Year2025_Day2_Part2"""

INPUT_PATH = r"input.txt"
EXAMPLE_INPUT_PATH = r"example1.txt"


import textwrap
from functools import lru_cache

input_ranges = open(INPUT_PATH).read().split(",")


@lru_cache(None)
def is_repeating(n):
    s = str(n)

    for i in range(len(s)):
        parts = textwrap.wrap(s, i + 1)
        # print(f"{n=} {parts=} {set(parts)=} {len(set(parts))=}")
        if len(parts) != 1 and len(set(parts)) == 1:
            return True
    return False


s = 0
for input_range in input_ranges:
    start, end = map(int, input_range.split("-"))
    # print(f"Processing range from {start} to {end}")
    for number in range(start, end + 1):
        if is_repeating(number):
            # print(number)
            s += number

    # print()
print(f"{s=}")
