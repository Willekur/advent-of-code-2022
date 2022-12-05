#!/usr/bin/python3


INPUT_FILE = "input"


def main():
    lines = get_input()
    instructions = format_instructions(lines)

#   stacks = {
#           1: ["Z", "N"],
#           2: ["M", "C", "D"],
#           3: ["P"],
#           }

    stacks = {
            1: ["L", "N", "W", "T", "D"],
            2: ["C", "P", "H"],
            3: ["W", "P", "H", "N", "D", "G", "M", "J"],
            4: ["C", "W", "S", "N", "T", "Q", "L"],
            5: ["P", "H", "C", "N"],
            6: ["T", "H", "N", "D", "M", "W", "Q", "B"],
            7: ["M", "B", "R", "J", "G", "S", "L"],
            8: ["Z", "N", "W", "G", "V", "B", "R", "T"],
            9: ["W", "G", "D", "N", "P", "L"],
            }

    for instruction in instructions:
        picked_up = []
        for block in range(0, instruction[0]):
            picked_up.append(stacks[instruction[1]].pop())
        for block in range(0, instruction[0]):
            stacks[instruction[2]].append(picked_up.pop())
    for stack in stacks.values():
        print(stack[-1:])


def format_instructions(lines):
    instructions = list()
    for line in lines:
        if line[:4] == "move":
            instructions.append([int(line[5:7]), int(line[12:14]), int(line[-1:])])
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
