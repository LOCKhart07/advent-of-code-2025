"""AoC_Year2025_Day1_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

numbers = []
for line in open(INPUT_PATH).read().splitlines():
    number = int(line[1:])
    actual_number = number if line[0] == "R" else -number
    numbers.append(actual_number)

answer = 0
su = 50
for number in numbers:
    # print(f"{su=}         {number=}")
    su += number
    if su % 100 == 0:
        # print("Found zero at", number)
        answer += 1

print("Answer:", answer)
