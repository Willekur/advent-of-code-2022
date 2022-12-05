#!/usr/bin/python3


INPUT_FILE = "input"


REQUIRED_RESPONSE = {
        "A": {          # Rock
            "X": 3,     # Scissors
            "Y": 1,     # Rock
            "Z": 2,     # Paper
            },
        "B": {          # Paper
            "X": 1,     # Rock
            "Y": 2,     # Paper
            "Z": 3,     # Scissors
            },
        "C": {          # Scissors
            "X": 2,     # Paper
            "Y": 3,     # Scissors
            "Z": 1,     # Rock
            },
        }

REQUIRED_TACTIC = {
        "X": 0,         # Loose
        "Y": 3,         # Draw
        "Z": 6,         # Win
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
    return REQUIRED_RESPONSE[choices[0]][choices[1]] + REQUIRED_TACTIC[choices[1]]

if __name__ == "__main__":
    main()
