#!/usr/bin/python3


INPUT_FILE = "aoc_2022_day01_large_input.txt"


def main():
    lines = get_input()
    highest_calories = 0
    current_calories = 0
    for calories in lines:
        if calories == "":
            if highest_calories < current_calories:
                highest_calories = current_calories
                current_calories = 0
        else:
            current_calories = current_calories + int(calories)
    print(highest_calories)


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
