#!/usr/bin/python3


INPUT_FILE = "input"


def main():
    lines = get_input()
    fully_contains = 0
    for line in lines:
        split_line = line.split(",")
        elf_one = split_line[0].split("-")
        elf_two = split_line[1].split("-")
        if int(elf_one[0]) <= int(elf_two[0]) and int(elf_one[1]) >= int(elf_two[1]):
            fully_contains += 1
        elif int(elf_one[0]) >= int(elf_two[0]) and int(elf_one[1]) <= int(elf_two[1]):
            fully_contains += 1
    print(fully_contains)


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
