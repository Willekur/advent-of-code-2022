#!/usr/bin/python3


INPUT_FILE = "input"


def main():
    lines = get_input()
    tree_map = structure_input(lines)
    map_height = len(tree_map)
    map_width = len(tree_map[0])
    turned_tree_map = turn_tree_map(tree_map)

    senic_scores = []

    for verpos in range(0, map_height):
        for horpos in range(0, map_width):
            tree = tree_map[verpos][horpos]
            list_left = tree_map[verpos][:horpos]
            list_left.reverse()
            list_right = tree_map[verpos][horpos+1:]
            list_up = turned_tree_map[horpos][:verpos]
            list_up.reverse()
            list_down = turned_tree_map[horpos][verpos+1:]


            if not list_left or not list_right or not list_up or not list_down:
                continue

            # Check view distance on the left
            left_view_distance = 0
            for other_tree in list_left:
                if tree > other_tree:
                    left_view_distance = left_view_distance + 1
                else:
                    left_view_distance = left_view_distance + 1
                    break

            # Check view distance on the right
            right_view_distance = 0
            for other_tree in list_right:
                if tree > other_tree:
                    right_view_distance = right_view_distance + 1
                else:
                    right_view_distance = right_view_distance + 1
                    break

            # Check view distance on the up
            up_view_distance = 0
            for other_tree in list_up:
                if tree > other_tree:
                    up_view_distance = up_view_distance + 1
                else:
                    up_view_distance = up_view_distance + 1
                    break

            # Check view distance on the down
            down_view_distance = 0
            for other_tree in list_down:
                if tree > other_tree:
                    down_view_distance = down_view_distance + 1
                else:
                    down_view_distance = down_view_distance + 1
                    break

            senic_scores.append(calculate_senic_score(
                left_view_distance,
                right_view_distance,
                up_view_distance,
                down_view_distance,
            ))

    print("Max Senic Score: " + str(max(senic_scores)))


def structure_input(lines):
    structured_lines = []
    for line in lines:
        line_list_string = list(line)
        line_list_int = []
        for height in line_list_string:
            line_list_int.append(int(height))
        structured_lines.append(line_list_int)
    return structured_lines


def turn_tree_map(tree_map):
    width = len(tree_map[0])
    turned_map = []
    for _ in range(0, width):
        turned_map.append([])
    for verline in tree_map:
        for horpos, horval in enumerate(verline):
            turned_map[horpos].append(horval)
    return turned_map


def calculate_senic_score(left, right, up, down):
    return left * right * up * down


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
