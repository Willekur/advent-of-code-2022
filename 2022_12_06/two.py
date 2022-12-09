#!/usr/bin/python3


INPUT_FILE = "input"

MARKER_LENGTH = 14


def main():
    lines = get_input()
    line = lines[0]
    packet_marker = []
    for i, letter in enumerate(line):
        packet_marker.append(letter)
        if len(packet_marker) > MARKER_LENGTH:
            packet_marker.pop(0)
        if len(packet_marker) == len(list(set(packet_marker))) and len(packet_marker) == MARKER_LENGTH:
            print("First start of packet marker detected at " + str(i + 1))
            print(packet_marker)
            break


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
