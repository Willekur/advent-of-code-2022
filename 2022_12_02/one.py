#!/usr/bin/python3


INPUT_FILE = "input"


CHALLENGES = {
        "A": {          # Rock
            "X": 3,     # Rock
            "Y": 6,     # Paper
            "Z": 0,     # Scissors
            },
        "B": {          # Paper
            "X": 0,     # Rock
            "Y": 3,     # Paper
            "Z": 6,     # Scissors
            },
        "C": {          # Scissors
            "X": 6,     # Rock
            "Y": 0,     # Paper
            "Z": 3,     # Scissors
            },
        }

POINTS_PER_CHOICE = {
        "X": 1,         # Rock
        "Y": 2,         # Paper
        "Z": 3,         # Scissors
        }

def main():
    lines = get_input()
    total_points = 0
    for line in lines:
        total_points = total_points + calculate_points(line.split())
    print(total_points)
        


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


def calculate_points(choices):
    return CHALLENGES[choices[0]][choices[1]] + POINTS_PER_CHOICE[choices[1]]

if __name__ == "__main__":
    main()
