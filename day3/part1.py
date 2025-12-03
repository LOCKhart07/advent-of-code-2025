"""AoC_Year2025_Day3_Part1"""

INPUT_PATH = r"input.txt"
EXAMPLE_INPUT_PATH = r"example1.txt"


with open(INPUT_PATH, "r") as f:
    banks = [list(map(int, line.strip())) for line in f]


total_joltage = 0
for bank in banks:
    # print(bank)
    max_value = float("-inf")
    max_index = -1
    for i in range(0, len(bank) - 1):
        if bank[i] > max_value:
            max_value = bank[i]
            max_index = i

    other_max_value = max(bank[max_index + 1 :])
    # print(
    #     f"Max value: {max_value} at index {max_index}. Other max value: {other_max_value}"
    # )
    total_joltage += (max_value * 10) + other_max_value
    # break

print(f"Total joltage: {total_joltage}")
