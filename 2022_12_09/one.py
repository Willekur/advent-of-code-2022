#!/usr/bin/python3


INPUT_FILE = "example_input"


def main():
    lines = get_input()
    instructions = format_instructions(lines)
    generate_map(instructions)


def generate_map(instructions):
    current_position = [0,0]
    highest_position = 0
    rightest_position = 0
    for instruction in instructions:
        match instruction[0]:
            case "U":
                current_position[0] += instruction[1]
            case "D":
                current_position[0] -= instruction[1]
            case "L":
                current_position[1] -= instruction[1]
            case "R":
                current_position[1] += instruction[1]
        print(current_position)
        if current_position[0] > highest_position:
            highest_position = current_position[0]
        if current_position[1] > rightest_position:
            rightest_positiion = current_position[1]

    print(highest_position, rightest_position)




def format_instructions(lines):
    instructions = []
    for line in lines:
        split = line.split()
        instructions.append([split[0], int(split[1])])
    return instructions


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
