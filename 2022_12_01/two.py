#!/usr/bin/python3


INPUT_FILE = "aoc_2022_day01_large_input.txt"


def main():
    lines = get_input()
    highest_calories = [0, 0, 0]
    current_calories = 0
    for calories in lines:
        if calories == "":
            check_calories(highest_calories, current_calories)
            current_calories = 0
        else:
            current_calories = current_calories + int(calories)
    check_calories(highest_calories, current_calories)
    print(highest_calories[0] + highest_calories[1] + highest_calories[2])


def check_calories(highest_calories, current_calories):
    if highest_calories[0] < current_calories:
        highest_calories[2] = highest_calories[1]
        highest_calories[1] = highest_calories[0]
        highest_calories[0] = current_calories
    elif highest_calories[1] < current_calories:
        highest_calories[2] = highest_calories[1]
        highest_calories[1] = current_calories
    elif highest_calories[2] < current_calories:
        highest_calories[2] = current_calories


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
