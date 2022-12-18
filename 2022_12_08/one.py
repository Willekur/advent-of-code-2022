#!/usr/bin/python3


INPUT_FILE = "input"


def main():
    lines = get_input()
    tree_map = structure_input(lines)
    map_height = len(tree_map)
    map_width = len(tree_map[0])
    boolean_map = build_boolean_map(map_height, map_width)
    turned_tree_map = turn_tree_map(tree_map)

    for verpos in range(0, map_height):
        for horpos in range(0, map_width):
            tree = tree_map[verpos][horpos]
            visible = False
            if all(tree > other_tree for other_tree in tree_map[verpos][:horpos]):
                visible = True
            if all(tree > other_tree for other_tree in tree_map[verpos][horpos+1:]):
                visible = True
            if all(tree > other_tree for other_tree in turned_tree_map[horpos][:verpos]):
                visible = True
            if all(tree > other_tree for other_tree in turned_tree_map[horpos][verpos+1:]):
                visible = True
            boolean_map[verpos][horpos] = visible

    counter = 0
    for line in boolean_map:
        for value in line:
            if value:
                counter = counter + 1
    print(counter)


def turn_tree_map(tree_map):
    width = len(tree_map[0])
    turned_map = []
    for _ in range(0, width):
        turned_map.append([])
    for verline in tree_map:
        for horpos, horval in enumerate(verline):
            turned_map[horpos].append(horval)
    return turned_map


def structure_input(lines):
    structured_lines = []
    for line in lines:
        line_list_string = list(line)
        line_list_int = []
        for height in line_list_string:
            line_list_int.append(int(height))
        structured_lines.append(line_list_int)
    return structured_lines


def build_boolean_map(height, width):
    boolean_map = []
    for _ in range(0, height):
        verticle_line = []
        for _ in range(0, width):
            verticle_line.append(False)
        boolean_map.append(verticle_line)
    return boolean_map


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
