#!/usr/bin/python3


INPUT_FILE = "input"


def main():
    lines = get_input()
    dir_structure = init_dir_structure(lines)


def init_dir_structure(lines):
    global answer
    current_path = []
    all_paths = {}
    directory_structure = {}
    for line in lines:
        if line[0] == "$":
            if line[2:4] == "cd":
                match line[5:]:
                    case "..":
                        current_path.pop()
                    case "/":
                        current_path = []
                    case _:
                        current_path.append(line[5:])
        else:
            is_dir = True if line[0:3] == "dir" else False
            match len(current_path):
                case 0:
                    if is_dir:
                        directory_structure[line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[file[1]] = int(file[0])
                case 1:
                    if is_dir:
                        directory_structure[current_path[0]][line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[current_path[0]][file[1]] = int(file[0])
                case 2:
                    if is_dir:
                        directory_structure[current_path[0]][current_path[1]][line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[current_path[0]][current_path[1]][file[1]] = int(file[0])
                case 3:
                    if is_dir:
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][file[1]] = int(file[0])
                case 4:
                    if is_dir:
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][file[1]] = int(file[0])
                case 5:
                    if is_dir:
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][file[1]] = int(file[0])
                case 6:
                    if is_dir:
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][current_path[5]][line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][current_path[5]][file[1]] = int(file[0])
                case 7:
                    if is_dir:
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][current_path[5]][current_path[6]][line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][current_path[5]][current_path[6]][file[1]] = int(file[0])
                case 8:
                    if is_dir:
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][current_path[5]][current_path[6]][current_path[7]][line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][current_path[5]][current_path[6]][current_path[7]][file[1]] = int(file[0])
                case 9:
                    if is_dir:
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][current_path[5]][current_path[6]][current_path[7]][current_path[8]][line[4:]] = {}
                    else:
                        file = line.split()
                        directory_structure[current_path[0]][current_path[1]][current_path[2]][current_path[3]][current_path[4]][current_path[5]][current_path[6]][current_path[7]][current_path[8]][file[1]] = int(file[0])
    calculate_dirs(directory_structure)
    #print(answer)


answer = 70000000


def calculate_dirs(directory_structure):
    global answer
    directory_size = 0
    for item, size in directory_structure.items():
        if type(size) == dict:
            directory_size += calculate_dirs(size)
        elif type(size) == int:
            directory_size += size
    if directory_size > 8381165 and directory_size < answer:
        answer = directory_size
    print(directory_size)
    return directory_size


def get_input():
    with open(INPUT_FILE) as f:
        lines_raw = f.readlines()

    lines = []
    for line in lines_raw:
        lines.append(line.strip('\n'))

    return lines


if __name__ == "__main__":
    main()
