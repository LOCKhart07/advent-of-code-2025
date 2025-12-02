"""AoC_Year2025_Day2_Part1"""

INPUT_PATH = r"input.txt"
EXAMPLE_INPUT_PATH = r"example1.txt"


input_ranges = open(INPUT_PATH).read().split(",")


def is_repeating(n):
    s = str(n)
    mid = len(s) // 2
    return s[:mid] == s[mid:]


s = 0
for input_range in input_ranges:
    start, end = map(int, input_range.split("-"))
    for number in range(start, end + 1):
        if is_repeating(number):
            s += number

print(f"{s}")
