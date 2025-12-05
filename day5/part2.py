"""AoC_Year2025_Day5_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

ranges = []
with open(INPUT_PATH, "r") as file:

    for range_ in file.readlines():
        if range_ == "\n":
            break
        start, end = map(int, range_.split("-"))
        ranges.append((start, end))


def merge_intervals(intervals: list[tuple[int, int]]):

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1] + 1:
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged.append(current)

    return merged


fresh = 0
merged_ranges = merge_intervals(ranges)
for start, end in merged_ranges:
    fresh += end - start + 1

print(fresh)
