"""AoC_Year2025_Day1_Part2"""

INPUT_PATH = r"input.txt"
EXAMPLE_INPUT_PATH = r"example1.txt"

numbers = []
for line in open(INPUT_PATH).read().splitlines():
    number = int(line[1:])
    actual_number = number if line[0] == "R" else -number
    numbers.append(actual_number)

answer = 0
su = 50
for number in numbers:
    # print(f"{su=}         {number=}")
    # su += number
    for _ in range(abs(number)):
        su += 1 if number > 0 else -1
        if su % 100 == 0:
            # print("Found zero at", number)
            answer += 1

print("Answer:", answer)
