#!/usr/bin/python3


INPUT_FILE = "input"


def main():
    lines = get_input()
    elfs_with_overlap = 0
    for line in lines:
        split_line = line.split(",")
        elf_one = split_line[0].split("-")
        elf_two = split_line[1].split("-")
        range_one = range(int(elf_one[0]), int(elf_one[1]) + 1)
        range_two = range(int(elf_two[0]), int(elf_two[1]) + 1)
        overlap = set(range_one) & set(range_two)
        if len(overlap) > 0:
            elfs_with_overlap += 1
    print(elfs_with_overlap)
    

def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
