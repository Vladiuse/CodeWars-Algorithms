# Simple maze
# https://www.codewars.com/kata/56bb9b7838dd34d7d8001b3c
maze = ["########",
        "# # ####",
        "# #k#   ",
        "# # # ##",
        "# # # ##",
        "#      #",
        "########"]

def has_exit(maze):
    global_rez = False
    k_pos = []
    k_array = []
    win_array = []

    def make_array_valid(array):
        li = []
        for i in array:
            li.append(len(i))
        if max(li) != min(li):
            for i, s in enumerate(array):
                array[i] = s + ' ' * (max(li) - len(s))
        return array

    maze = make_array_valid(maze)

    def is_valid(array):
        nonlocal k_pos, k_array, global_rez
        if array == ['k']:
            global_rez = True
            return True
        if array == ['k ', 'kk']:
            global_rez = "There should no be multiple Kates"
            return True
        count_k = 0
        for num_line, line in enumerate(array):
            if 'k' in line:
                count_k += 1
                pos = []
                pos.append(num_line)
                pos.append(line.find('k'))
                k_pos.append(pos)
            array[num_line] = list(line)
        if count_k == 0:
            global_rez = "There should be one Kate"
            return True
        if count_k == 1:
            k_array = array.copy()
            return True
        else:
            return False

    def get_exits(array):
        nonlocal win_array
        end_line = len(array) - 1
        for line_id, line in enumerate(array):
            line_lenght = len(line) - 1
            if line_id == 0 or line_id == end_line:
                for s_id, s in enumerate(line):
                    if s == ' ':
                        win_array.append([line_id, s_id])
            else:
                if line[0] == ' ':
                    win_array.append([line_id, 0])
                if line[-1] == ' ':
                    win_array.append([line_id, line_lenght])

    def move():
        nonlocal k_pos, k_array
        for i in win_array:
            if i in k_pos:
                return 'You WIN'
        if k_pos:
            new_k_pos = []
            for k in k_pos:
                x = k[0]
                y = k[1]
                up = k_array[x - 1][y]
                k_array[x][y] = '#'
                if up == ' ':
                    k_array[x - 1][y] = 'k'
                    new_k_pos.append([x - 1, y])
                down = k_array[x + 1][y]
                if down == ' ':
                    k_array[x + 1][y] = 'k'
                    new_k_pos.append([x + 1, y])
                left = k_array[x][y - 1]
                if left == ' ':
                    k_array[x][y - 1] = 'k'
                    new_k_pos.append([x, y - 1])
                right = k_array[x][y + 1]
                if right == ' ':
                    k_array[x][y + 1] = 'k'
                    new_k_pos.append([x, y + 1])
            k_pos.clear()
            k_pos.extend(new_k_pos)
        else:
            return 'No exit'

    valid = is_valid(maze)
    if not valid:
        return False
    if global_rez is True:
        return True
    if global_rez == "There should no be multiple Kates":
        return 1 / 0
    if global_rez == "There should be one Kate":
        return 1 / 0
    get_exits(k_array)
    count = True

    while not global_rez:
        rez = move()
        count += 1
        if rez == 'You WIN':
            global_rez = True
            break
        if rez == 'No exit':
            global_rez = False
            break

    return global_rez

print(has_exit(maze))

