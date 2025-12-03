"""AoC_Year2025_Day3_Part2"""

INPUT_PATH = r"input.txt"
EXAMPLE_INPUT_PATH = r"example1.txt"


with open(INPUT_PATH, "r") as f:
    banks = [list(map(int, line.strip())) for line in f]

BATTERIES_TO_TURN_ON = 12
total_joltage = 0


def get_max_with_index(bank, start, end):
    # print("bank:", bank)
    max_value = float("-inf")
    max_index = -1
    for i in range(0, len(bank)):
        if i < start or i >= end:
            continue
        # print(bank[i], end=" ")
        if bank[i] > max_value:
            max_value = bank[i]
            max_index = i
    return max_value, max_index


for bank in banks:
    # print(bank)

    batteries_turned_on = []
    max_index = -1
    to_ignore = BATTERIES_TO_TURN_ON - 1
    for _ in range(BATTERIES_TO_TURN_ON):
        max_value, max_index = get_max_with_index(
            bank, max_index + 1, len(bank) - to_ignore
        )
        to_ignore -= 1
        # print("battery selected", max_value)
        # print()
        batteries_turned_on.append(max_value)

    # print(
    #     f"Max value: {max_value} at index {max_index}. Other max value: {other_max_value}"
    # )
    total_joltage += int("".join([str(v) for v in batteries_turned_on]))
    # print(f"{total_joltage=}")
    # break

print(f"Total joltage: {total_joltage}")
