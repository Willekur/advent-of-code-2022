#!/usr/bin/python3


INPUT_FILE = "example_input"


def main():
    lines = get_input()
    print("Hello world!")


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
