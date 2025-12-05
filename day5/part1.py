"""AoC_Year2025_Day5_Part1"""

INPUT_PATH = r"input.txt"
EXAMPLE_INPUT_PATH = r"example1.txt"


ranges = []
ids = []
with open(INPUT_PATH, "r") as file:
    flag_ranges = True
    for range_ in file.readlines():
        if range_ == "\n":
            flag_ranges = False
            continue

        if flag_ranges:
            start, end = map(int, range_.split("-"))
            ranges.append((start, end))
        else:
            id = int(range_.strip())
            ids.append(id)


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
for id in ids:
    for start, end in merged_ranges:
        # if id < start:
        #     print(f"{id} is spoiled")
        #     break
        if start <= id <= end:
            # print(f"{id} is fresh")
            fresh += 1
            break
    else:
        # print(f"{id} is spoiled")
        pass

print(fresh)
